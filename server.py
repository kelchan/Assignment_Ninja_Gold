from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "THIS IS MY SECRET"

global num_gold
num_gold = 0
global activities
activities = []

@app.route( '/' )
def home():
    return render_template( "index.html", num_gold = num_gold, activities = activities )

@app.route( '/process_money', methods = ['POST'] )
def process_money():
    print(request.form)
    global num_gold
    if request.form['building'] == 'farm':
        randomNum = random.randint(10, 20)
        num_gold += randomNum
        session['color'] = 'green'
        activities.append(f"Earned {randomNum} gold from the {request.form['building']}")
    if request.form['building'] == 'cave':
        randomNum = random.randint(5, 10)
        num_gold += randomNum
        session['color'] = 'green'
        activities.append(f"Earned {randomNum} gold from the {request.form['building']}")
    if request.form['building'] == 'house':
        randomNum = random.randint(2, 5)
        num_gold += randomNum
        session['color'] = 'green'
        activities.append(f"Earned {randomNum} gold from the {request.form['building']}")
    if request.form['building'] == 'casino':
        randomNum = random.randint(-50, 50)
        num_gold += randomNum
        if randomNum < 0:
            session['color'] = 'red'
            activities.append(f"Entered a casino and lost {randomNum * -1} gold")
        if randomNum >= 0:
            activities.append(f"Earned {randomNum} gold from the {request.form['building']}")

    return redirect( '/' )













if __name__ == "__main__":
    app.run(debug=True)
