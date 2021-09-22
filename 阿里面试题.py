def list1(a):
    dict={}
    set1=set(a)
    # for key in a:
    #     dict[key]=dict.get(key,0)+1
    # print(dict)
    for item in set1:
        dict.update({item:a.count(item)})
    print(dict)

b=[21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
list1(b)