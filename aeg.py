from Statistics.Statistics import *
from Spellings.Spellings import *
from Grammar.Grammar import *
import sys

#open essay
sourceFileName = str(sys.argv[1])
#sourceFileName = "./Sample_Essays/essay2.txt"
sourceFile = open(sourceFileName, "r")

#read essay
essay = sourceFile.read()

#Statistics
wordCount = getWordCount(essay)
sentCount = getSentenceCount(essay)
paraCount = getParaCount(essay)
avgSentLen = getAvgSentenceLength(essay)
stdDevSentLen = getStdDevSentenceLength(essay)

#Spellings
numMisspelt, misspeltWordSug = spellCheck(essay)

#Grammar
grammarCumScore, grammarSentScore = getGrammarScore(essay)

s = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
	<title>Automated Essay Grader</title>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
	<meta name="generator" content="Geany 0.20" />
	<link type="text/css" rel = "stylesheet" href = "style.css" />
</head>

<body>
	<div id = "canvas">
		<div id = "heading"> <h1><center> AUTOMATED ESSAY GRADER </center></h1></div>
		<br />
		
		<div> 
		<img src = "./images/essay.jpg" />
		<h2> Essay :- </h2> <div id = "essay">'''

for para in essay.splitlines():
	if para == "":
		s = s + "<br /> <br />"
	else:
		s = s + para
	

s = s + '''</div> </div> <br /> <hr /> <hr /> <br />
		
		<div id = "statistics">
			<img src = "./images/stats.jpg" />
			<h2> Essay Statistics :- </h2>
			<table border = "1">
				<tr> <th>Word Count</th> <td>'''+ str(wordCount) + '''</td></tr>
				<tr> <th>Sentence Count</th> <td>'''+ str(sentCount) + '''</td></tr>
				<tr> <th>Paragraph Count</th> <td>'''+ str(paraCount) + '''</td></tr>
				<tr> <th>Average Sentence Length</th> <td>'''+ str(avgSentLen) + '''</td> </tr>
				<tr> <th>Standard Deviation from the Average Sentence Length</th> <td>'''+ str(stdDevSentLen) + '''</td> </tr>
			</table>
		</div>
		<br /> <hr /> <hr /> <br />
		
		<div id = "spellings"> 
			<img src = "./images/spell.jpg" />
			<h2> Spellings :- </h2>
			<h3 style="text-align:left">Number of Misspelt Words ::''' + str(numMisspelt) + '''</h3>
			<h2 style="text-align:right" class="score" >Score :: ''' + str((1-(float(numMisspelt)/wordCount))*5) + '''</h2>
			
			<table border="1">
				<thead> <tr> <th>Misspelt Word</th> <th> Spelling Suggestions</th> </tr> </thead>
				<tbody>'''

for key in misspeltWordSug:
	s = s + "<tr> <td>" + key + "</td> <td> " + str(misspeltWordSug[key]) + "</td> </tr>"


s = s + '''</tbody>
			</table>
		</div>
		<br /> <hr /> <hr /> <br />
		
		<div id ="grammar">
			<img src = "./images/grammar.jpg" />
			<h2> Grammar :- </h2>
			<h2 style="text-align:right" class = "score" >Score :: ''' + str(grammarCumScore) + '''</h2>
			
			<table border="0">
				<thead> <tr> <th>Sentences</th> <th> Score</th> </tr> </thead>
				<tbody>'''
				
for key in grammarSentScore:
	s = s + "<tr> <td>" + key + "</td> <td> " + str(grammarSentScore[key]) + "</td> </tr>"
	
	
s = s + ''' </tbody>
			</table>
		</div>
		<br /> <hr /> <hr /> <br />
		
		<div id="conclusion">
			Aparna N, Apoorva Rao B, Kathik R Prasad <br /> Guide: B Narsing Rao
		</div>
		
	</div>
	
</body>

</html>


'''

outputFileName = str(sys.argv[2])
outputFile = open(outputFileName,"w")
outputFile.write(s)


