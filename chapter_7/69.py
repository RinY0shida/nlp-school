from gensim.models import KeyedVectors
import pycountry
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

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

    # k_means = KMeans(n_clusters = 5, random_state = 0)
    # labels = k_means.fit_predict(countries_vector)
    hierarchy_cluster = linkage(countries_vector, method = "ward")
    # print(hierarchy_cluster)

    plt.figure(figsize=(24, 8))
    dendrogram(hierarchy_cluster, labels = countries_name)
    plt.savefig("result/graph68.png", dpi = 400)
    plt.show()
    
if __name__ == "__main__":
    main()
