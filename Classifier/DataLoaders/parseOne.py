from nltk.corpus import stopwords
from nltk.book import *
import re
import sys
from progress.bar import Bar

id_start_at = 52
id_end_at = 84
filenames = [  '2009-2010']
ids = []
Articles = []
first_line_counter = 0
second_line_counter = 0
BasePath = "F:\\HallmarksEngine\\Data\\SciGraph\\comp\\"
progress_title = ""
max_bar_length = 40

tempb  = Bar('Test', max=4)
tempb.next()
tempb.next()
tempb.next()
tempb.next()
tempb.finish()


def titleset(inputfilename):
	return BasePath + 'springernature-scigraph-articles-'+inputfilename+'.cc-by.2017-11-07.nt'

def titleset_nc(inputfilename):
	return BasePath + 'springernature-scigraph-articles-'+inputfilename+'.cc-by-nc.2017-11-07.nt'

def readall():
        global id_start_at
        global id_end_at
        global Articles
        global first_line_counter
        global second_line_counter
        global ids
        for item in filenames:
                readone(item)

def readone(onefile):
        global id_start_at
        global id_end_at
        global Articles
        global first_line_counter
        global second_line_counter
        global ids
        ids = []
        Articles = []
        first_line_counter = 0
        second_line_counter = 0
        print('Checking if all files are present.')
        counter = 0
        with open(titleset(onefile)) as f:
                counter = counter+1
        with open(titleset_nc(onefile)) as f:
                counter = counter+1
        print('Found ' + str(counter) + ' files. No errors. Starting to process them...')

        print('Reading files for ' + onefile + ' part c.')
        with open(titleset(onefile)) as f:
                for line in f:
                        process_line(line)
        print('Reading files for ' + onefile + ' part nc.') 
        with open(titleset_nc(onefile)) as f:
                for line in f:
                        process_line(line)

        print("Done. Found " + str(len(ids)) + " Ids. Generating Articles.") 
        for id in ids:
                Articles.append(Article(id));

        print("Done. Gathering data for Articles.")
        startProgress("Reading lines")
        with open(titleset(onefile)) as f:
                for line in f:
                        process_line_for_articles(line)
        with open(titleset_nc(onefile)) as f:
                for line in f:
                        process_line_for_articles(line)
        endProgress()
        print("Done. Building Articles.")
        for art in Articles:
                art.build_from_lines()
                #art.print_lines()
        print("Done. Writing Datafiles.")
        with open(BasePath + "CancerArticlesShort" + onefile + ".dat", 'w') as of_short:
                for art in Articles:
                        of_short.write(art.UID + '\t' + art.Title + '\t' + art.Abstract + '\n')
        with open(BasePath + "CancerArticlesLong" + onefile + ".dat", 'w') as of_long:
                for art in Articles:
                        for line in art.Lines:
                                of_long.write(art.UID + '\t' + line + '\n')
        print("Done.")

def process_line_for_articles(line):
        global id_start_at
        global id_end_at
        global Articles
        global first_line_counter
        global second_line_counter
        global ids
        second_line_counter = second_line_counter +1
        if second_line_counter % 10000 == 0:
                progress(100 * second_line_counter / first_line_counter)
        id = line[id_start_at:id_end_at]
        if id in ids:
                for art in Articles:
                        if art.UID == id:
                                art.Lines.append(line.split('> ', 1)[1])
	
def process_line(line):
        global id_start_at
        global id_end_at
        global Articles
        global first_line_counter
        global second_line_counter
        global ids
        first_line_counter = first_line_counter +1
        if 'cancer' in line.lower():
                id = line[id_start_at:id_end_at]
                if id not in ids:
                        ids.append(id)

def startProgress(title):
        global progress_x
        global progress_title
        global bar
        global max_bar_length
        progress_title = title
        bar = Bar(progress_title, max=max_bar_length)
        bar.next()
        progress_x = 0

def progress(x):
        global progress_x
        global bar
        global max_bar_length
        x = int(x * 40 // 100)
        if x != progress_x:
                bar.next()        
                progress_x = x

def endProgress():
        global bar
        bar.finish()

s=set(stopwords.words('english'))

class Article(object):
	def __init__(self,id):
		self.UID = id
		self.Title = "#nf#"
		self.Abstract = "#nf#"
		self.Lines = []

	def set_Title(self,title):
		self.Title = title

	def set_Abstract(self,abstract):
		self.Abstract = re.sub('[\.,!]', '', abstract)

	def prepareText(self):
		self.Words = filter(lambda w: not w in s,self.Abstract.split())
		self.Distribution = FreqDist(self.Words)

	def print(self):
		self.Distribution.pprint(100)
	def print_lines(self):
		print(self.UID + ":" + self.Title)
		for line in self.Lines:
			print(line)
	def build_from_lines(self):
		for line in self.Lines:
			if 'abstract' in line.lower().split('> ',1)[0]:
				self.set_Abstract(line.split('> ')[1])
			if 'title' in line.lower().split('> ',1)[0]:
				self.set_Title(line.split('> ')[1])
			
			
readall()
	
	
