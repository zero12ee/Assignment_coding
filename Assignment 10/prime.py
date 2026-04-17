from flask import Flask, Response
import json

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/prime_number/<number>")

def prime_number(number):
    p_number = int(number)
    result = {"Number": p_number, "isPrime": is_prime(p_number)}
    return json.dumps(result)

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=5001)
