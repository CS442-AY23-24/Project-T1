import io
import sys

from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.core.engine.util import objectToBytes, bytesToObject

group = PairingGroup('SS512')
cpabe = CPabe_BSW07(group)
hybrid_Abe = HybridABEnc(cpabe, group)

secret_key_input = input("User Secret Key File: ")
try:
    with open(secret_key_input, "rb") as f:
        secret_key = bytesToObject(f.read(), group)
except Exception:
    print("Error with ", secret_key_input," file, please check and try again")
    exit()

master_pk_input = input("Master Public Key File: ")
try:
    with open(master_pk_input, "rb") as f:
        master_pk = bytesToObject(f.read(), group)
except Exception:
    print("Error with ", master_pk_input," file, please check and try again")
    exit()
    
cipher_text_input = input("Enter encrypted file: ")
try:
    with open(cipher_text_input, "rb") as f:
        cipher_text = bytesToObject(f.read(), group)
except Exception:
    print("Error with ", cipher_text_input," file, please check and try again")
    exit()

decrypted_msg = hybrid_Abe.decrypt(master_pk, secret_key, cipher_text)

filename = "./" + cipher_text_input.split("%")[0]
with open(filename, "wb") as f:
    f.write(decrypted_msg)

print("Done! File is at ", filename)