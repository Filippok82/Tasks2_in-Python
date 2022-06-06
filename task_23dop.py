#!/usr/bin/python3
 
s = '?0?+?01=1??'
 
a, bc = s.split('+')
b, c = bc.split('=')
del bc
assert len(a) == len(b) == len(c)
 
r1, r2, r3 = [], [], []
flag = 0
for a1, a2, a3 in zip(reversed(a), reversed(b), reversed(c)):
    if a1 != '?' and a2 != '?' and a3 == '?':
        a3 = int(a1) + int(a2) + flag
        flag = 0
        if a3 > 10:
            a3 -= 10
            flag = 1
        a3 = str(a3)
    elif a1 == '?' and a2 != '?' and a3 != '?':
        a1 = int(a3) - int(a2) + flag
        flag = 0
        if a1 > 10:
            a1 -= 10
            flag = 1
        a1 = str(a1)
    elif a1 != '?' and a2 == '?' and a3 != '?':
        a2 = int(a3) - int(a1) + flag
        flag = 0
        if a2 > 10:
            a2 -= 10
            flag = 1
        a2 = str(a2)
    elif a1 == '?' and a2 != '?' and a3 == '?':
        a1 = '0'
        a3 = int(a1) + int(a2)
        a3 = str(a3)
    elif a1 != '?' and a2 == '?' and a3 == '?':
        a2 = '0'
        a3 = int(a1) + int(a2)
        a3 = str(a3)
    elif a1 == '?' and a2 == '?' and a3 != '?':
        a1 = '0'
        a2 = a3
    else:
        raise NotImplementedError(a1, a2, a3)
    r1 = [a1] + r1
    r2 = [a2] + r2
    r3 = [a3] + r3
 
print('%s+%s=%s' % (''.join(r1), ''.join(r2), ''.join(r3)))