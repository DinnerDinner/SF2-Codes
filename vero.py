# # tup = ('grape', 33.12, [98, 99], 'apricot')
# # lst = tup[2]
# # tup[2][0] = 77
# # lst.append('tomato')
# # print(tup)
# # print(lst)

# dic = {"a": 2, "b": 3, 'c': 312,'d':"does exist"}
# dic['d'] = dic.get('d',69)
# dic['e'] = 420
# dic.update({'d':42069, 'ab':0})
# print(sorted(dic.valu))
# print(dic)


def check(n,k):
    new_dict = {}
    for word in n.split():
        if word not in new_dict:
            new_dict.update({word:1})
        else:
            new_dict[word]+=1
    all = sorted(new_dict.values(), reverse=True)
    clean = list(set(all))
    clean.sort(reverse=True)
    if clean != all[:len(clean)] or k>len(clean):
        return 'nah it dont be nothing as common isnt the true common'
    else:
        key = [key for key, val in new_dict.items() if val == clean[k-1]]
    return key[0]

print(check("a a b b c a b c s s s s s", 1))