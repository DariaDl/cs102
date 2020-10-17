

import typing as tp

def encrypt_caesar(plaintext: str, shift: int) -> str:
    ciphertext = ''
    for ch in plaintext:
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
            code = ord(ch) + 3
            if code > ord('Z') and code < ord('a') or code > ord('z'):
                code -= 26
            ciphertext += chr(code)
        else:
            ciphertext += ch
    return ciphertext



def decrypt_caesar(ciphertext: str, shift: int) -> str:
    plaintext = ''

    for ch in ciphertext:

        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':

            code = ord(ch) - 3

            if code < ord('a') and code > ord('Z') or code < ord('A'):

                code += 26

            plaintext += chr(code)

        else:

            plaintext += ch

    return plaintext



d = {"python", "java", "ruby"}
def caesar_breaker(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    text = list(ciphertext.lower())
    for element in dictionary:
        element = list(element)
        sub1 = ord(text[0]) - ord(element[0])
        sub2 = ord(text[1]) - ord(element[1])
        if sub1 < 0:
            sub1 += 26
        if sub2 < 0:
            sub2 += 26
        if sub1 == sub2:
            best_shift = sub1
    return best_shift