import random

# Define the 32-bit LFSR polynomial as a binary string
POLY = "100000100110000010001110110110111"

def lfsr(seed):
    """
    Generates a random 32-bit integer using a 32-bit LFSR polynomial.
    """
    # Initialize the LFSR with the given seed
    state = int(seed, 2)

    # Iterate the LFSR until a full cycle is completed
    for i in range(32):
        # Extract the rightmost bit from the current state
        bit = state & 1

        # Shift the current state to the right by 1 bit
        state >>= 1

        # If the rightmost bit was a 1, XOR the current state with the polynomial
        if bit == 1:
            state ^= int(POLY, 2)

    # Return the final state as a 32-bit integer
    return state & 0xFFFFFFFF

# Generate a random 32-bit integer using a random seed
seed = bin(random.getrandbits(32))[2:].zfill(32)
random_int = lfsr(seed)

# Print the results
print("Seed:      ", seed)
print("Random int:", random_int)

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

import math
import random
i = 2 
k = 11
pos = round(abs(math.sin(i +k))* (2**32))
#print(pos)

 
# a random number with 4 bits
a=random.getrandbits(128)
print(a)
a=bin(a)
print(a)
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

