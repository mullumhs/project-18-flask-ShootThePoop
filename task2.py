from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')		# Route	
def say_hello():		# Function
    return "Hello, visitor!"

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')
def calculator(operation, num1, num2):

    if operation == "add" or operation == "+":
        result = num1 + num2

    if operation == "subtract" or operation == "-":
        result = num1 - num2

    if operation == "multiply" or operation == "*":
        result = num1 * num2

    if operation == "divide" or operation == "division":
        result = num1 / num2

    return str(result)


@app.route('/search')
def search():
    query = request.args.get('q', '')
    category = request.args.get('category', 'all')
    return f'Searching for "{query}" in category: {category}'






if __name__ == '__main__':
    app.run(debug=True)