import OPCODES

def ScriptPubKeyForP2PK(PubKey_Bytes, IsItCompressed_Bool):

#Field1 must be 0x41 or 0x21 because the public key has to be pushed in the stack, in order to be checked with the signature
#If the public key is not compressed, the value is 0x41, else, 0x21

#Field2 is the public key, that has to be compared with the signature

#Field3 is the OPCODE of CHECKSIG

    if(IsItCompressed_Bool == 0):


        Field1_Bytes = bytes([OPCODES.OPCODE_BYTES["OP_PUSHBYTES_65"]])

    else:

        Field1_Bytes = bytes([OPCODES.OPCODE_BYTES["OP_PUSHBYTES_33"]])
    
    Field2_Bytes = PubKey_Bytes
    
    Field3_Bytes = bytes([OPCODES.OPCODE_BYTES["OP_CHECKSIG"]])

    P2PKScriptPubKey_Bytes = Field1_Bytes + Field2_Bytes + Field3_Bytes

    return P2PKScriptPubKey_Bytes

def ScriptPubKeyForP2PKH(PubKeyHash_Bytes):

    Field1_Bytes = bytes([OPCODES.OPCODE_BYTES["OP_DUP"]])

    Field2_Bytes = bytes([OPCODES.OPCODE_BYTES["OP_HASH160"]])

    Field3_Bytes = bytes([OPCODES.OPCODE_BYTES["OP_PUSHBYTES_20"]])

    Field4_Bytes = PubKeyHash_Bytes

    Field5_Bytes = bytes([OPCODES.OPCODE_BYTES["OP_EQUALVERIFY"]])

    Field6_Bytes = bytes([OPCODES.OPCODE_BYTES["OP_CHECKSIG"]])

    P2PKHScriptPubKey_Bytes = Field1_Bytes + Field2_Bytes + Field3_Bytes + Field4_Bytes + Field5_Bytes + Field6_Bytes

    return P2PKHScriptPubKey_Bytes