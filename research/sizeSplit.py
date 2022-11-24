# Handling splitting an unsigned monero transaction into multiple monerosigner frames
import qrcode
FILENAME = "transaction/unsigned_monero_tx"

# The limit for qrcodes in binary form (In low error correcting mode)
#Eventually we need to subtract the auillary frame metadata from this to get the effective payload size
LIMITS = {}
#limit for 25x25
LIMITS["25"] = 32 #version 2
LIMITS["29"] = 53
LIMITS["33"] = 78
LIMITS["37"] = 106 #v5
LIMITS["53"] = 230 #v6
LIMITS["177"] = 2953 #v7


#function to break down number of frames needed
def calcNumFrames(_dataSize, _frameSize):
    return (_dataSize // _frameSize) + (1 if (( _dataSize % _frameSize) > 0)  else 0)


(1 if (True) > 0  else 0)
with open(FILENAME, mode='rb') as file:
    unsignedTX = file.read()


#the size of the transaction in bytes

sizeIN = len(unsignedTX)


FrameSize_25 = calcNumFrames(sizeIN, LIMITS["25"])
