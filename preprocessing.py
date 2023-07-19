import requests 

class Preprocessor:
	
	def get_data(self):
		url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
		response = requests.get(url)
		tiny_shakespeare_text = response.text
		self.clean_data(tiny_shakespeare_text[:100])
		return tiny_shakespeare_text[:100]
		
	def clean_data(self, text):
		# set: gets the unique chars from text 
		# list: puts chars into a list 
		chars = sorted(list(set(text)))
		vocab_size = len(chars)
		print("chars: ", chars)
		print("vocab size: ", vocab_size)
		