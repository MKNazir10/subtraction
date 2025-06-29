from flask import Flask, request, jsonify
from app.logic import subtract  # ✅ import logic from app package

app = Flask(__name__)

@app.route('/subtract')
def subtract_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = subtract(a, b)
    return jsonify({'result': result})
