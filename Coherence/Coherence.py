##
#	COHERENCE GRADER
#		-- assigns a score based on the coherence of the essay
#	
#	@author karthik and aparna
#	@date 08 April 2012 -- karthik -- getCoherenceMeasure()
#	@date 13 April 2012 -- karthik -- getRelatedWords()
#	@date 14 April 2012 -- aparna  -- getScore()
#
##

from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import re
#for graph
import networkx as nx
#for score
import math



##
# @brief returns a set of related words to the given word
#	-- called by makeWordGraph()
#
def getRelatedWords(word):
	
	relWords = set()
	
	for synset in wn.synsets(word):
		# add lemma names to the list
			#replacing _ with - as a word separater in phrases
		relWords |= set([name.replace("_", "-") for name in synset.lemma_names])
		
		# add hyponyms to the list
			#replacing _ with - as a word separater in phrases
		relWords |= set(name.replace("_","-") for name in 
							[lemma.name for subsynset in synset.hyponyms() 
											for lemma in subsynset.lemmas])
		
	#print relWords
	return relWords




# @brief make a word graph of related words
#		 INPUT : essay
#		 OUTPUT: graph
#
def makeWordGraph(essay):
	# list of stopwords
	stopwordsList = stopwords.words('english')
	
	# split the essay into words minus the stopwords
	wordList = [word for word in re.findall(r'\w+', essay) if word.lower() not in stopwordsList]
	
	# make a graph
	graph = nx.Graph()
		
	# make every word a node in the graph
	graph.add_nodes_from(wordList)
	
	# consider every word in the word list
	for word in wordList:
		
		#get a list of related words
		relatedWords1 =  getRelatedWords(word)
		
		# if the related word is present in the essay, increase the degrees by 2
		for relWord1 in relatedWords1:
			if relWord1 in graph:
				graph.add_edge(word, relWord1, weight=2)
			
			# finding the related words in the second level
			# if the related word is present in the essay, increase the degrees by 1
			relatedWords2 =  getRelatedWords(relWord1)
			for relWord2 in relatedWords2:
				if relWord2 in graph:
					graph.add_edge(word, relWord2, weight=1)
	
	#return the obtained word graph
	return graph




##
#@brief returns a score for the essay with its topic being the 1st paragraph
#
def getScore(clustCoffList,graph):
	
	rangeList=[0,0,0,0,0,0,0,0,0,0,0]
	average=0.0
	
	for ele in clustCoffList:
		rangeList[int(math.floor(clustCoffList[ele]*10))]=rangeList[int(math.floor(clustCoffList[ele]*10))]+1
	
	for i in range(len(rangeList)):
		rangeList[i]=rangeList[i]/float(len(graph))
	
	i=1
	for i in range(len(rangeList)-1):
		average=average+rangeList[i]
	#####
	print rangeList[0]
	print rangeList[10]
	#####
	if(rangeList[0]<=0.3 and rangeList[10]<=0.10):
		return 'completely relevant'
	elif((rangeList[0]>0.3 or rangeList<=0.4) and rangeList[10]<=0.10):
		return 'moderately relavant'
	else:
		return 'irrelevant'




# @brief main function to be called
#		 INPUT : essay
#		 OUTPUT: Coherence Measure (Score)
#
def getCoherenceMeasure(essay):
	graph = makeWordGraph(essay)
	# obtain clustering coefficient			
	clustCoeffList=nx.clustering(graph)
	#####
	print getScore(clustCoeffList,graph)
	print nx.average_clustering(graph)
	#####



# TEST DRIVER FOR TESTING THE MODULE INDEPENDENTLY
if __name__ == '__main__':

	#open essay
	sourceFileName = "../Sample_Essays/dog.txt"
	sourceFile = open(sourceFileName, "r")
	
	#read essay
	essay = sourceFile.read()

	getCoherenceMeasure(essay)
	
