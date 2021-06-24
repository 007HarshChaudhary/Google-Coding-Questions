# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:20:40 2020

@author: Harsh Chaudhary
"""

#Encrypting Google foo.bar 2017 encrypted message
#Algo-> Decode the message string to base64 bytes.
#       and do XOR of decoded bytes with your Google username.

import base64

#The encrypted key
message='D08WHQYRChoARUFZS0YAEwwPAE9JSEIRAAUfBwAEHgRAQVNOUw0WHAAXAgwXRU1DTAQBBwYcABtC SF9SSAAdARMGDwgFDQxJWEhCCQYaBgwFBwwGBRVAQVNOUx0LBAoRBAwXRU1DTBMGAwsHABtCSF9S SBoSBARER0FABwYBU0hfSEIFBgdSRRw='

#Your Google username
key='theheroisbackagain'

decrypted_message=[]

#decode the key to base64 bytes
dec_bytes=base64.b64decode(message)

#XOR with Username
for a,b in enumerate(dec_bytes):
    decrypted_message.append(chr(b ^ ord(key[a%len(key)])))

#The encypted message
print("".join(decrypted_message))
