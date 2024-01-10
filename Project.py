from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("phishing.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form['url']
        prediction = predict_phishing(url)
        return render_template('result.html', prediction=prediction, url=url)

@app.route('/prevention')
def prevention():
    return render_template('prevention.html')

def predict_phishing(url):
    result = model.predict([url])[0]

    if result == 'bad':
        return "Phishing"
    else:
        return "Not Phishing"

if __name__ == '__main__':
    app.run(debug=True)
