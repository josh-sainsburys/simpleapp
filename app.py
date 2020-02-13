from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cars/')
def my_link():
  print('I got clicked!')
  res = requests.get('http://cars-python.cars-python-uat.svc.cluster.local:5000/api/v1.0/cars') # the service name

  return res.text

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False)
