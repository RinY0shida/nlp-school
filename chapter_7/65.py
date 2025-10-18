from gensim.models import KeyedVectors

def main():
    ans64_data = []
    ans64_path = "result/ans64.txt"
    ans64_file = open(ans64_path, "r", encoding = "utf-8")
    
    for line in ans64_file:
        line = line.strip()
        words = line.strip().split()
        if words:
            ans64_data.append(words)

    ans64_file.close()

    correct_answers_count = 0
    count = 0
    category = ans64_data[0][0]
    ans64_data_len = range(len(ans64_data))
    
    for i in ans64_data_len:
        if ans64_data[i][0] != category:
            accuracy = correct_answers_count / count
            print(f"{category} accuracy: {accuracy}")
            category = ans64_data[i][0]
            correct_answers_count = 0
            count = 0
        
        if ans64_data[i][3] == ans64_data[i][5]:
            correct_answers_count += 1

        count += 1
    
if __name__ == "__main__":
    main()
