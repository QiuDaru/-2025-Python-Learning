# a = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# print(a)
def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper(): 
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():  
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else: 
            encrypted_text += char

    return encrypted_text


text = "az "
shift = 3
encrypted = caesar_cipher(text, shift)
print("加密後的字串:", encrypted)
