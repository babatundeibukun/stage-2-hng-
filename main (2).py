from flask import Flask , jsonify, request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS']= False

@app.route('/', methods=['POST'])
def computation():
   slackUsername = 'officialibk'
   operation_type= request.json['operation_type']
   x=int(request.json['x'])
   y=int(request.json['y'])
  
   if operation_type == 'addition':
     result= x+y
     
   elif operation_type == 'subtraction':
     result = x-y
     
   elif operation_type == 'multiplication':
      result = x*y
     
   return jsonify({
          'slackUsername': slackUsername,
          'operation_type': operation_type,
          'result': result})
  
    
app.run(host='0.0.0.0', port=81)
