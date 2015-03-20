#-*- encoding:utf-8 -*-
import codecs
from TextRank import KeywordExtraction, SentenceExtraction

class Extractor(object):
	"""docstring for Extractor"""
	def __init__(self, stop_words_file = None):
		super(Extractor, self).__init__()
		self.keyword_extraction = KeywordExtraction(stop_words_file=stop_words_file)
		self.sentence_extraction = SentenceExtraction(stop_words_file=stop_words_file)

	def keyword_train(self, text, num=10):
		self.keyword_extraction.train(text=text, window=2, lower=False, speech_tag_filter=True)
		keyword_res = self.keyword_extraction.get_keywords(num=num, word_min_len=2)
		keyphrase_res = self.keyword_extraction.get_keyphrases(keywords_num=20, min_occur_num=2)
		return keyword_res,keyphrase_res

	def sentence_train(self,text,num=2,limitedlen=100):
		self.sentence_extraction.train(text=text, lower=True, speech_tag_filter=True)
		abstract = self.sentence_extraction.get_key_sentences(limitedlen=limitedlen)
		return abstract

if __name__ == '__main__':
	text = codecs.open('./text/01.txt','r+','utf-8', 'ignore').read()
	extractor = Extractor(stop_words_file='./stopword.data')
	keyword,keyphrase = extractor.keyword_train(text=text)
	abstract = extractor.sentence_train(text, limitedlen=100)
	
	f = codecs.open('result_for_extractor.txt','w+','utf-8')
	
	f.write('keword:\n')
	f.write('/'.join(keyword))
	
	f.write('\nkeyphrase:\n')
	f.write('/'.join(keyphrase))

	f.write('\nabstract:\n')
	f.write('...'.join(abstract))
	f.close()