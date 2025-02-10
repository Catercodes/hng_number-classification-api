from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Enable CORS
from flask_cors import CORS
CORS(app)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d**len(digits) for d in digits) == n

def classify_number(n):
    properties = []
    if is_prime(n):
        properties.append("prime")
    if is_perfect(n):
        properties.append("perfect")
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("odd" if n % 2 else "even")
    
    return properties

@app.route('/api/classify-number', methods=['GET'])
def classify():
    num = request.args.get("number")
    
    # Validate input
    if not num or not num.isdigit():
        return jsonify({"number": num, "error": True}), 400

    num = int(num)
    properties = classify_number(num)
    digit_sum = sum(int(d) for d in str(num))

    # Fetch a fun fact
    fact_url = f"http://numbersapi.com/{num}"
    fun_fact = requests.get(fact_url).text

    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

