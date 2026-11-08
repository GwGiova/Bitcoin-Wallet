import OPCODES

def ScriptSigForP2PK(Signature_Bytes):

    SignatureLenght_Bytes = str(len(Signature_Bytes))

    Field1_Bytes = bytes([OPCODES.OPCODE_BYTES[f"OP_PUSHBYTES_{SignatureLenght_Bytes}"]])

    Field2_Bytes = Signature_Bytes

    P2PKScriptSig_Bytes = Field1_Bytes + Field2_Bytes

    return P2PKScriptSig_Bytes