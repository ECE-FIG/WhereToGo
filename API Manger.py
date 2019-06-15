import requests

URL = "https://api.yelp.com/v3/businesses/search"
HEADERS = {
'Authorization': 'Bearer TN738I_IAGsfYxDykZL49gJMVXIxf9OfFRiB93z5s6_JMEy34C1rHW7eKERYpbYfJvELwGU17VSpL2fVAWUGxWPGKB63qh7fID38nGiwLi1nafbw_Hs_bee29EsFXXYx'
}
LIMIT = 50


def getBusinesses(sortType):
    file = open("WhereToGo/testfile1.txt", "w", encoding='utf-8')
    location = "2001 E Martin Luther King Jr Blvd, Austin, TX 78702"
    # location = "Austin, TX"
    offset = 0

    if sortType == 'distance':
        PARAMS = {'limit': LIMIT, 'offset': offset,
                  'location': location, 'sort_by': 'distance'}
    elif sortType == 'reviewCount':
        PARAMS = {'limit': LIMIT, 'offset': offset,
                  'location': location, 'sort_by': 'review_count'}
    elif sortType == 'rating':
        PARAMS = {'limit': LIMIT, 'offset': offset,
                  'location': location, 'sort_by': 'rating'}
    elif sortType == 'bestMatch':
        PARAMS = {'limit': LIMIT, 'offset': offset,
                  'location': location, 'sort_by': 'best_match'}

    # to loop through 1000 businesses
    # should be range(20) for entire 1000 businesses
    for i in range(5):
        r = requests.get(url=URL, headers=HEADERS, params=PARAMS)
        offset += 50
        print(str(r.status_code) + "\n")
        data = r.json()

        businesses = data.get('businesses')

        #  filter = [business for business in businesses if business.get(
        #     'distance') < 2500]

        # print(businesses)

        for business in businesses:
            stuff = business.get('name') + " " + str(business.get(sortType))

            file.write(stuff + "\n")
            print(stuff)

        # print("\n")
        # print(data.get('total'))

    file.close


getBusinesses('rating')
