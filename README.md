# Text-Summarization
This project compares the Lexrank and LSA algorithms for text summarization.</br>
Both these algorithms employ an extractive summarization methodology, i.e. important sentences from the original document are selected and concatenated to form a summary.</br>
The paper associated with this project was published in the peer-reviewed journal IJCST and can be found here - http://www.ijcstjournal.org/volume-4/issue-3/IJCST-V4I3P63.pdf

# Implementation 
The input files have word counts ranging from 500 – 25,000.</br>
The csv files for both the algorithms contain the word count associated with each text file and the time required for generation of the summary.</br> 
The corresponding output files contain the generated automatic summary. 

# Python packages used 
<b>Natural Language Toolkit (NLTK) -</b></br>
Open source Python library for Natural Language Processing.</br>
http://www.nltk.org/ </br>
<b>Sumy -</b></br>
Python library and command line utility version 0.4.1 used for
 extracting summary from html pages and plain text
 documents.</br>
https://pypi.python.org/pypi/sumy </br>

# Conclusion
For larger sized files (files with a
 greater word count), LSA is faster than Lexrank however for
smaller files (files with a smaller word count), Lexrank is
 faster.

# Future Scope
Comparing the quality of summary generated in
 addition to the efficiency in terms of speed for greater
 accuracy and ease of summarization. 
