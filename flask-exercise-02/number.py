from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/result', methods = ['GET'])
def result(): 
    try:
        number = int(request.args.get('number'))
        if number % 2 == 0:
            return render_template('result.html', result=f"{number} is even.")
        else:
            return render_template('result.html', result=f"{number} is odd.")
    except ValueError:
        return render_template('result.html', result=f"Please enter a valid integer")
        
if __name__ == '__main__':
    app.run(debug=True)
