from flask import Flask,request,jsonify,render_template
import json
from datetime import datetime
app = Flask(__name__)

data = []
@app.route('/raw')
def raw():
  return jsonify(data)

def getdata():
  global data
  return data

@app.route('/')
def index():
  print(data)
  return render_template('index.html',data=data)
@app.route('/data/writeout',methods = ['GET'])
def writeout():
  json.dump(data,open("DATABACKUP.json",'w'))
  return "WRITTEN"

@app.route('/data/readin',methods = ['GET'])
def readin():
  global data
  data = json.load(open("DATABACKUP.json"))
  return "WRITTEN"

@app.route('/data/add',methods = ['POST'])
def add_data():
  foo = dict()
  if not data:
    foo['id'] = 1
  else:   
    foo['id'] = data[-1]['id']+1
  foo['ip'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
  foo['data'] = request.json.get('data',)
  foo['timestamp'] = datetime.now().isoformat()
  data.append(foo)
  return jsonify({'data': foo}), 201

if __name__ == '__main__':
  app.run(debug=True)