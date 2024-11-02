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
        best_score_index = 0

        reference_ngrams = nGramUtils.read_ngrams_from_file("eng-n-grams/" + "english_monograms.txt")
        reference_ngrams_probability = nGramUtils.calculate_ngrams_probability(
             reference_ngrams
        )
        for key in range(1, 26):
            plaintext = self.decrypt(ciphertext, key)

            ngrams = nGramUtils.generate_ngrams_occurrence(plaintext, 1)

            score = nGramUtils.calculate_hi_test(ngrams, reference_ngrams_probability)
            scores.append({
                "plain_text": plaintext,
                "hi_test": score,
                "key": str(key)
            })
     

        for i in range(len(scores)):
            if scores[i]["hi_test"] < scores[best_score_index]["hi_test"]:
                best_score_index = i
        
        print("Wyniki ataku bruteforce")
        print(scores[best_score_index]["plain_text"] + " dla klucza " + scores[best_score_index]["key"])

        return scores[best_score_index]["plain_text"]
    
    def get_key_from_string(self, key_as_string):
        return int(key_as_string)
