import io
import sys

from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.core.engine.util import objectToBytes, bytesToObject

group = PairingGroup('SS512')
cpabe = CPabe_BSW07(group)
hybrid_Abe = HybridABEnc(cpabe, group)

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

users = [
{
    "name": "S1_1SIR",
    "attributes": ["S1", "1SIR", "HQ", "RESTRICTED", "CONFIDENTIAL", "SECRET"] 
},
{
    "name": "S4_1SIR", 
    "attributes": ["S4", "1SIR", "HQ", "RESTRICTED", "CONFIDENTIAL", "SECRET"] 
},
{
    "name": "OC_A_1SIR", 
    "attributes": ["OC", "1SIR", "A", "RESTRICTED", "CONFIDENTIAL", "SECRET"] 
},
{
    "name": "OC_B_1SIR", 
    "attributes": ["OC", "1SIR", "B", "RESTRICTED", "CONFIDENTIAL", "SECRET"] 
},
{
    "name": "SGT_A1_1SIR", 
    "attributes": ["PLT SGT", "1SIR", "A", "RESTRICTED"] 
},
{
    "name": "SGT_A2_1SIR", 
    "attributes": ["PLT SGT", "1SIR", "A", "RESTRICTED", "CONFIDENTIAL"] 
},
{
    "name": "CO_1SIR", 
    "attributes": ["CO", "1SIR", "HQ", "RESTRICTED", "CONFIDENTIAL", "SECRET", "TOPSECRET"] 
},
{
    "name": "CO_16C4I",
    "attributes": ["CO", "16C4I", "HQ", "RESTRICTED", "CONFIDENTIAL", "SECRET", "TOPSECRET"] 
}]

for user in users: 
    secret_key = hybrid_Abe.keygen(master_pk, master_key, user["attributes"])

    filename = "./" + user["name"] + ".txt"
    with open(filename, "wb") as f:
        f.write(objectToBytes(secret_key, group))

    print("Done! File is at ", filename)