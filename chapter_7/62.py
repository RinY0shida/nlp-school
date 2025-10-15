from gensim.models import KeyedVectors

def main():
    # pathを通す
    negative300_path = "../resources/GoogleNews-vectors-negative300.bin"
    negative300_model = KeyedVectors.load_word2vec_format(negative300_path, binary = True)
    
    similar_words_united_states = negative300_model.most_similar("United_States", topn = 10)
    
    print("top10 wards =")
    
    for word, score in similar_words_united_states:
        print(f"{word}: {score}")
    
if __name__ == "__main__":
    main()
