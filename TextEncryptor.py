class TextEncryptor:

    def convert_key_to_dict(self, key):

        mapped_key = {}
        for line in key.splitlines():
            if line.strip():
                key, wartosc = line.split()
                mapped_key[key] = wartosc
        return mapped_key

    def encrypt(self, text, key) -> str:

        encrypted_text = ""

        for char in text:
            if char in key:
                encrypted_text += key[char]
            else:
                raise Exception("Nie znaleziono klucza dla znaku: " + char)

        return encrypted_text
    
    def decrypt(self, text, key) -> str:

        decrypted_text = ""
        reversed_key = {v: k for k, v in key.items()}

        for char in text:
            if char in reversed_key:
                decrypted_text += key[char]
            else:
                raise Exception("Nie znaleziono klucza dla znaku: " + char)

        return decrypted_text
    
    
