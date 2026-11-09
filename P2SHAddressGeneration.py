import base58

def P2SHAddressRepresentation(RedeemScriptHASH160_Bytes):

    Prefix_Bytes = b'\x05'

    Base58Payload_Bytes = Prefix_Bytes + RedeemScriptHASH160_Bytes

    P2SHAddress = base58.b58encode(Base58Payload_Bytes).decode()

    return P2SHAddress