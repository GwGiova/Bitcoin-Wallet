import secrets
import hashlib
import MnemonicWordsList

def GeneratingNumberWithEntropy(EntropyChosenByTheUser_Int):

    NumberWithEntropyChosen_Int = secrets.randbits(EntropyChosenByTheUser_Int)

    return NumberWithEntropyChosen_Int

def CalculatingTheChecksum(NumberWithEntropyChosenInBitRepresentation_Str, EntropyChosenByTheUser_Int):

    #Explaining the following line of code:
    #hashlib.sha256() wants a byte variable as an argument, so inside it I included
    #(NumberWithEntropyChosenInBitRepresentation_Str.encode()) to make the variabile in byte format
    #Then i took the digest, from the sha256 hash object returned, and because digest() returns a byte variable
    #I converted it in a hex string format with hex()
    HashInHexFormat_Str = hashlib.sha256((NumberWithEntropyChosenInBitRepresentation_Str.encode())).digest().hex()

    #Explaining the following line of code:
    #Inside the bin() function i convert the Hash in the Hexadecimal format, into its int representation
    #Then it is transformed into his binary representation
    #The [2:] is used to remove the initial '0b' string infront of our binary representation
    #Then the zfill(256) adds a padding to the resulting Hash, so that if it starts with less zeroes (Ex: 001111011111)
    #It will be shown as a number with exactly 256 bits (The SHA256 output) and wont invalidate the ENT/32
    HashInBinFormat_Str = bin(int(HashInHexFormat_Str, 16))[2:].zfill(256)

    #According to the BIP39 standard, the checksum is the first (Entropy/32) bits from the number's resulting hash
    BitsToTakeFromTheCheckum_Int = EntropyChosenByTheUser_Int  // 32

    Checksum_Str = HashInBinFormat_Str[:BitsToTakeFromTheCheckum_Int].zfill(BitsToTakeFromTheCheckum_Int)

    return Checksum_Str

def GeneratingMnemonicWords(NumberPlusChecksum_Str):

    Word_Str = " "

    Counter_Int = 0

    StringContainingAllWords_Str = ""

    while Counter_Int + 11 <= len(NumberPlusChecksum_Str):

        GroupOf11Bits_Str = NumberPlusChecksum_Str[Counter_Int:Counter_Int+11]

        Word_Str = MnemonicWordsList.BIP39[GroupOf11Bits_Str]

        if Counter_Int != len(NumberPlusChecksum_Str) - 11:

            StringContainingAllWords_Str += (Word_Str + " ")

        else:

            StringContainingAllWords_Str += Word_Str

        Counter_Int += 11

    return StringContainingAllWords_Str

def GeneratingMnemonicWordsSeed(StringContainingAllWords_Str):

    #######################

    #I Inserted those constant variables to that if one day the BIP39 standard may change, the developers
    #Can change the value of those variables, instead of directly writing the value in the function

    ALGORITHM_USED_STR = "sha512"

    ITERATION_COUNT_INT = 2048

    ENCODING_USED_STR = "utf-8"

    #######################

    SaltPassword_Str = str(input("Insert a password for the SALT: "))

    SALT_STR = "mnemonic" + SaltPassword_Str

    MasterSeed_Str = hashlib.pbkdf2_hmac(ALGORITHM_USED_STR, StringContainingAllWords_Str.encode(ENCODING_USED_STR), SALT_STR.encode(ENCODING_USED_STR), ITERATION_COUNT_INT).hex()

import secrets
import hashlib
import MnemonicWordsList

def GeneratingNumberWithEntropy(EntropyChosenByTheUser_Int):

    NumberWithEntropyChosen_Int = secrets.randbits(EntropyChosenByTheUser_Int)

    return NumberWithEntropyChosen_Int

def CalculatingTheChecksum(NumberWithEntropyChosenInBitRepresentation_Str, EntropyChosenByTheUser_Int):

    #Explaining the following line of code:
    #hashlib.sha256() wants a byte variable as an argument, so inside it I included
    #(NumberWithEntropyChosenInBitRepresentation_Str.encode()) to make the variabile in byte format
    #Then i took the digest, from the sha256 hash object returned, and because digest() returns a byte variable
    #I converted it in a hex string format with hex()
    HashInHexFormat_Str = hashlib.sha256((NumberWithEntropyChosenInBitRepresentation_Str.encode())).digest().hex()

    #Explaining the following line of code:
    #Inside the bin() function i convert the Hash in the Hexadecimal format, into its int representation
    #Then it is transformed into his binary representation
    #The [2:] is used to remove the initial '0b' string infront of our binary representation
    #Then the zfill(256) adds a padding to the resulting Hash, so that if it starts with less zeroes (Ex: 001111011111)
    #It will be shown as a number with exactly 256 bits (The SHA256 output) and wont invalidate the ENT/32
    HashInBinFormat_Str = bin(int(HashInHexFormat_Str, 16))[2:].zfill(256)

    #According to the BIP39 standard, the checksum is the first (Entropy/32) bits from the number's resulting hash
    BitsToTakeFromTheCheckum_Int = EntropyChosenByTheUser_Int  // 32

    Checksum_Str = HashInBinFormat_Str[:BitsToTakeFromTheCheckum_Int].zfill(BitsToTakeFromTheCheckum_Int)

    return Checksum_Str

def GeneratingMnemonicWords(NumberPlusChecksum_Str):

    Word_Str = " "

    Counter_Int = 0

    StringContainingAllWords_Str = ""

    while Counter_Int + 11 <= len(NumberPlusChecksum_Str):

        GroupOf11Bits_Str = NumberPlusChecksum_Str[Counter_Int:Counter_Int+11]

        Word_Str = MnemonicWordsList.BIP39[GroupOf11Bits_Str]

        if Counter_Int != len(NumberPlusChecksum_Str) - 11:

            StringContainingAllWords_Str += (Word_Str + " ")

        else:

            StringContainingAllWords_Str += Word_Str

        Counter_Int += 11

    return StringContainingAllWords_Str

def GeneratingMnemonicWordsSeed(StringContainingAllWords_Str):

    #######################

    #I Inserted those constant variables to that if one day the BIP39 standard may change, the developers
    #Can change the value of those variables, instead of directly writing the value in the function

    ALGORITHM_USED_STR = "sha512"

    ITERATION_COUNT_INT = 2048

    ENCODING_USED_STR = "utf-8"

    #######################

    SaltPassword_Str = str(input("Insert a password for the SALT: "))

    SALT_STR = "mnemonic" + SaltPassword_Str

    MasterSeed_Str = hashlib.pbkdf2_hmac(ALGORITHM_USED_STR, StringContainingAllWords_Str.encode(ENCODING_USED_STR), SALT_STR.encode(ENCODING_USED_STR), ITERATION_COUNT_INT).hex()

    return MasterSeed_Str, SaltPassword_Str