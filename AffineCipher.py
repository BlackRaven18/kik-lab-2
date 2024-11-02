from NGramUtils import NGramUtils
from scipy.stats import chi2


class AffineCipher:

    # Liczby wzglednie pierwsze z 26
    possible_a_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

    def __init__(self):
        self.alfabet_length = 26
        self.degrees_of_freedom = 26 - 1

    def encrypt(self, text, a, b):
        result = ""
        for char in text:
            result += chr((a * (ord(char) - 65) + b) % 26 + 65)

        return result

    def decrypt(self, text, a, b):
        result = ""
        rev_a = self.mod_inverse(a, 26)
        for char in text:
                result += chr((rev_a * (ord(char) - 65 - b) + 26) % 26 + 65)

        return result

    def brute_force_attack(self, ciphertext):
        nGramUtils = NGramUtils()
        critical_value = chi2.ppf(0.95, self.degrees_of_freedom)
        print("Wartość krytyczna: " + str(critical_value) + "\n")

        scores = []
        best_score_index = 0

        reference_ngrams = nGramUtils.read_ngrams_from_file("eng-n-grams/" + "english_monograms.txt")
        reference_ngrams_probability = nGramUtils.calculate_ngrams_probability(
             reference_ngrams
        )
        for a in self.possible_a_values:
            for b in range(1, 26):
                plaintext = self.decrypt(ciphertext, a, b)

                ngrams = nGramUtils.generate_ngrams_occurrence(plaintext, 1)

                score = nGramUtils.calculate_hi_test(ngrams, reference_ngrams_probability)

                if(score < critical_value):
                    print("Znaleziono możliwy tekst angielski: ")
                    print(plaintext + " dla klucza " + str(a) + " " + str(b) + " i wartości testu hi kwadrat: " + str(score) + "\n")
                    scores.append({
                        "plain_text": plaintext,
                        "hi_test": score,
                        "a": str(a),
                        "b": str(b),
                    })
     

        for i in range(len(scores)):
            if scores[i]["hi_test"] < scores[best_score_index]["hi_test"]:
                best_score_index = i
        
        print("Wyniki ataku bruteforce")
        print(scores[best_score_index]["plain_text"] + " dla klucza a = " + scores[best_score_index]["a"] + " b = " + scores[best_score_index]["b"])

        return scores[best_score_index]["plain_text"]

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