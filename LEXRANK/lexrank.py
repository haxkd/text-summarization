#Import library essentials
from lib2to3.pgen2.pgen import generate_grammar
from sumy.parsers.plaintext import PlaintextParser 
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer 
import time

 
def main():
	for i in range (1,11):

		start_time = time.time()

		filename = "input/"+str(i)+".txt"
		#filename = "plain_text.txt" #name of the plain-text file
		summary_words = 0 
		summary_characters = 0
		generated_summary = ''
		data = open("lexrank.csv", "a")
		op = open("output_lexrank.txt", "a")

		parser = PlaintextParser.from_file(filename, Tokenizer("english"))
		summarizer = LexRankSummarizer()

		summary = summarizer(parser.document, 5) #Summarize the document in 5 sentences

		op.write(filename+"\n")
		for sentence in summary:
			generated_summary+=str(sentence)
			op.write(str(sentence))
			print(sentence)
		
		new_time = time.time() - start_time
		print("Time: ", new_time)

		summary_words = len(generated_summary.split())
		summary_characters = len(generated_summary)
		print(summary_characters, summary_words, filename)
		string = str(summary_characters)+" , "+str(summary_words)+" , "+str(new_time)+"\n"
		print(string)
		op.write("\n"+string+"\n")
		data.write(string)

	data.close()
	op.close()

if __name__ == "__main__":
	main()
