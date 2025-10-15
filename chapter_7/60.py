from gensim.models import KeyedVectors

def main():
    # pathを通す
    negative300_path = "../resources/GoogleNews-vectors-negative300.bin"
    negative300_model = KeyedVectors.load_word2vec_format(negative300_path, binary = True)

    vector = negative300_model["United_States"]

    print("United_States Vector\n")
    print(vector)

if __name__ == "__main__":
    main()
