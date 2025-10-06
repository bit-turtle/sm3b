# sm3b python implementation,written while having my font set to aurebesh

import sys

prg = sys.argv[1]

x = 0
y = 0
a = 0
i = 0
m = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
c = 0
f = False

def disp():
    print(f"x = {x}, y = {y}, a = {a}, i = {i}, m[a] = {m[a]}, c = {c}, f = {f}")

disp()
while i < len(prg):
    inst = prg[i]
    if inst == '?':
        if x == 0:
            t = i
            i = a
            a = t
            disp()
            continue
    i += 1    
    if inst == '0':
        if f:
            f = True
            x = 0
        else:
            x *= 2
        disp()
        continue
    elif inst == '1':
        if f:
            f = True
            x = 1
        else:
            x *= 2
            x += 1
        disp()
        continue
    f = False
    if inst == '+':
        c += x
        x = c
    elif inst == '-':
        c -= x
        x = c
    elif inst == '#':
        t = x
        x = y
        y = t
    elif inst == '@':
        t = x
        x = a
        a = t
    elif inst == '#':
        t = x
        x = m[a]
        m[a] = t
    disp()
