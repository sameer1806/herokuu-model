import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
def ValuePredictor(to_predict_list): 
	to_predict =  np.array(to_predict_list).reshape(1,9)
	loaded_model = pickle.load(open("finalized_model.pkl", "rb")) 
	result = loaded_model.predict(to_predict)
	return result[0]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST']) 
def predict(): 
	if request.method == 'POST': 
		to_predict_list = request.form.to_dict() 
		to_predict_list = list(to_predict_list.values()) 
		to_predict_list = list(map(int, to_predict_list)) 
		result = ValuePredictor(to_predict_list)		 
		if int(result)== 1: 
			prediction ='booking'
		else: 
			prediction ='not booking'			
		return render_template("index.html", prediction_text = prediction)



if __name__ == "__main__":
    app.run(debug=True) 
    
    