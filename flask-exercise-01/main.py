#Group Mem:Gabe H, Reid W, Kelvin S
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now()
    date = current_time.strftime("The current date is %A, %B %d %Y")
    time = current_time.strftime("%I:%M:%S %p")
    return render_template("index.html", date=date, time=time)

if __name__ == '__main__':
    app.run(debug=True)