import numpy as np

def apriori (set_, min_support):
    #calculate support
    item2support = {}
    one_d_set_ = list(np.hstack(set_))
    one_d_set_singular = list(set(one_d_set_))
    all_pairs = []
    for i in range (len(one_d_set_singular)):
        item2support[i] = one_d_set_.count(i)
        #get all pairs
        for j in range (len(one_d_set_singular)):
            if one_d_set_singular[i] != one_d_set_singular[j] and [one_d_set_singular[i], one_d_set_singular[j]] not in all_pairs and [one_d_set_singular[j], one_d_set_singular[i]] not in all_pairs:
                all_pairs.append([one_d_set_singular[i], one_d_set_singular[j]])

    #calculate confidence
    subset2support = {}
    for pair in all_pairs:
        pair_freq = 0
        for s in set_:
            if pair[0] in s and pair[1] in s:
                pair_freq +=1
        subset2support[tuple(pair)] = pair_freq

    pruned_set_ = []
    #prune initial set
    for s in set_:
        flag = False
        for point in s:
            if item2support.get(point) < min_support:
                flag = True

        for pair in all_pairs:
            t1,t2 = pair
            if subset2support.get(tuple(pair)) <= min_support:
                if t1 in s and t2 in s:
                    flag = True
        if not flag and len(s) > 2:
            pruned_set_.append(s)
    return pruned_set_

set_ = np.array([[0,1,2,3], [0,1,3], [0,1], [1,2,3], [1,2], [2,3], [1,3]])
print(apriori (set_, 2))
