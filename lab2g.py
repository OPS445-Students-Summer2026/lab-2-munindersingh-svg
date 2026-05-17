#!/usr/bin/env python3
#Author: Muninder Singh
#Author ID: 123266249
#Date Created: 2025/9/20

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
