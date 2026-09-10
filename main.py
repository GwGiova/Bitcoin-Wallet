import BIP39
import BIP32

EntropyChosenByTheUser_Int = int(input("Insert the entropy you want to chose (128/256 bit): "))

while EntropyChosenByTheUser_Int != 128 and EntropyChosenByTheUser_Int != 256:

    EntropyChosenByTheUser_Int = int(input("Insert the entropy you want to chose (128/256 bit): "))

NumberWithEntropyChosen_Int =  BIP39.GeneratingNumberWithEntropy(EntropyChosenByTheUser_Int)

#I convert the number chosen to its binary representation thanks to 0:08b
#I added zfill at the end to ensure any initial "0" bits wont be removed in the number representation
#Ex: 00111011 ---> 111011 so with zfill the number is represented even with the initial 0s
NumberWithEntropyChosenInBitRepresentation_Str = '{0:08b}'.format(NumberWithEntropyChosen_Int).zfill(EntropyChosenByTheUser_Int)

Checksum_Str = BIP39.CalculatingTheChecksum(NumberWithEntropyChosenInBitRepresentation_Str, EntropyChosenByTheUser_Int)

NumberPlusChecksum_Str = NumberWithEntropyChosenInBitRepresentation_Str + Checksum_Str

StringContainingAllWords_Str = BIP39.GeneratingMnemonicWords(NumberPlusChecksum_Str)

MasterSeed_Str, Salt_Str = BIP39.GeneratingMnemonicWordsSeed(StringContainingAllWords_Str)

print(StringContainingAllWords_Str)

print(MasterSeed_Str)