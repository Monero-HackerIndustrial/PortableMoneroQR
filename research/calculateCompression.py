import zlib
import base64

FILENAME = "transaction/unsigned_monero_tx"

(1 if (True) > 0  else 0)
with open(FILENAME, mode='rb') as file:
    unsignedTX = file.read()


unsignedB64 = base64.b64encode(unsignedTX).decode('ascii')
compressedB64 = zlib.compress(unsignedB64.encode())

compressedTX = zlib.compress(unsignedTX)
# print(zlib.decompress(a).decode())

print(f"size of the tx {len(unsignedTX)}")

print(f"compressed size of the tx {len(compressedTX)}")


print(f"uncompressed base64 {len(unsignedB64)}")
print(f"compressed base64 {len(compressedTX)}")

print(type(compressedTX))
print(f"{compressedTX}")

# a = "this string needs compressing"
# a = zlib.compress(a.encode())
# print(zlib.decompress(a).decode())  # outputs original contents of a




# sys.getsizeof(obj)
