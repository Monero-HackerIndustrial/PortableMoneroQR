import qrcode
qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
# qr.add_data('Some data')
# qr.make(fit=True)
testData = "1" * 12184
img = qrcode.make(testData)

# img = qr.make_image(fill_color="black", back_color="white")
img.save("test.png")
