import requests 

class Preprocessor:
	
	def get_data(self):
		url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
		response = requests.get(url)
		tiny_shakespeare_text = response.text
		return tiny_shakespeare_text[:100]
		
	def clean_data(self):
		pass
		