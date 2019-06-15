import requests

URL = "https://api.yelp.com/v3/businesses/search"
HEADERS = {
    'Authorization': 'Bearer TN738I_IAGsfYxDykZL49gJMVXIxf9OfFRiB93z5s6_JMEy34C1rHW7eKERYpbYfJvELwGU17VSpL2fVAWUGxWPGKB63qh7fID38nGiwLi1nafbw_Hs_bee29EsFXXYx'
}
LIMIT = 50

# budget string is in format "1,2,3" for 1-3 dollar signs


def getAffordableBusinesses(sortType: str, budget: str) -> list:
 #   file = open("./output.txt", "w", encoding='utf-8')
    location = "2001 E Martin Luther King Jr Blvd, Austin, TX 78702"
    # location = "Austin, TX"
    offset = 0

    # to loop through 1000 businesses
    # should be range(20) for entire 1000 businesses
    for i in range(5):
        if sortType == 'distance':
            PARAMS = {'limit': LIMIT, 'offset': offset,
                      'location': location, 'sort_by': 'distance', 'price': budget}
        elif sortType == 'review_count':
            PARAMS = {'limit': LIMIT, 'offset': offset,
                      'location': location, 'sort_by': 'review_count', 'price': budget}
        elif sortType == 'rating':
            PARAMS = {'limit': LIMIT, 'offset': offset,
                      'location': location, 'sort_by': 'rating', 'price': budget}
        elif sortType == 'best_match':
            PARAMS = {'limit': LIMIT, 'offset': offset,
                      'location': location, 'sort_by': 'best_match', 'price': budget}

        r = requests.get(url=URL, headers=HEADERS, params=PARAMS)
        offset += 50
     #   print(str(r.status_code) + "\n")
        data = r.json()
        businesses = data.get('businesses')
        return businesses

 #   file.close


#sortingMethod = input("Enter a sorting method: ")
budget = input("Enter a budget (format: 1,2,3 for $$$): ")
distanceList = getAffordableBusinesses('distance', budget)
reviewCountList = getAffordableBusinesses('review_count', budget)
ratingList = getAffordableBusinesses('rating', budget)
bestMatchList = getAffordableBusinesses('best_match', budget)


# Distance: 5/10 -- > top 50 elements
# Review Count: 6/10 -> top 40 elements
# rating: 7/20 -> top 30 elements
# Any duplicates between rating, review, and distance arrays? Make an array of them
# If not, then make an array with just most important category. Within that array,
