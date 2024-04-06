import io
import sys

from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
from charm.adapters.abenc_adapt_hybrid import HybridABEnc
from charm.core.engine.util import objectToBytes

group = PairingGroup('SS512')
cpabe = CPabe_BSW07(group)
hybrid_Abe = HybridABEnc(cpabe, group)

(master_public_key, master_key) = hybrid_Abe.setup()

with open("./master_public_key.txt", "wb") as f:
    f.write(objectToBytes(master_public_key, group))
    
with open("./master_key.txt", "wb") as f:
    f.write(objectToBytes(master_key, group))

print("Done! The files are 'master_public_key.txt' and 'master_key.txt'.\nPlease use these keys for generating user keys, and file encryption/decryption")