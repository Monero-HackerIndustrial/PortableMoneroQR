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


There is a variable named "words". These array of words is what the monero software uses internally to generate seed phrases.


### Creating a offline wordlist dictionary

The seed phrase is an encoded
