from nltk.corpus import stopwords
from nltk.book import *
from sortedcontainers import SortedList
import re
import array
s=set(stopwords.words('english'))
BasePath = "F:\\HallmarksEngine\\Data\\SciGraph\\comp\\"
count = 0
all_words = SortedList()


print("Step 1: Searching Words in Raw Data...")
with open(BasePath + "CancerArticlesClean.dat") as f:
    for line in f:
        splitted = line.split('\t', 2)
        splitted[2] = re.sub("[0-9]", '', splitted[2])
        updated_line = splitted[2].replace("`", " ").replace("@", " ").replace("[", " ").replace("]", " ").replace(">", " ").replace("<", " ").replace("+", " ").replace("*", " ").replace("&", " ").replace("}", " ").replace("{", " ").replace("=", " ").replace("\\", " ").replace("%", " ").replace("^", " ").replace(";", " ").replace("$", " ").replace(":", " ").replace("/", " ").replace("(", " ").replace(")", " ").replace("#", " ").replace("\"", " ").replace(".", " ").replace(",", " ").replace("!", " ").replace("'", " ").replace("-", " ")
        words = filter(lambda w: not w in s,updated_line.split())
        for word in words:
            if len(word) > 4:
                if word.lower() not in all_words:
                    all_words.add(word.lower())
        count += 1
        if count % 20000 == 0:
            print(str(count) + " processed. found " + str(len(all_words)))

print("Step 2: Counting occurences of all words found in the previous step.")
counters = array.array('i',(0 for i in range(0,len(all_words))))
with open(BasePath + "CancerArticlesClean.dat") as f:
    for line in f:
        splitted = line.split('\t', 2)
        splitted[2] = re.sub("[0-9]", '', splitted[2])
        updated_line = splitted[2].replace("`", " ").replace("@", " ").replace("[", " ").replace("]", " ").replace(">", " ").replace("<", " ").replace("+", " ").replace("*", " ").replace("&", " ").replace("}", " ").replace("{", " ").replace("=", " ").replace("\\", " ").replace("%", " ").replace("^", " ").replace(";", " ").replace("$", " ").replace(":", " ").replace("/", " ").replace("(", " ").replace(")", " ").replace("#", " ").replace("\"", " ").replace(".", " ").replace(",", " ").replace("!", " ").replace("'", " ").replace("-", " ")
        words = filter(lambda w: not w in s,updated_line.split())
        for word in words:
            if len(word) > 4:
                ind = all_words.index(word.lower())
                counters[ind] = counters[ind] + 1

print("Step 3: Analyzing distribution of number of occurences.")
max = 5
for i in range(0,len(all_words)):
    if counters[i] > max:
        max = counters[i]
occ_dist = array.array('i',(0 for i in range(0,max+1)))
for i in range(0,len(all_words)):
    occ_dist[counters[i]] += 1
for i in range(0,max+1):
    if occ_dist[i] > 0:
        print(str(occ_dist[i]) + " words occured " + str(i) + " times.")

print("Step 4: Writing output files.")
with open(BasePath + "Words.dat", 'w') as f:
    for word in all_words:
        f.write(word + '\n')
with open(BasePath + "Occurences.dat", 'w') as f:
    f.write("Number of files\tNumber of Occurences"+ "\n")
    for i in range(0,max+1):
        if occ_dist[i] > 0:
            f.write(str(occ_dist[i]) + "\t" + str(i)+ "\n")

with open(BasePath + "AboveThreshold.dat", 'w') as f:
    f.write("Threshold\tArticles Below"+ "\n")
    above_t=0
    for i in range(1,max+1):
        if occ_dist[max+1 - i]> 0:
            above_t += occ_dist[max+1-i]
            f.write(str(occ_dist[max+1-i]) + "\t" + str(above_t) + "\n")
