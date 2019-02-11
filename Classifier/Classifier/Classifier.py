from jsmin import jsmin
import numpy as np
from scipy.sparse import csr_matrix
import datetime
from nltk.corpus import stopwords
from nltk.book import *
from sortedcontainers import SortedList
import re
import array
s=set(stopwords.words('english'))
BasePath = "F:\\HallmarksEngine\\Data\\SciGraph\\comp\\"
count = 0
all_words = SortedList()

input_files_path_base = ""
output_files_path_base = ""
stat_filename = ""
article_list_filename = ""
dictionary_filename = ""
stat_filename_min = ""
article_list_filename_min = ""
dictionary_filename_min = ""


class Classifier(object):
    def __init__(self, hallmark_count, word_count):
        self.stat = {
            "word_count": word_count
            "hallmark_count": hallmark_count
            "date": datetime.datetime.now()
        }
        self.article_data = []
        self.dictionary_data = []

    def load_data(self):

    def build_Co_Mention_Matrix(self):

    def build_Path_Matrix(self):

    def classify(self):

    def write_output_for_UI(self):
        self.write_dictionary(self, dictionary_filename)
        self.write_stats(self, stat_filename)
        self.write_article_list(serlf, article_list_filename)

    def write_dictionary(self,filename):

    def write_stats(self,filename):
    
    def write_article_list(self,filename):

    def minify_all_files(self):
        f = create_file(self, output_files_path_base,stat_filename_min)
        with open(os.path.join(output_files_path_base, stat_filename), 'r') as stat_file
            f.write(jsmin(stat_file.read()))
        f.close()
        f = create_file(self, output_files_path_base,article_list_filename_min)
        with open(os.path.join(output_files_path_base, article_list_filename), 'r') as article_file
            f.write(jsmin(article_file.read()))
        f.close()
        f = create_file(self, output_files_path_base,dictionary_filename_min)
        with open(os.path.join(output_files_path_base, dictionary_filename), 'r') as dictionary_file
            f.write(jsmin(dictionary_file.read()))
        f.close()

    def clean_up_files(self):
        // TODO

    def create_file(self, path, filename):
        return open(os.path.join(path, filename),'w')