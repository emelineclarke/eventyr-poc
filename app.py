from flask import Flask, render_template
import os
 
app = Flask(__name__)
app.secret_key = os.urandom(12)
 
@app.route('/')
def home():
    return render_template('home.html')

 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0', port=4000)
