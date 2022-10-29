# Seed Wordlist

Bitcoin has bip39 standard for seed phrases. Monero does not have an equivalent.
Trezor has Slip44 standard which uses a bip39 wordlist to generate multi coin wallets using a deviation path.

This readme standardizes the wordlist that is used for monero seeds in the monerosigner.
The same wordlist is used as the official monero wallet. Thsi document outlines what that list is and
how a user is able to recreate their own version of an offline printable and verifiable wordlist.

### What is a mnemonic seed ?
Monero Mnemonic words https://www.getmonero.org/resources/moneropedia/mnemonicseed.html

Mnemonic words are a standard way of encoding private crypto keys in an easy to backup format.
The official Monero wallet uses a 25 word seed mnemonic phrase. This phrase can be used to regenrate a private key and
associated wallets.

There is a word list with 1626 words in it (for the english one). Each one of those words has an index associated with it.

for example the first 5 words on the list along with their index (Index starts at 0)

```
0 = "abbey"
1 = "abducts"
2 = "ability"
3 = "ablaze"
4 = "abnormal"
```

These 5 words have an index

### Where are the word lists ?

Those words are defined in the the Monero Source codebase: https://github.com/monero-project/monero/tree/master/src/mnemonics

For example the english one is located at the following location :

Mnemonic wordlist location: https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h#L56

and also :
https://github.com/monero-ecosystem/monero-python/blob/master/monero/wordlists/english.py

The original implementaion for reference in helper functions:
https://github.com/monero-project/mininero/blob/master/mnemonic.py


There is a variable named "words". These array of words is what the monero software uses internally to generate seed phrases.


### Creating a offline wordlist dictionary

TODO: Add instructions for building an offline wordlist dictionary.




### MoneroSeedQR

25 word mnemonic seed phrase is:

```
25 words * 4 digits per word = 100 digits
```

This is the same as the Monero core wallet.

The 25 words correspond to a 256-bit interger which is the account's "private spend key".
The Private view key is derived by hashing the private spend key with Keccak-256.
The public keys are then derived from the private keys.
