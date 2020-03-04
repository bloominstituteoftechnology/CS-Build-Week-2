import itertools

directions = [ 'n','w','e','e','e','s','w','s','s','n','e','e','e','e']
    #   [['n'], ['w'], ['e', 'e', 'e'], ['s'], ['w'], ['s', 's'], ['n'], ['e', 'e', 'e', 'e']]
ids = [   1,    3,     4,   5,   55,    7,     8,     9 ,  2,     56,    233, 51,  44,   67]
length  = max(len(list(v)) for g,v in itertools.groupby(directions))
listy = [list(v) for g,v in itertools.groupby(directions)]
listy_ids = [list(v) for g,v in itertools.groupby(ids)]
v = [v for g,v in itertools.groupby(directions)]
g = [g for g,v in itertools.groupby(directions)]


print(f'length: {length}')
print(f'listy: {listy}')
print(f'v: {v}')
print(f'g: {g}')
temp_length = 0
counter = 0
for i in range(len(listy)):
    length = len(listy[i])
    

    print(listy[i])
    # print(ids[i:(i+temp_length)])
    temp_length += length
    print(ids[counter:temp_length])
    ids_str = str(ids[counter:temp_length]).strip('[]')
    print(ids_str)
    dir = listy[i][0]
    data = '{"direction":"'+ dir +'", "num_rooms":"' + str(length) + '", "next_room_ids":"' + ids_str + '"}'
    data = '{"direction":"n", "num_rooms":"5", "next_room_ids":"10,19,20,63,72"}'
    counter = temp_length