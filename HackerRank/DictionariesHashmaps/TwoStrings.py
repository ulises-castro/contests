#!/bin/python3

import math
import os
import random
import re
import sys

def twoStrings(s1, s2):
    ABC = [0] * 28;

    for pos in s1:
        getCode = ord(pos) - 97;
        ABC[getCode] = 1;

    for pos in s2:
        getCode = ord(pos) - 97;
        if( ABC[getCode] ):
            return 'YES'

    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        fptr.write(result + '\n')

    fptr.close()
