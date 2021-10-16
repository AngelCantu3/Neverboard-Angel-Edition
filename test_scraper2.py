import requests
from bs4 import BeautifulSoup
import json
import pandas
from pandas import DataFrame

def main():

    page = requests.get("https://www.tourtexas.com/all-events")
    soup = BeautifulSoup(page.text, 'html.parser')

    events = soup.find_all(type="application/ld+json")
    names = []
    urls = []
    startDates = []
    endDates = []
    addresses = []
    cities = []
    zips = []



    for i in range(1, len(events)):
        try:   
            contents = events[i].contents[0]
            event_json = json.loads(contents)
            event_location = event_json[0]
            
            names.append(event_location['name'])
            if 'url' in event_location:
                urls.append(event_location['url'])
            else:
                urls.append('N/A')
            startDates.append(event_location['startDate'])
            endDates.append(event_location['endDate'])
            addresses.append(event_location['location']['address']['streetAddress'])
            cities.append(event_location['location']['address']['addressLocality'])
            zips.append(event_location['location']['address']['postalCode'])
        except:
            pass

    dict = {'name': names, 'url': urls, 'start date': startDates, 'end date': endDates, 'address': addresses, 'city': cities, 'zip': zips}
    df = pandas.DataFrame(dict)

    df.to_csv('events.csv')

main()
    


