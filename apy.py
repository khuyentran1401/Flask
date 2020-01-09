
from flask import Flask, request, jsonify
from sklearn.externals import joblib
import traceback
import pandas as pd  
import numpy as np 
import sys
import os

app = Flask(__name__)

@app.route('/predict',methods=['POST'])

def predict():

	#If the model exists
	if forest_clf:
		try:

			#Create a dataframe as JSON
			json_ = request.json_

			query = pf.get_dummies(pd.dataframe(json_))
			
			
			#Missing input values will have the value of zero
			query = query.reindex(columns=model_columns, fill_value=0)

			#Predict with the trained model and return the list of predictions
			prediction = list(forest_predictions.predict(query))
			return jsonify({'prediction':list(prediction)})

		except:

			return jsonify({'trace': traceback.format_exc()})

	else:
		print("Train the model first")
		return("No model here to use")

if __name__=='__main__':
	try:
		port = int(sys.argv[1]) #First command line argument passed to the script

	except:
		port = 12345 #If no port is provided, the port will be set to 12345

	#load model
	forest_clf = joblib.load("forest.pkl")
	print('Model loaded')
	model_columns = joblib.load("model_columns.pkl")
	print('Model columns loaded')

	app.run(port=port, debug=True)

