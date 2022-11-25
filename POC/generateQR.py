import qrcode
import base64
import json

qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# qr.add_data('Some data')
# qr.make(fit=True)
testData = b"1" * 1000


data = testData
# data = str.encode(data)
# data = bytes(data, 'utf-8')
data = base64.b64encode(data).decode('ascii')


frame = {
"index" : 0,
"total" : 8,
"data" :  data
}

def dict_to_binary(the_dict):
    str = json.dumps(the_dict)
    binary = ' '.join(format(ord(letter), 'b') for letter in str)
    return binary


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)
    return d

# frame = dict_to_binary(frame)


img = qrcode.make(frame)

# img = qr.make_image(fill_color="black", back_color="white")
img.save("test.png")


testFrame = {
"index" : 10,
"total" : 12,
"data" :  1
}

json.dumps(testFrame) #lenght of the frame is 37
