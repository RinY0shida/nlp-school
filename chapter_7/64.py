from gensim.models import KeyedVectors

def main():
    # pathを通す
    negative300_path = "../resources/GoogleNews-vectors-negative300.bin"
    negative300_model = KeyedVectors.load_word2vec_format(negative300_path, binary = True)

    spain_vector = negative300_model["spain"]
    madrid_vector = negative300_model["madrid"]
    athens_vector = negative300_model["athens"]

    composite_vector = spain_vector - madrid_vector + athens_vector
    
    similar_words_united_states = negative300_model.most_similar(composite_vector, topn = 10)
    
    print("top10 wards =")
    for word, score in similar_words_united_states:
        print(f"{word}: {score}")
    
if __name__ == "__main__":
    main()
