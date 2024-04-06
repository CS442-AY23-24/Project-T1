import io
import sys

from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.core.engine.util import objectToBytes, bytesToObject

group = PairingGroup('SS512')
cpabe = CPabe_BSW07(group)
hybrid_Abe = HybridABEnc(cpabe, group)

file_input = input("File to encrypt: ")
try:
    with open(file_input, "rb") as f:
        msg = f.read()
except Exception:
    print("Error with ", file_input," file, please check and try again")
    exit()
    
master_pk_input = input("Master Public Key File: ")
try:
    with open(master_pk_input, "rb") as f:
        master_pk = bytesToObject(f.read(), group)
except Exception:
    print("Error with ", master_pk_input," file, please check and try again")
    exit()
    
access_policy_input = input("Enter access policy file or type out the access policy rules: ")
try:
    with open(access_policy_input, "r") as f:
        access_policy = f.read()
except Exception:
    access_policy = access_policy_input

cipher_text = hybrid_Abe.encrypt(master_pk, msg, access_policy)

filename = "./" + file_input + "%encrypted.txt"
with open(filename, "wb") as f:
    f.write(objectToBytes(cipher_text, group))

print("Done! File is at ", filename)