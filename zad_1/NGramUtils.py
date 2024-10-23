
from collections import Counter
from FileUtils import FileUtils

class NGramUtils:

    def generate_ngrams_occurrence(self, text, n) -> Counter:
       ngrams = Counter()
       for i in range(len(text) - n + 1):
           ngrams[text[i : i + n]] += 1
       return ngrams
    
    def save_ngrams_to_file(self, ngrams, destination_filename):
       with open(FileUtils.default_files_directory + destination_filename, "w") as file:
           for ngram, count in ngrams.items():
               file.write(f"{ngram} {count}\n")

    def get_ngrams_number(self, ngrams) -> int:
        ngrams_number = 0
        for ngram, count in ngrams.items():
            ngrams_number += count
        return ngrams_number
    
    def read_ngrams_from_file(self, file) -> dict:
        ngrams_as_string = FileUtils.read_file(file)
        ngrams = {}
        for line in ngrams_as_string.splitlines():
            if line.strip():
                key, value = line.split()
                ngrams[key] = int(value)

        return ngrams

    def calculate_ngrams_probability(self, ngrams, destination_filename = "") -> dict:
        ngrams_probability = {}
        ngrams_number = self.get_ngrams_number(ngrams)

        for ngram, count in ngrams.items():
            probability = count / ngrams_number
            ngrams_probability[ngram] = probability
        
        ngrams_probability = ngrams_probability

        if destination_filename:
            with open(FileUtils.default_files_directory + destination_filename, "w") as file:
                    for ngram, probability in ngrams_probability.items():
                        file.write(f"{ngram} {probability}\n")

        return ngrams_probability

    def calculate_hi_test(self, ngrams, ngrams_probability, excluded_ngrams = []):
        hi= 0
        ngram_occurances = self.get_ngrams_number(ngrams)
        for ngram, count in ngrams.items():
            if ngram in excluded_ngrams:
                continue
            probability = ngrams_probability[ngram]
            Ci = ngrams[ngram]
            Ei = ngram_occurances * probability
            hi += (Ci - Ei)**2 / Ei

        print("Wyniki testu hi kwadrat: " + str(hi))

    