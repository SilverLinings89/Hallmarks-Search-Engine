import sys

id_start_at = 52
id_end_at = 84
filenames = ['1901-1950', '1951-1970', '1971-1980', '1981-1990', '1991-1995', '1996-2000', '2001-2005', '2006-2008', '2009-2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017' ]
ids = []
Articles = []
first_line_counter = 0
second_line_counter = 0
BasePath = "F:\\HallmarksEngine\\Data\\SciGraph\\comp\\"
progress_title = ""
max_bar_length = 40

def titleset(inputfilename):
	return BasePath + 'CancerArticlesShort'+inputfilename+'.dat'

def readall():
        counter =0
        with open(BasePath + "CancerArticlesClean.dat", 'w') as of:
                for item in filenames:
                        with open(titleset(item)) as f:
                                for line in f:
                                        if "#nf#" not in line:
                                                counter = counter +1
                                                of.write(line)
                                                if counter % 1000 == 0:
                                                        print(counter)
readall()
