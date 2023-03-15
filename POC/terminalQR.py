# Sample file to print out QR code to terminal 
import io
import qrcode
qr = qrcode.QRCode()
qr.add_data("Some text")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())


# Binary doesn't work with ascii encoding

# qr = qrcode.QRCode()
# qr.add_data(b"Some text")
# f = io.BytesIO()
# qr.print_ascii(out=f)
# f.seek(0)
# print(f.read())
