import hashlib
import base58

#The creation of a P2PKH address (Pay 2 Public Key Hash) requires the public key as the input.
#The public key is then passed into a sha256 function, generating an hash long 256 bits.
#The resulting hash is finally passed in the RIPEMD160 function, that returns a 160 bits hash, which is the 
#P2PKH address.
def CreateTheP2PKHAddress(PublicKey_Str):

    PublicKey_Bytes = bytes.fromhex(PublicKey_Str)

    Hash256BitsOfPublicKey_Bytes = hashlib.sha256(PublicKey_Bytes).digest()

    Hash256BitsOfPublicKey_Str = Hash256BitsOfPublicKey_Bytes.hex()

    ripemd160 = hashlib.new("ripemd160")

    ripemd160.update(Hash256BitsOfPublicKey_Bytes)

    #RAW P2PKH address format, without encoding.
    P2PKHAddress_Bytes = ripemd160.digest()

    P2PKHAddress_Str = P2PKHAddress_Bytes.hex()

    return P2PKHAddress_Str

#This function expects a P2PKH raw address in string format
def ConversionInBase58Check(P2PKHAddress_Str):

    Prefix_Bytes = b"\x00"
    
    P2PKHAddress_Bytes = bytes.fromhex(P2PKHAddress_Str)

    CompleteP2PKHAddress_Bytes = Prefix_Bytes + P2PKHAddress_Bytes

    FirstSha256_Bytes = hashlib.sha256(CompleteP2PKHAddress_Bytes).digest()

    SecondSha256_Bytes = hashlib.sha256(FirstSha256_Bytes).digest()

    Checksum_Bytes = SecondSha256_Bytes[:4]

    PayloadBase58Check = CompleteP2PKHAddress_Bytes + Checksum_Bytes

    Base58CheckAddress_Str = base58.b58encode(PayloadBase58Check).decode()

    return Base58CheckAddress_Str