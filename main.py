from flask import Flask, jsonify
from preprocessing import Preprocessor 

app = Flask(__name__)

@app.route('/')
def index():
	preprocessor = Preprocessor()
	tiny_shakespeare_text_sample = preprocessor.get_data()
	response = { "message": "Hello, from Pocket Shakespeare " + tiny_shakespeare_text_sample }
	return jsonify(response)	

app.run(host='0.0.0.0', port=81)
