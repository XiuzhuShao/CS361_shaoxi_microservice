from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
headers = {'User-Agent': 'Chrome/106.0.5249.119'}

@app.route('/')
def index():
    return "Please navigate to /zipcode to use this API"\


@app.route('/<zipcode>', methods=['GET'])
def get_info_via_zip(zipcode):
    """
    Fetches info from https://unitedstateszipcodes.org/<zipcode> and parses info via beautiful soup. Returns a JSON object
    of the resulting information.
    :param zipcode: string zip code
    :return: JSON
    """
    if request.method == 'GET':
        res = dict()

        # Using requests and BeautifulSoup, create soup object from which we will retrieve our data
        url_string = "http://www.unitedstateszipcodes.org/" + str(zipcode)
        page = requests.get(url_string, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")

        # Get all tables
        tables = soup.find_all('table')

        # If there are no tables this isn't a valid search term
        if not tables:
            return 'Zip code does not exist',404

        # Find the post office city/state
        res[ "city_state" ] = tables[ 0 ].find("td").text.strip().split('(')[ 0 ].strip()

        # Find the county
        res[ "county" ] = tables[ 0 ].find_all("td")[ 2 ].text.strip()

        # Find the timezone
        res[ "timezone" ] = tables[ 0 ].find_all("td")[ 3 ].text.strip().split('(')[ 0 ].strip()

        # Find the population
        res[ "population" ] = int(tables[ 1 ].find("td", class_="text-right").text.strip().replace(',', ''))

        # Find the number of housing units
        res[ "housing_units_by_number" ] = int(
            tables[ 1 ].find_all("td", class_="text-right")[ 2 ].text.strip().replace(',', ''))

        # Find the median home value
        res[ "median_home_value_by_dollar" ] = tables[ 1 ].find_all("td", class_="text-right")[
            3 ].text.strip().replace(',', '')

        # Find the median household income
        res[ "median_household_income_by_dollar" ] = tables[ 2 ].find_all("td", class_="text-right")[
            3 ].text.strip().replace(',', '')

        # Find the median age
        res[ "median_age" ] = int(tables[ 3 ].find_all("td")[ 1 ].text.strip().replace(',', ''))

        # Find the families vs singles information
        res[ "living_arrangements_by_number_of_people" ] = {
            "married": int(tables[ 10 ].find_all("td", class_="text-right")[ 0 ].text.strip().replace(',', '')),
            "single_guardian": int(tables[ 10 ].find_all("td", class_="text-right")[ 2 ].text.strip().replace(',', '')),
            "single": int(tables[ 10 ].find_all("td", class_="text-right")[ 4 ].text.strip().replace(',', '')),
            "single_with_roommates": int(
                tables[ 10 ].find_all("td", class_="text-right")[ 6 ].text.strip().replace(',', ''))
        }

        # Find the owner/renter breakdown
        res[ "housing_occupancy_types_by_number_of_people" ] = {
            "owned_with_mortgage": int(
                tables[ 15 ].find_all("td", class_="text-right")[ 0 ].text.strip().replace(',', '')),
            "owned_outright": int(tables[ 15 ].find_all("td", class_="text-right")[ 2 ].text.strip().replace(',', '')),
            "renter_occupied": int(tables[ 15 ].find_all("td", class_="text-right")[ 4 ].text.strip().replace(',', '')),
            "vacant": int(tables[ 15 ].find_all("td", class_="text-right")[ 6 ].text.strip().replace(',', ''))
        }

        # Find rental property by number of rooms
        res[ "rental_property_by_number" ] = {
            "studio": int(tables[ 17 ].find_all("td", class_="text-right")[ 0 ].text.strip().replace(',', '')),
            "one_bedroom": int(tables[ 17 ].find_all("td", class_="text-right")[ 2 ].text.strip().replace(',', '')),
            "two_bedroom": int(tables[ 17 ].find_all("td", class_="text-right")[ 4 ].text.strip().replace(',', '')),
            "three+_bedroom": int(tables[ 17 ].find_all("td", class_="text-right")[ 6 ].text.strip().replace(',', ''))
        }
        return res, 200
    else:
        return 'Method not recognized', 405

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)