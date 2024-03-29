"""Given a word w, rearrange the letters of w to construct another word s in such a way that, s is lexicographically greater than w. 
In case of multiple possible answers, find the lexicographically smallest one."""

import string
t = input()
w = [0]*t
alpha = list(string.ascii_lowercase)
for i in range(t):
    w[i] = input()
    if (any(p.isdigit() for p in w[i])):
        print()
    else:
        listw = list(w[i])
        x = len(w[i])-1
        while (x>0) and (listw[x]<=listw[x-1]):
            x-=1
           
        x -= 1
        b = listw[x:len(listw)]
        bindiff = [0]*len(b)
        for u in range(0,len(b)):
            bindiff[u] = alpha.index(b[u]) - alpha.index(b[0])
        mins = (filter(lambda x: x > 0, bindiff))
        if (mins != []): 
            y = bindiff.index(min(mins))
            l = b[0]
            b[0] = b[y]
            b[y] = l
            bcut = b[1:len(b)]
            bcut.sort()
            b[1:len(b)] = bcut
            listw[x:len(listw)] = b
                

        neww = ''.join(listw)
        if neww > w[i]:
            print(neww)
        else: 
            print('no answer')
