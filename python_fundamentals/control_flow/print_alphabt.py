#!/usr/bin/env python3
#forbidden values 101, 113
for x in range (97, 123):
    if x == 101 or x == 113:
        continue
    print(chr(x), end="")
