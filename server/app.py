from flask import Flask, render_template
from flask import request, jsonify
from start import start

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('./index.html')

# this route receives json in request and it should have key "name"
@app.route('/getfiling', methods=['GET'])
def api():
    start()
    # data = request.get_json()
    # result = {'message': 'Hello, {}!'.format(data['name'])}
    return "request done successfully"

if __name__ == '__main__':
    app.run(port=5000, debug=True)