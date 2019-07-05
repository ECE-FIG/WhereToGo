import cgi
from flask import Flask, render_template, request, url_for
import random
from yelp_api_handler import getBusinesses, getMatches

app = Flask(__name__)


@app.route("/")
def myHandler():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def inputHandler():
    NoneType = type(None)
    bOne = request.form.get('onedollar')
    bTwo = request.form.get('twodollar')
    bThree = request.form.get('threedollar')
    bFour = request.form.get('fourdollar')
    preBudgetList = []

    if type(bOne) != NoneType:
        preBudgetList.append(bOne)
    if type(bTwo) != NoneType:
        preBudgetList.append(bTwo)
    if type(bThree) != NoneType:
        preBudgetList.append(bThree)
    if type(bFour) != NoneType:
        preBudgetList.append(bFour)

    budget = (",").join(preBudgetList)
    term = request.form['category']
    openDuration = int(request.form['elapsed time'] or 0)
    distanceImportance = int(request.form['distance score'] or 0)
    ratingImportance = int(request.form['rating score'] or 0)
    location = str(request.form['location'] or "Austin, TX")
    # initialize parameters
    restaurantName = None
    rating = None
    yelpURL = None
    fakespotURL = None
    imageURL = None
    nameList = ""
    optionsList = getMatches(location, budget, term,
                             openDuration, distanceImportance, ratingImportance)
    maxIndices = len(optionsList)

    if maxIndices != 0:
        randIndex = random.randint(0, maxIndices-1)
        restaurantChoice = optionsList[randIndex]

        # if needed, loop through more restaurants until an open one is found
        while (restaurantChoice.get('is_closed')):
            randIndex = random.randint(0, maxIndices-1)
            restaurantChoice = optionsList[randIndex]

        restaurantName = optionsList[randIndex].get('name')
        rating = optionsList[randIndex].get('rating')
        yelpURL = optionsList[randIndex].get('url')
        fakespotURL = "https://www.fakespot.com/analyze?url=" + yelpURL
        imageURL = optionsList[randIndex].get('image_url')

        for item in optionsList:
            nameList += item.get("name") + "<br><br>"

        print("\nFinal Restaurant Decision: " +
              restaurantChoice.get('name'))
        print("Rating (rounded): " + str(rating) + " / 5.0")
        print("Yelp URL: " + yelpURL)
        print("FakeSpot URL (for fake yelp URL detection): " + fakespotURL)
        print("Image URL: " + imageURL)
        # Eventually, implement reviews
    else:
        print("Critera was too strict to return a match!")
    return render_template('results.html', restaurantName=restaurantName, rating=rating, yelpURL=yelpURL, fakespotURL=fakespotURL, imageURL=imageURL, nameList=nameList)


if __name__ == "__main__":
    app.run(debug=True)
