from gensim.models import KeyedVectors

def main():
    negative300_path = "../resources/GoogleNews-vectors-negative300.bin"
    model = KeyedVectors.load_word2vec_format(negative300_path, binary = True)

if __name__ == "__main__":
    main()
