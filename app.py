letters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*/ "
letters_map = letters*2
key = "supermario"
message = input("enter the message you want to encrypt: ")
while len(key) < len(message):
    key += key


def encrypt(message, key):
    enc_message = ""
    for key_index, char in enumerate(message):
        if char in letters:
            index = letters.find(char)
            password_index = letters.find(key[key_index])
            enc_message += letters_map[index+password_index]
    return enc_message


def decrypt(message, key):
    enc_message = ""
    for key_index, char in enumerate(message):
        if char in letters:
            index = letters.find(char)
            password_index = letters.find(key[key_index])
            enc_message += letters_map[index-password_index]
    return enc_message


enc_text = encrypt(message, key)


dec_text = decrypt(enc_text, key)

print(enc_text)
print(dec_text)
