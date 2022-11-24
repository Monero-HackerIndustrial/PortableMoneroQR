# Handling splitting an unsigned monero transaction into multiple monerosigner frames
import qrcode
import base64
import json

FILENAME = "transaction/unsigned_monero_tx"
QRVERSION = 7
METADATA_SIZE = 37

# The limit for qrcodes in binary form (In low error correcting mode)
#Eventually we need to subtract the auillary frame metadata from this to get the effective payload size
QRLIMITS = {}
#limit for 25x25
QRLIMITS["2"] = 32 #version 2 25x25
QRLIMITS["3"] = 53 #version 3 29x 29
QRLIMITS["4"] = 78 #version 4 3x33
QRLIMITS["5"] = 106 #v5 37x37
QRLIMITS["6"] = 230 #v6 53x53
QRLIMITS["7"] = 2953 #v7  177x177


LIMIT = QRLIMITS[str(QRVERSION)] - METADATA_SIZE

#function to break down number of frames needed
def calcNumFrames(_dataSize, _frameSize):
    return (_dataSize // _frameSize) + (1 if (( _dataSize % _frameSize) > 0)  else 0)

def createFrame(_data, _frameSize):
    sizeIN = len(_data)
    framesNeeded = calcNumFrames(sizeIN, LIMIT)
    fullData = memoryview(_data).cast('c')
    for x in range(0,framesNeeded):
        start = x * _frameSize
        stop = start + _frameSize
        dataSlice = bytes(fullData[start:stop])
        dataSlice = base64.b64encode(dataSlice).decode('ascii')
        frame = {
        "index" : start,
        "total" : framesNeeded,
        "data" :  dataSlice
        }
        print(json.dumps(frame))


(1 if (True) > 0  else 0)
with open(FILENAME, mode='rb') as file:
    unsignedTX = file.read()


#the size of the transaction in bytes

sizeIN = len(unsignedTX)


framesNeeded = calcNumFrames(sizeIN, LIMIT)

print(f"The unsinged tx is {sizeIN} bytes long ")
print(f"Using QR version #{QRVERSION}")
print(f"Transfer requires {framesNeeded} frames")


createFrame(unsignedTX,LIMIT )
