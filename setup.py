from flask import Flask, render_template, request
import pickle
from game import gam

model = pickle.load(open('game.pickle', 'rb'))

app = Flask(__name__ , template_folder ='templates')


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']

    dt = gam(data1, data2, data3, data4,data5,data6,data7,data8,data9)
    try:

        pred = model.predict(dt)

    except:
        pred= "OOPS....TRY AGAIN"
    return render_template('home.html', prediction_text=pred)


if __name__ == "__main__":
    app.run(debug=True)



