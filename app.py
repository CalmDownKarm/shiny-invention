from flask import Flask,request,jsonify
from datetime import datetime
app = Flask(__name__)

data = []
@app.route('/')
def index():
  return jsonify(data)

@app.route('/data/add',methods = ['POST'])
def add_data():
  foo = dict()
  if not data:
    foo['id'] = 1
  else:   
    foo['id'] = data[-1]['id']+1
  foo['ip'] = request.remote_addr
  foo['data'] = request.json.get('data',)
  foo['timestamp'] = datetime.now()
  data.append(foo)
  return jsonify({'data': foo}), 201

if __name__ == '__main__':
  app.run(debug=True)