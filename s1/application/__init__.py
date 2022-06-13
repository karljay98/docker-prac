from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/transformer', methods=['GET', 'POST'])
# a get request should be made for service 2 and 4
def show_transformer():
    s2 = requests.get('http://service2:5001/get/colour').text
    s3 = requests.get('http://service3:5002/get/car').text
    transformer = s2+","+s3 # concatenation of colour and car which is sent to service 4
    result = requests.post('http://service4:5003/post/transformer', data=transformer)
    return render_template('index.html', title='Transfromer generator', transformer=result.text, colour=s2, car=s3)

if __name__ == '__main__':
    app.run(port=5000, debug = True, host='0.0.0.0')