from gensim.models import KeyedVectors
import pycountry
from sklearn.cluster import KMeans

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

    k_means = KMeans(n_clusters = 5, random_state = 0)
    labels = k_means.fit_predict(countries_vector)

    for i in range(5):
        print(f"cluster {i}:")
        for country_name, label in zip(countries_name, labels):
            if label ==i:
                print(country_name)
                
if __name__ == "__main__":
    main()
