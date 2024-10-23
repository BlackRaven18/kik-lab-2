class CesarCipher:

    def encrypt(self, text, key):
        encrypted_text = ""
        for char in text:
            encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = ""
        for char in text:
            decrypted_text += chr((ord(char) - key - 65) % 26 + 65)

        return decrypted_text
