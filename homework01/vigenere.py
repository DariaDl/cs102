def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    for i, letter in enumerate(plaintext):
        key_let = keyword[i % len(keyword)]
        if "A" <= key_let <= "Z":
            shift = ord(key_let) - ord('A')
        else:
            shift = ord(key_let) - ord('a')

        if "A" <= letter <= "Z":
            ciphertext += chr(ord("A") + (ord(letter) - ord("A") + shift) % 26)
        else:
            ciphertext += chr(ord("a") + (ord(letter) - ord("a") + shift) % 26)

    return ciphertext

print(encrypt_vigenere("introduction to python", "lsci"))
def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
     plaintext = ""
     for i, letter in enumerate(ciphertext):
        key_let = keyword[i % len(keyword)]
        if 'A' <= key_let <= 'Z':
            shift = ord(key_let) - ord('A')
        else:
            shift = ord(key_let) - ord('a')

        if 'A' <= letter <= 'Z':
            plaintext += chr(ord('A') + (26 + ord(letter) - ord('A') - shift) % 26)
        else:
            plaintext += chr(ord("a") + (26 + ord(letter) - ord("a") - shift) % 26)

     return plaintext


