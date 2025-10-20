from gensim.models import KeyedVectors
import pycountry
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

def main():
    # pathを通す
    negative300_path = "../resources/GoogleNews-vectors-negative300.bin"
    negative300_model = KeyedVectors.load_word2vec_format(negative300_path, binary = True)

    # pycountryを使うのが初めてなので、とりあえず使ってみる
    countries_name = []
    countries_vector = []
    for country in pycountry.countries:
        # TODO(RinYoshida): なんかモデルに'a'が無い？って言われたから無理やりモデルが存在してるvectorだけ抽出したった。
        if country.name in negative300_model.key_to_index:
            countries_name.append(country.name)
            countries_vector.append(negative300_model[country.name])
            # print(countries_vector)

    countries_vector = np.array(countries_vector)
    t_sne = TSNE(n_components = 3, random_state = 0)
    reduced = t_sne.fit_transform(countries_vector)

    plt.figure(figsize=(10, 8))
    
    for i, country_name in enumerate(countries_name):
        plt.scatter(reduced[i, 0], reduced[i, 1])
        plt.text(reduced[i, 0] + 0.1, reduced[i, 1] + 0.1, country_name)
    plt.savefig("result/graph69.png", dpi = 400)
    plt.show()
    
if __name__ == "__main__":
    main()
