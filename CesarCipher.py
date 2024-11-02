from NGramUtils import NGramUtils
from scipy.stats import chi2

class CesarCipher:

    def encrypt(self, text, key) -> str:
        encrypted_text = ""
        for char in text:
            encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
        return encrypted_text

    def decrypt(self, text, key) -> str:
        decrypted_text = ""
        for char in text:
            decrypted_text += chr((ord(char) - key - 65) % 26 + 65)

        return decrypted_text
    
    def brute_force_attack(self, ciphertext):
        
        nGramUtils = NGramUtils()
        scores = []
        plain_text_array = []
        best_score_index = 0

        reference_ngrams = nGramUtils.read_ngrams_from_file("eng-n-grams/" + "english_monograms.txt")
        reference_ngrams_probability = nGramUtils.calculate_ngrams_probability(
             reference_ngrams
        )
        for key in range(1, 26):
            plaintext = self.decrypt(ciphertext, key)
            plain_text_array.append(plaintext)

            ngrams = nGramUtils.generate_ngrams_occurrence(plaintext, 1)

            score = nGramUtils.calculate_hi_test(ngrams, reference_ngrams_probability)
            scores.append(score)
     

        for i in range(len(scores)):
            if scores[i] < scores[best_score_index]:
                best_score_index = i
        
        print("Wyniki ataku bruteforce")
        print(plain_text_array[best_score_index] + " dla klucza " + str(best_score_index + 1))

        return plain_text_array[best_score_index]
    
    def get_key_from_string(self, key_as_string):
        return int(key_as_string)
