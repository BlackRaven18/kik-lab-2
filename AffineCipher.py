
class AffineCipher:

    def encrypt(self, text, a, b):
        result = ""
        for char in text:
            result += chr((a * (ord(char) - 65) + b) % 26 + 65)

        return result

    def decrypt(self, text, a, b):
        result = ""
        rev_a = self.mod_inverse(a, 26)
        print(rev_a)
        for char in text:
                result += chr((rev_a * (ord(char) - 65 - b) + 26) % 26 + 65)

        return result

    def brute_force_attack(self, ciphertext):
        pass

    def get_key_from_string(self, key_as_string):
        key = key_as_string.split(" ")
        key = [int(k) for k in key]
        return key
    
    # Extended Euclidean algorithm
    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    # Modular multiplicative inverse
    def mod_inverse(self, a, m):
        gcd, x, _ = self.extended_gcd(a, m)
        if gcd != 1:
            raise ValueError("Odwrotność modulo nie istnieje")
        else:
            return x % m