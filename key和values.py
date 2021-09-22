dict = {"k1":"v1","k2":"v2","k3":"v3"}
for c in dict:
    print(c)
for b in dict.keys():
    print(b)
for d in dict.values():
    print(d)
for a in dict:
    print(dict[a])

dict['k4']='v4'
print(dict)