#1. Feladat) kódolás, rejtjelezés

def encrypt(message, key):
    # Karakterek kódolása
    def char_to_code(char):
        if char == ' ':
            return 26
        else:
            return ord(char) - ord('a')

    # Kód visszaalakítása karakterré
    def code_to_char(code):
        if code == 26:
            return ' '
        else:
            return chr(code + ord('a'))

    encrypted_message = []

    for m, k in zip(message, key):
        m_code = char_to_code(m)
        k_code = char_to_code(k)
        encrypted_code = (m_code + k_code) % 27
        encrypted_message.append(code_to_char(encrypted_code))

    return ''.join(encrypted_message)

#dekódolás

def decrypt(encrypted_message, key):
    # Karakterek kódolása
    def char_to_code(char):
        if char == ' ':
            return 26
        else:
            return ord(char) - ord('a')

    # Kód visszaalakítása karakterré
    def code_to_char(code):
        if code == 26:
            return ' '
        else:
            return chr(code + ord('a'))

    decrypted_message = []

    for c, k in zip(encrypted_message, key):
        c_code = char_to_code(c)
        k_code = char_to_code(k)
        decrypted_code = (c_code - k_code) % 27
        decrypted_message.append(code_to_char(decrypted_code))

    return ''.join(decrypted_message)

# Tesztelés
message = "helloworld"
key = "abcdefgijkl"

# Rejtjelezés és visszafejtés
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Eredeti üzenet:", message)
print("Kulcs:", key)
print("Rejtjelezett üzenet:", encrypted_message)
print("Visszafejtett üzenet:", decrypted_message)
#2.feladat

#szólista betöltése
def load_wordlist(filename):
    with open(filename, 'r') as file:
        words = set(word.strip() for word in file.readlines())
    return words

#közös kulcs feltárása
def find_common_key(encrypted1, encrypted2, wordlist):
    # Karakterek kódolása
    def char_to_code(char):
        if char == ' ':
            return 26
        return ord(char) - ord('a')

    # Kód visszaalakítása karakterré
    def code_to_char(code):
        if code == 26:
            return ' '
        return chr(code + ord('a'))

    def decrypt_char(c1, c2):
        c1_code = char_to_code(c1)
        c2_code = char_to_code(c2)
        return (c1_code - c2_code) % 27

    # Kitalálja a kulcsot az első szó alapján
    def guess_key_for_word(start, word, enc1, enc2):
        key = []
        for i, char in enumerate(word):
            key_code = decrypt_char(enc1[start + i], char)
            key.append(code_to_char(key_code))
        return ''.join(key)

    # Megpróbálja megfejteni az üzenetet egy adott kulcs részlettel
    def attempt_decrypt_with_key_part(key_part, encrypted):
        message = []
        for i, enc_char in enumerate(encrypted):
            if i < len(key_part):
                k_code = char_to_code(key_part[i])
            else:
                k_code = 0  # ha a kulcs rövidebb, a fennmaradó része nulla lesz
            e_code = char_to_code(enc_char)
            decrypted_code = (e_code - k_code) % 27
            message.append(code_to_char(decrypted_code))
        return ''.join(message)

    possible_keys = []

    # Próbálja megtalálni a kulcsot minden szó esetén
    for i in range(len(encrypted1)):
        for word in wordlist:
            if i + len(word) <= len(encrypted1):
                key_part = guess_key_for_word(i, word, encrypted1, encrypted2)
                decrypted1 = attempt_decrypt_with_key_part(key_part, encrypted1)
                decrypted2 = attempt_decrypt_with_key_part(key_part, encrypted2)

                # Ellenőrzi, hogy az eredmények értelmesek-e
                if all(word in wordlist for word in decrypted1.split()) and all(
                        word in wordlist for word in decrypted2.split()):
                    possible_keys.append(key_part)

    return possible_keys













