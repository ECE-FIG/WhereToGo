import cgi
from flask import Flask, render_template, request, url_for
import random
from yelp_api_handler import getAffordableBusinesses, runFrontEndExample

app = Flask(__name__)


@app.route("/")
def myHandler():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def inputHandler():
    budget = request.form['budget']
    term = request.form['category']
    openDuration = int(request.form['elapsed time'])
    distanceImportance = int(request.form['distance score'])
    ratingImportance = int(request.form['rating score'])
    # initialize parameters
    restaurantName = None
    rating = None
    yelpURL = None
    fakespotURL = None
    imageURL = None
    nameList = ""

    optionsList = runFrontEndExample(
        budget, term, openDuration, distanceImportance, ratingImportance)
    maxIndices = len(optionsList)

    if maxIndices != 0:
        randIndex = random.randint(0, maxIndices-1)
        restaurantChoice = optionsList[randIndex]

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

        print("name list: " + nameList)
        print("\nFinal Restaurant Decision: " +
              restaurantChoice.get('name'))
        print("Rating (rounded): " + str(rating) + " / 5.0")
        print("Yelp URL: " + yelpURL)
        print("FakeSpot URL (for fake yelp URL detection): " + fakespotURL)
        print("Image URL: " + imageURL)
        # webbrowser.open(imageURL)
        # Eventually, implement reviews
    return render_template('results.html', restaurantName=restaurantName, rating=rating, yelpURL=yelpURL, fakespotURL=fakespotURL, imageURL=imageURL, nameList=nameList)


if __name__ == "__main__":
    app.run(debug=True)
