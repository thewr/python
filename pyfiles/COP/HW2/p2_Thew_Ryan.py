import math


# p2 (a)
n = 100
list_p2a = []
for c in range(1, n):
    for a in range(1, c):
        b = math.sqrt(c ** 2 - a ** 2)

        if (b % 2 == 0) or ((b + 1) % 2 == 0):
            ''' if even or odd integer, add to list of tupples'''
            b = int(b)
            list_p2a.append((a, b, c))

#print('(a, b, c)')
#for tupple in list_p2a:
#   print(tupple)



# p2 (b)
def capitalize_all(word):
    word_capped = ""
    for c in word:
        word_capped += c.capitalize()
    return word_capped

old = ['one', 'seven', 'three', 'two', 'ten', 'thirty-three']
new = []
for word in old:
    word_len = len(word)
    if word_len > 3:
        new.append((word_len, capitalize_all(word)))

print(new)
#p2 (c)
names = ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]
new_names = []
for i in range(0,len(names)):
    name = names[0]  #get peek of names
    first, last = name.split(' ')
    names.remove(name)   #remove old format
    name = last +", " + first
    names.append(name)      #add new

print(names)

#p2 (d)
def concatenate(seperator, *args):
    if(len(args)==1):
        return args[0]
    else:
        out = ''
        for arg in args:
            if arg == args[-1]: #if last argument
                out += arg
            else:
                out += arg + seperator

        return out

print(concatenate(" and ","Hootie","The Blowfish"))
