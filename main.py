import sys
import csv

csv_file = sys.argv[1]
input_word = sys.argv[2]

total_list = []
word_dict = {}
word_dict2 = {}
with open(csv_file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        word, f = row
        word_dict[word.lower()] = int(f.strip())

sorted_keys = sorted(word_dict.keys())
for i in sorted_keys:
    word_dict2[i] = word_dict[i]
word_dict2 = sorted(word_dict2.items(),key=lambda x: x[1], reverse=True)
word_dict = {}
for element in word_dict2:
    word_dict[element[0]] = element[1]

temp_dict = {}
if input_word.lower() in word_dict.keys():
    print(input_word)

elif input_word not in word_dict.keys():
    for i in range(len(input_word)):
        for word in word_dict.keys():
            if word[:-i] == input_word[:-i]:
                break
    res = list(word_dict.keys()).index(word)
    for i in list(word_dict.keys())[res:res+5]:
        print(i)
