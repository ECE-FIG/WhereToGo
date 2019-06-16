import cgi
from flask import Flask, render_template, request, url_for
from yelp_api_handler import getAffordableBusinesses, runFrontEndExample

app = Flask(__name__)

# budget = "1,2"
# term = "asian"
# openDuration = 4
# distanceImportance = 5
# ratingImportance = 5


@app.route("/")
def myHandler(value=None):
    myString = ""

    # budget = userInput.getvalue('budget')
    # term = userInput.getvalue('term')
    # openDuration = int(userInput.getvalue('elapsed time'))
    # distanceImportance = int(userInput.getvalue('distance'))
    # ratingImportance = int(userInput.getvalue('rating'))

    # myString = runFrontEndExample(
    #     budget, term, openDuration, distanceImportance, ratingImportance)
    # print(myString)
    return render_template('index.html', value=myString)
    # return render_template('index.html', value="HI")


@app.route('/', methods=['POST'])
def inputHandler(value=None):
    print("HELLO ELLOOOOO")
    print(request.form['budget'])
    budget = request.form['budget']
    myString = 'hi'
    term = request.form['category']
    openDuration = int(request.form['elapsed time'])
    distanceImportance = int(request.form['distance score'])
    ratingImportance = int(request.form['rating score'])

    myString = runFrontEndExample(
        budget, term, openDuration, distanceImportance, ratingImportance)
    # print(myString)
    return render_template('index.html', value=myString)

# if __name__ == "__main__":
#     app.run(debug=True)