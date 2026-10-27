<<<<<<< HEAD
import hashlib
import hmac


def GenerateMasterPrivateKeyAndMasterChainCode(MnemonicSeed_Str):

    #I Inserted this constant variable to that if one day the BIP39 standard may change, the developers
    #Can change the value of it, instead of directly writing the value in the function
    KEY_STR = "Bitcoin seed"

    HashOfSeedAndKey_Str = hmac.new(KEY_STR.encode(), bytes.fromhex(MnemonicSeed_Str), hashlib.sha512).digest().hex()

    #The master private key as defined in the BIP32 standard, is the first 32 byte of the seed's + key resulting hash
    MasterPrivateKey_Str = HashOfSeedAndKey_Str[0:64]     #First 32 byte
    #The master chain code as defined in the BIP32 standard, is the last 32 byte of the seed's + key resulting hash
    MasterChainCode_Str = HashOfSeedAndKey_Str[64:128]    #Last 32 byte
=======
import hashlib
import hmac
from ecdsa import SECP256k1


def GenerateMasterPrivateKeyAndMasterChainCode(MnemonicSeed_Str):

    #I Inserted this constant variable to that if one day the BIP39 standard may change, the developers
    #Can change the value of it, instead of directly writing the value in the function
    KEY_STR = "Bitcoin seed"

    HashOfSeedAndKey_Str = hmac.new(KEY_STR.encode(), MnemonicSeed_Str.encode(), hashlib.sha512).digest().hex()

    #The master private key as defined in the BIP32 standard, is the first 32 byte of the seed's + key resulting hash
    MasterPrivateKey_Str = HashOfSeedAndKey_Str[0:64]     #First 32 byte
    #The master chain code as defined in the BIP32 standard, is the last 32 byte of the seed's + key resulting hash
    MasterChainCode_Str = HashOfSeedAndKey_Str[64:128]    #Last 32 byte

    G = SECP256k1.generator

    MasterPublicKey_Str = MasterPrivateKey_Str * G

    print(hex(MasterPublicKey_Str.x()))
    print(hex(MasterPublicKey_Str.y()))
>>>>>>> master
