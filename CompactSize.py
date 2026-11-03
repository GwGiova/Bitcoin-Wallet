#Compact Size is a way to represent a field whom value is variable, not constant.
#It's used in field like "input count" in a Bitcoin transaction.
#??Have to implement little endian??

def CompactCode(CompactSize_Bytes):

    if(CompactSize_Bytes <= 0xfc):

        return CompactSize_Bytes

    elif(CompactSize_Bytes == 0xfd):

        return 2

    elif(CompactSize_Bytes == 0xfe):

        return 4

    elif(CompactSize_Bytes == 0xff):

        return 8