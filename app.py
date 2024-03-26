from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "Coolchiken123"
debug = DebugToolbarExtension(app)
app.debug = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

Reponses= []

#init page
@app.route("/")
def home_page():
    return render_template("base.html")

# question 1
@app.route("/question/1", methods = ["POST"])
def question_1():
    season = request.form['season']
    # #add to database
    flash("you got it! Keep going. :)")
    Reponses.append(season)
    return redirect("/question/2")
    # return render_template("question_1.html", responses = Reponses)

# Question 2
@app.route("/question/2")
def question_2():
    cuisine = request.form['cusine']
    Reponses.append(cuisine)
    return redirect("/question/3")

# Question 3
@app.route("/question/3")
def question_3():
    time = request.form['time']
    Reponses.append(time)
    return redirect("/question/3")


# Question 4
@app.route("/question/4")
def question_4():
    vacation = request.form['vaction']
    Reponses.append(vacation)
    return redirect("/question/5")



@app.route("/question/5")
def question_5():
    return redirect("/end")

#end
@app.route("/end")
def end():
    return render_template("end.html")