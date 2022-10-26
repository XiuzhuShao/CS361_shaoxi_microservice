from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)
cache = dict()
headers = {'User-Agent': 'Chrome/106.0.5249.119'}


@app.route('/', methods=['GET'])
def index():
    return "Please navigate to /zipcode to use this API"


# @app.route('/<zipcode>', methods=[ 'GET' ])
# def get_info_via_zip(zipcode):
#     """
#     Fetches info from https://unitedstateszipcodes.org/<id> and parses info via beautiful soup. Returns a JSON object
#     of the resulting information.
#     :param zipcode: Integer Zip code
#     :return: JSON
#     """
#     if request.method == 'GET':
#         # If this request has previously been made, return the cached copy of the JSON data, else create
#         # a new entry to store data.
#         if zipcode in cache:
#             return cache[zipcode]
#         else:
#             res = {}
#             cache[zipcode] = res
#
#         # Using requests and BeautifulSoup, create soup object from which we will retrieve our data
#         url_string = "http://www.unitedstateszipcodes.org/" + str(zipcode)
#         page = requests.get(url_string, headers=headers)
#         soup = BeautifulSoup(page.content, "html.parser")
#
#         map_info = soup.find_all(id="map-info")
#
#
#
#
#         return res, 200
#     else:
#         return 'Method not recognized', 405


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
