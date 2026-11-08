import OPCODES

def ScriptSigForP2PK(Signature_Bytes):

    SignatureLenght_Bytes = str(len(Signature_Bytes))

    Field1_Bytes = bytes([OPCODES.OPCODE_BYTES[f"OP_PUSHBYTES_{SignatureLenght_Bytes}"]])

    Field2_Bytes = Signature_Bytes

    P2PKScriptSig_Bytes = Field1_Bytes + Field2_Bytes

    return P2PKScriptSig_Bytes

def ScriptSigForP2PKH(Signature_Bytes, PubKey_Bytes):

    PubKeyLenght_Str = str(len(PubKey_Bytes))

    SignatureLenght_Str = str(len(Signature_Bytes))

    Field1_Bytes = bytes([OPCODES.OPCODE_BYTES[f"OP_PUSHBYTES_{SignatureLenght_Str}"]])

    Field2_Bytes = Signature_Bytes

    Field3_Bytes = bytes([OPCODES.OPCODE_BYTES[f"OP_PUSHBYTES_{PubKeyLenght_Str}"]])

    Field4_Bytes = PubKey_Bytes

    P2PKHScriptSig_Bytes = Field1_Bytes + Field2_Bytes + Field3_Bytes + Field4_Bytes

    return P2PKHScriptSig_Bytes

def ScriptSigForP2MS(SignaturesArray):

    Field1_Bytes = bytes([OPCODES.OPCODE_BYTES["OP_0"]])

    P2MSScriptSig_Bytes = Field1_Bytes

    for i in range(len(SignaturesArray)):

        Signature = SignaturesArray.pop()

        Field_Bytes = bytes([OPCODES.OPCODE_BYTES[f"OP_PUSHBYTES_{len(Signature)}"]])

        P2MSScriptSig_Bytes += Field_Bytes

        P2MSScriptSig_Bytes += Signature