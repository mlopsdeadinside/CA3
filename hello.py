from flask import Flask, request, jsonify

app = Flask(__name__)


def add(x,y):
    return x+y

def mul(x,y):
    return x*y

def sub(x,y):
    return x-y

def div(x,y):
    return x/y

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

# Define routes for calculator operations
@app.route('/calc/add/<int:num1>/<int:num2>', methods=['GET'])
def calculate_add(num1, num2):
    result = add(num1, num2)
@app.route('/calc/sub/<int:num1>/<int:num2>', methods=['GET'])
def calculate_sub(num1, num2):
    result = sub(num1, num2)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(port=5000)