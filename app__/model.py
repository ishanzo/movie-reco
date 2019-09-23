import random
import numpy as np
import collections

def movie_recomendor_1(hash):
    #movies
    animated = ["The Incredibles", "Ratatouille", "Wreck-It Ralph", "Coraline","Tangled","Mulan"]
    chick_flick = ["The Notebook","Mean Girls","The Proposal","She's the Man","Mis Congeniality"]
    horror = ["It", "Annabelle Comes Home", "Pyscho","The Ring"]
    mystery = ["Gone Girl", "Murder on the Orient Express","The Da Vinci Code", "Arrival"]
    count = 0
    highest = 0
    compare = []
    for key, value in hash.items:
        for n in animated:
            if hash[key] == animated[n]:
                animated_count = + 1
        compare.append(count)
        for c in chick_flick:
            if hash[key] == chick_flick[c]:
                chick_flick_count = + 1
        compare.append(count)
        for h in horror:
            if hash[key] == horror[h]:
                horror_count = + 1
        compare.append(count)
        for m in mystery:
            if hash[key] == mystery[m]:
                mystery_count = + 1
        compare.append(count)
        for y in compare:
            if n > highest:
                highest = n
        return highest
        if highest == animated_count:
            return "Spider-Man: Into the Spider-Verse"
        if highest == chick_flick_count:
            return "White Chicks"
        if highest == horror_count:
            return "A Quiet Place"
        if highest == mystery_count:
            return "The Inivisble Guest (Contratiempo)"

    print(compare)


def movie_recomendor_2 (user_movies):
    animated = ["The Incredibles", "Ratatouille", "Wreck-It Ralph", "Coraline","Tangled","Mulan"]
    chick_flick = ["The Notebook","Mean Girls","The Proposal","She's the Man","Mis Congeniality"]
    horror = ["It", "Annabelle Comes Home", "Pyscho","The Ring"]
    mystery = ["Gone Girl", "Murder on the Orient Express","The Da Vinci Code", "Arrival"]
    movie_lists = [animated,chick_flick,horror,mystery]

    category_freq = {}
    #get frequency of user favourite movies in each movie list
    for category in movie_lists:
        freq = len(set(category) &  set(user_movies))
        category_freq[tuple(category)] = freq
    #order dictionary by most frequent movie list
    category_freq = sorted(category_freq.items(), key=lambda kv: kv[1], reverse= True)
    category_freq = collections.OrderedDict(category_freq)
    #get most frequent movie list
    user_movie_list = list(list(category_freq)[0])
    #remove all movies in most frequent movie list that have already been seen
    unseen_movies_list = [x for x in user_movie_list if x not in user_movies]
    return unseen_movies_list

print(movie_recomendor_2 (["Ratatouille", "Pyscho", "The Ring", "It"]))
