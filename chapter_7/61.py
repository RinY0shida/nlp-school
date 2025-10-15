from gensim.models import KeyedVectors

def main():
    # pathを通す
    negative300_path = "../resources/GoogleNews-vectors-negative300.bin"
    negative300_model = KeyedVectors.load_word2vec_format(negative300_path, binary = True)

    # ベクトルから自分で導出できるけど、素晴らAPIがあるのでエコシステムに乗っからせてもらう
    united_states_vector = negative300_model["United_States"]
    us_vector = negative300_model["U.S"]

    

    cosine_similarity_us_united_states = negative300_model.similarity("U.S", "United_States")
    print("consine similarity =", cosine_similarity_us_united_states)

if __name__ == "__main__":
    main()
