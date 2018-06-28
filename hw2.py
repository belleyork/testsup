n= input("Enter lines of text at the keyboard")
# print(sorted(n, key=Counter(a).get, reverse= True))

n=sorted(n, key=n.count, reverse=True)

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
            print(n)
    return dict


print(char_frequency(n))
