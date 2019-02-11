# from parseOne import Article
import re

listOfFileNames = ["F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2017.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2016.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2015.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2014.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2013.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2012.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2011.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2009-2010.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2006-2008.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-2001-2005.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-1996-2000.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-1991-1995.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-1981-1990.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-1971-1980.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-1951-1970.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-1901-1950.cc-by.2017-11-07.nt", "F:/HallmarksEngine/Data/SciGraph/comp/springernature-scigraph-articles-1801-1900.cc-by.2017-11-07.nt"]

def crawlOneFile(filename):
    print("Crawling file: " + filename)
    exp = re.compile("Cigarette smoking, physical activity, a")
    exp2 = re.compile("cancer")
    with open(filename) as f:
        keepGoing = True
        line = f.readline()
        cnt =1 
        while keepGoing:
            if exp.search(line):
                print(line)
            
            # if exp2.search(line):
            #     print(line)
            line = f.readline()
            cnt +=1
            if line:
                keepGoing = True
            else:
                keepGoing = False
        
crawlOneFile(listOfFileNames[3])

# <http://scigraph.springernature.com/ontologies/core/title
