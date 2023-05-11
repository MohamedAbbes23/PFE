import numpy as np
from pylfsr import LFSR

state = [0,0,0,1,0]
fpoly = [5,3]
L = LFSR(fpoly=fpoly,initstate =state)

# Generate K-bits
k=10
seq_k  = L.runKCycle(k)

print('10 bits')
print(L.arr2str(seq_k))
print('')


# Generate bits of one full period.
# Expected period of LFSR = 2^M-1, for M-bit LFSR).
seq_full  = L.runFullPeriod()

print('Full period of LFSR = 31-cycles')
print(L.arr2str(seq_full))

L.Viz()
#*************************************************
# Importing math Library
import math
# This will print the value of pi in the output
print (math.pi)
#*************************************************
xor_num = num1 ^ num2



import hashlib
 
# encoding GeeksforGeeks using md5 hash
# function
result = hashlib.md5(b'GeeksforGeeks')
 
# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end ="")
print(result.digest())



import math
i = 2 
k = 11
pos = round(abs(math.sin(i +k))* (2**32))
print(pos)
