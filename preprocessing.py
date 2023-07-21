import requests 

class Preprocessor:
	
	def get_data(self):
		url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
		response = requests.get(url)
		tiny_shakespeare_text = response.text
		self.clean_data(tiny_shakespeare_text)
		return tiny_shakespeare_text[:100]
		
	def clean_data(self, text):
		"""
  		Character level tokenization 
		set: extracts unique chars from text 
  		list: puts chars into a list 
  		"""
		chars = sorted(list(set(text)))
		vocab_size = len(chars)
		stoi = { ch:i for i,ch in enumerate(chars) } # string to index, mapping from chars to integers
		itos = { i:ch for i,ch in enumerate(chars) } # index to string, mapping from integers to chars 
		# encoder: take a string, output a list of integers 
	    # Ex "hii there" -> [46, 47, 47, 1, 58, 46, 43, 56, 43]	
		encode = lambda s: [ stoi[c] for c in s ] 
		# decoder: take a list of integers and output a string
		# Ex [46, 47, 47, 1, 58, 46, 43, 56, 43] -> "hii there"	
		decode = lambda l: ''.join([itos[i] for i in l])
		