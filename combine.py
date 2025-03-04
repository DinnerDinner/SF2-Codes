def combine(d1,d2): 
    new_dict = {}
    for key in d1:
        if key in d2:
            new_dict[key] = new_dict.get(key, 0) + sum(d1[key])+sum(d2[key])
    return(new_dict)      
d1 = {1:[2], 4:[5,6]}
d2 = {4:[8], 1:[24]}

print(combine(d1,d2))