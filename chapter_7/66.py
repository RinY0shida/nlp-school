from gensim.models import KeyedVectors
import pandas as pd
from scipy.stats import spearmanr

def main():
    # pathを通す
    negative300_path = "../resources/GoogleNews-vectors-negative300.bin"
    negative300_model = KeyedVectors.load_word2vec_format(negative300_path, binary = True)

    human_score = []
    model_score = []

    conbined_path = "../resources/wordsim353/combined.csv"
    combined_file = pd.read_csv(conbined_path)

    # 各行を順に処理
    for _, row in combined_file.iterrows():
        word_1 = row["Word 1"]
        word_2 = row["Word 2"]
        human_similarity = row["Human (mean)"]

        if word_1 in negative300_model and word_2 in negative300_model:
            model_similarity = negative300_model.similarity(word_1, word_2)
            human_score.append(float(human_similarity))
            model_score.append(model_similarity)
            # print(model_similarity)

    # スピアマン相関係数を導出する。人間のスコアとモデルのスコアの比較
    correlation_coefficient, p_value = spearmanr(human_score, model_score)
    print(f"correlation coefficient: {correlation_coefficient}")
    print(f"p_value: {p_value}")
    
if __name__ == "__main__":
    main()
