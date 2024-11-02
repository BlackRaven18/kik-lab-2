import argparse
from NGramUtils import NGramUtils
from FileUtils import FileUtils
from CesarCipher import CesarCipher
from AffineCipher import AffineCipher

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
    parser.add_argument('-a', help="Perform brute force attack on Cesar cipher")
    parser.add_argument('-cesar', action="store_true", help="Use Cesar cipher")
    parser.add_argument('-affine', action="store_true", help="Use Affine cipher")

    args = parser.parse_args()

    return args

def main():
    args = parse_args()
    cesarCipher = CesarCipher()
    affineCipher = AffineCipher()


    if args.e or args.d:
        key_as_string = FileUtils.read_file(args.k)
        input_text = FileUtils.read_file(args.i, True)
        output_text = ""

        if args.cesar:
            key = cesarCipher.get_key_from_string(key_as_string)
            
            if args.e:
                output_text = cesarCipher.encrypt(input_text, key)

            if args.d:
                output_text = cesarCipher.decrypt(input_text, key)
        elif args.affine:
            key = affineCipher.get_key_from_string(key_as_string)

            if args.e:
                output_text = affineCipher.encrypt(input_text, key[0], key[1])

            if args.d:
                output_text = affineCipher.decrypt(input_text, key[0], key[1])
        else:
            raise Exception("Nie wybrano szyfru")

        FileUtils.write_file(args.o, output_text)
        
        return
    
    if args.a and args.a == "bf":
        input_text = FileUtils.read_file(args.i, True)
        cesarCipher = CesarCipher()
        decrypted_text = cesarCipher.brute_force_attack(input_text)
        FileUtils.write_file(args.o, decrypted_text)


if __name__ == "__main__":
    main()
