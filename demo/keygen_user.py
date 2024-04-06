import io
import sys

from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.core.engine.util import objectToBytes, bytesToObject

group = PairingGroup('SS512')
cpabe = CPabe_BSW07(group)
hybrid_Abe = HybridABEnc(cpabe, group)

user = input("Who is the user: ")

master_key_input = input("Master Key File: ")
try:
    with open(master_key_input, "rb") as f:
        master_key = bytesToObject(f.read(), group)
except Exception:
    print("Error with ", master_key_input," file, please check and try again")
    exit()

master_pk_input = input("Master Public Key File: ")
try:
    with open(master_pk_input, "rb") as f:
        master_pk = bytesToObject(f.read(), group)
except Exception:
    print("Error with ", master_pk_input," file, please check and try again")
    exit()
    
attr_input = input("Enter attribute file or list of attributes separated by whitespace: ")
try:
    with open(attr_input, "r") as f:
        attributes = f.read().splitlines()
except Exception:
    attributes = attr_input.split()

secret_key = hybrid_Abe.keygen(master_pk, master_key, attributes)

filename = "./" + user + ".txt"
with open(filename, "wb") as f:
    f.write(objectToBytes(secret_key, group))

print("Done! File is at ", filename)