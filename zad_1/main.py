import argparse
from NGramUtils import NGramUtils
from FileUtils import FileUtils
from CesarCipher import CesarCipher

path_to_reference_ngrams_directory = "eng-n-grams/"
reference_ngrams_files = ["english_monograms.txt", "english_bigrams.txt", "english_trigrams.txt", "english_quadgrams.txt"]
excluded_ngrams = ["J", "K", "Q", "X", "Z"]

def parse_args():
    parser = argparse.ArgumentParser(
        description="Parametry programu"
    )
    parser.add_argument("-e", action="store_true", help="Tryb szyfrowania")
    parser.add_argument("-d", action="store_true", help="Tryb deszyfrowania")
    parser.add_argument("-k", help="Klucz")
    parser.add_argument("-i", help="Tekst jawny")
    parser.add_argument("-o", help="Tekst zaszyfrowany")
    parser.add_argument("-g", type=int, help="Liczenie n-gramow")
    parser.add_argument('file', nargs='?', help="Destination file [Optional]")
    parser.add_argument('-r', type=int, help="Odczyt referencyjnej bazy X-gramow")
    parser.add_argument('-s', action="store_true", help="Test hi kwadrat")

    args = parser.parse_args()

    return args

def main():
    args = parse_args()
    nGramUtils = NGramUtils()

    if args.e or args.d:
        key_as_string = FileUtils.read_file(args.k)
        key = int(key_as_string)
        input_text = FileUtils.read_file(args.i, True)
        output_text = ""

        cesarCipher = CesarCipher()

        if args.e:
            output_text = cesarCipher.encrypt(input_text, key)

        if args.d:
            output_text = cesarCipher.decrypt(input_text, key)

        FileUtils.write_file(args.o, output_text)
        
        return
    
    if args.g and args.g > 0:

        ngrams = nGramUtils.generate_ngrams_occurrence(FileUtils.read_file(args.i, True), args.g)
        nGramUtils.save_ngrams_to_file(ngrams, args.file)

        return
        

    if args.r:

        ngrams = nGramUtils.generate_ngrams_occurrence(FileUtils.read_file(args.i, True), args.r)

        if args.s is False:
            nGramUtils.calculate_ngrams_probability(ngrams, args.file)

        else:
            reference_ngrams = nGramUtils.read_ngrams_from_file(path_to_reference_ngrams_directory + reference_ngrams_files[args.r - 1])
            reference_ngrams_probability = nGramUtils.calculate_ngrams_probability(
                reference_ngrams
            )

            nGramUtils.calculate_hi_test(ngrams, reference_ngrams_probability, excluded_ngrams)

if __name__ == "__main__":
    main()
