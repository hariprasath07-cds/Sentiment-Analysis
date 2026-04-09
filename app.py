import joblib
import numpy as np
from preprocess import preprocess
from flask import Flask,request,jsonify

app = Flask(__name__)

model=joblib.load('model.joblib')
vectorizer = joblib.load('tf_idf.joblib')

@app.route('/',methods=['GET'])
def home():
    return jsonify({
        'message': 'Sentiment Analysis API is running!',
        'endpoints':(
            'health': 'GET  /health',
            'predict': 'POST  /predict'
        )
    })            

@app.route("/predict",methods=["POST"])
def predict():
    data = request.get_json()

    reviews = data ['reviews']

    process_review = preprocess(reviews)

    process_review = vectorizer.transform([process_review])

    prediction = model.predict(process_review)

    return jsonify({"prediction": prediction[0]})



@app.route("/health",methods = ['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    #app.run(debug=True,host="0.0.0.0",port=5000)
    port = int(os.environ.get('POST',5000))
    app.run(host='0.0.0.0',port=port
            
