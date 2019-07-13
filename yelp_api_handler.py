import requests
import time
import random

URL = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'Bearer TN738I_IAGsfYxDykZL49gJMVXIxf9OfFRiB93z5s6_JMEy34C1rHW7eKERYpbYfJvELwGU17VSpL2fVAWUGxWPGKB63qh7fID38nGiwLi1nafbw_Hs_bee29EsFXXYx'}
LIMIT = 50


def getBusinesses(location: str, sortType: str, budget: str, term: str, openDuration: int) -> list:
    businesses = []
    # budget string is in format "1,2,3,4" for 1-4 dollar signs
    # location = "29.720, -95.34"
    # location = "Austin, TX"
    offset = 0

    # add a couple hours to allow eating?
    openAt = int((openDuration * 3600) + time.time())

    # to loop through 1000 businesses
    # should be range(20) for entire 1000 businesses
    for i in range(2):
        if sortType == 'distance':
            PARAMS = {'limit': LIMIT, 'offset': offset,
                      'location': location, 'sort_by': 'distance', 'price': budget, 'term': term, 'open_at': openAt}
        elif sortType == 'review_count':
            PARAMS = {'limit': LIMIT, 'offset': offset,
                      'location': location, 'sort_by': 'review_count', 'price': budget, 'term': term, 'open_at': openAt}
        elif sortType == 'rating':
            PARAMS = {'limit': LIMIT, 'offset': offset,
                      'location': location, 'sort_by': 'rating', 'price': budget, 'term': term, 'open_at': openAt}
        elif sortType == 'best_match':
            PARAMS = {'limit': LIMIT, 'offset': offset,
                      'location': location, 'sort_by': 'best_match', 'price': budget, 'term': term, 'open_at': openAt}

        r = requests.get(url=URL, headers=HEADERS, params=PARAMS)
        offset += 50
        data = r.json()

        print(data)
        businesses.extend(data.get('businesses'))
    return businesses


def getMatches(location: str, budget: str, term: str, openDuration: int, distanceImportance: int, ratingImportance: int) -> list:
    # budget = input("Enter a budget (format: 1,2,3 for $$$): ")
    # term = input("Enter a category: ")
    # openDuration = int(input("Hours until you plan to go: "))
    # distanceImportance = int(
    #     input("Rate the importance of distance from 1-10: "))
    # ratingImportance = int(input("Rate the importance of ratings from 1-10: "))

    # budget = "1,2"
    # term = "asian"
    # openDuration = 4
    # distanceImportance = 5
    # ratingImportance = 5

    distanceList = getBusinesses(location,
                                 'distance', budget, term, openDuration)
    # reviewCountList = getBusinesses(location, 'review_count', budget, term, openDuration)
    ratingList = getBusinesses(location,
                               'rating', budget, term, openDuration)
    # bestMatchList = getBusinesses(location, 'best_match', budget, term, openDuration)

    print("\nLooking through potential restaurant ideas...")
    businessCount = len(distanceList)

    for i in range(0, businessCount, 10):
        maxDistance = int((10 - distanceImportance) * 100 * i)
        maxRating = int((10 - ratingImportance) * 100 * i)
        bestDistanceList = distanceList[0:maxDistance]
        bestRatingList = ratingList[0:maxRating]
        optionsList = [a for a in bestDistanceList if a in bestRatingList]

        print()
        print(businessCount)
        print(len(bestDistanceList))
        print(len(bestRatingList))
        print(len(optionsList))

        if len(optionsList) > 0:
            break
    return optionsList


# uncomment below to run example call
# getMatches("29.720, -95.34", "1", "food", 5, 10, 10)

# Distance: 5/10 -- > top 50 elements
# Review Count: 6/10 -> top 40 elements
# rating: 7/20 -> top 30 elements
# Any duplicates between rating, review, and distance arrays? Make an array of them
# If not, then make an array with just most important term. Within that array,

# no restaurants returned after Sunday
# getBusinesses('distance', "1, 2, 3, 4", "food", 12)
