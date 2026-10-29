# Bitcoin-Wallet

**This Bitcoin Wallet is currently unfinished**

This project works as a basic Bitcoin wallet engine.  
It implements the core standards used to generate mnemonic phrases, seeds, master keys and child keys.

---

## Requirements

These Python libraries are required:

- `secrets` — secure random number generation  
- `hashlib` — hashing functions (SHA256, SHA512, etc.)  
- `hmac` — HMAC implementation used in BIP32  

---

## Mnemonic Words List

The file **MnemonicWordsList.py** contains all the 2048 English BIP39 words.  
This allows fully offline mnemonic generation, avoiding online wordlists and reducing risks such as MitM attacks.

---

## Implemented Standards

I implemented the **BIP39** standard and partially the **BIP32** standard, following the official documentation:

- [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)  
- [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)

---

## Roadmap

- [x] BIP39  
- [ ] BIP32  
- [ ] BIP44  
- [ ] Address formats (Base58, Taproot (BIP86), etc.)  
- [ ] Transactions  
- [ ] GUI  
- [ ] More coming soon...

---

## Structure

- **main.py**  
  Entry‑point file. It manages all interactions and calls the functions from the other modules.

- **BIP39.py / BIP32.py**  
  These files contain all the functions related to their standards (entropy, checksum, seed, master keys, child keys, etc.).

- **MnemonicWordsList.py**  
  Contains the 2048 BIP39 words stored in a dictionary.  
  Each 11‑bit binary number (0–2047) maps to a specific word.

- **OPCODES.py**
  Contains two dictionaries used to convert Bitcoin Script opcodes between their string representations and their hexadecimal values:
  OPCODE_BYTES: maps opcode names (e.g., "OP_PUSHDATA1") to their corresponding hexadecimal values (e.g., 0x4c).
  BYTES_OPCODE: maps hexadecimal opcode values (e.g., 0x4c) back to their corresponding opcode names (e.g., "OP_PUSHDATA1").
  These dictionaries allow conversion in both directions between opcode names and their byte values.
---

## Usage

All interactions with the wallet are done through **main.py**.  
Just run that file and it will automatically call the required functions from the other modules.

---

## Disclaimer

**This wallet is not recommended for financial use.**  
It is not developed or maintained by a professional security team and may not meet all the required safety standards.
