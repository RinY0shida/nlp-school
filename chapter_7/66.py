from gensim.models import KeyedVectors

def main():
    # pathを通す
    negative300_path = "../resources/GoogleNews-vectors-negative300.bin"
    negative300_model = KeyedVectors.load_word2vec_format(negative300_path, binary = True)

    questions_words_path = "../resources/questions-words.txt"

    # questions-wordsの特定の変数だけ抜き出すのは今後のことを考えるとベターじゃない気がするので、全部一気に読み込ませる

    # TODO(RinYoshida): 関数用意させたほうがいいよね
    questions_words = []
    txt_file = open(questions_words_path, "r", encoding="utf-8")
    for line in txt_file:
        line = line.strip()
        if line.startswith(":"):
            category = line[2:]
            continue
        words = line.strip().split()
        if words:
            words.insert(0, category)
            questions_words.append(words)

    txt_file.close()

    txt_file = open("result/ans64.txt", "w", encoding = "utf-8")
    for i in range(len(questions_words)):
        composite_vector = negative300_model[questions_words[i][3]] - negative300_model[questions_words[i][2]] + negative300_model[questions_words[i][4]]
        similar_result = negative300_model.most_similar(composite_vector, topn = 1)
        similar_word, similarity = similar_result[0]
        txt_file.write(questions_words[i][0]
                       + " "
                       + questions_words[i][1]
                       + " "
                       + questions_words[i][2]
                       + " "
                       + questions_words[i][3]
                       + " "
                       + questions_words[i][4]
                       + " "
                       + similar_word
                       + " "
                       + str(similarity)
                       + "\n"
                       )
        print(i)

        
#    composite_vector = negative300_model[questions_words[2]] - negative300_model[questions_words[1]] + negative300_model[questions_words[3]]
    
#    similar_words_united_states = negative300_model.most_similar(composite_vector, topn = 1)
    
    
if __name__ == "__main__":
    main()
