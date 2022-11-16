from monero.seed import Seed
# import the keccak-256
from Crypto.Hash import keccak
#can follow along with https://xmr.llcoins.net/

b = 256
q = 2**255 - 19
l = 2**252 + 27742317777372353535851937790883648493


def reverse_byte_order(hex):
    if(len(hex)%2==1): hex = '0' + hex
    return "".join(reversed([hex[i:i+2] for i in range(0, len(hex), 2)]))


def sc_reduce32(key):
    return reverse_byte_order("%x" % int((int(reverse_byte_order(key), 16) % l)))


def cn_fast_hash(hex):
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(bytearray.fromhex(hex))
    return keccak_hash.hexdigest()

#1026 875 ridges
p = Seed("owls moat ridges weird obedient itself orbit grunt nagged eldest piloted update twice hunter apart dwarf pumpkins ramped gags dyslexic dolphin happens swiftly trying dyslexic")

hex = p.hex




#
# keccak_hash = keccak.new(digest_bits=256)
#
# keccak_hash.update(b'2ff2c92ed5751ad617fb46343db20b40e2ecb2a8d9c0610329ab05fbd245d60c')
#
# privateSpendKey = keccak_hash.hexdigest()
# print(privateSpendKey)
#
# from binascii import unhexlify
#
# a = int.from_bytes(unhexlify(privateSpendKey), "little")
# b = hexlify(a.to_bytes(32, "little")).decode("latin-1")


hexadecimal_seed = '2ff2c92ed5751ad617fb46343db20b40e2ecb2a8d9c0610329ab05fbd245d60c'
hash_of_seed = cn_fast_hash(hexadecimal_seed)
private_spend_key = sc_reduce32(hash_of_seed) #this one is correct, should be private view key
private_view_key = sc_reduce32(cn_fast_hash(hash_of_seed)) #comes out wrong





#21687669386742833111537372263911639637679491191883450262969211767899742918156
# example bitcoin seed digit stream :
# 192402220235174306311124037817700641198012901210
