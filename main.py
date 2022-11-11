from flask import Flask, request
import csv

def getData(filename):
    fields = [ ]
    rows = [ ]
    zip_data = dict()

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    # parse to dictionary object
    for row in rows:

        # First, make sure zip code is in the form of 5-digit string
        zipcode = str(row[ 0 ])
        if len(zipcode) < 5:
            zipcode = "0" * (5 - len(zipcode)) + zipcode
        row[0] = zipcode

        # Initialize current zipcode object
        curr_zip_info = dict()

        # Fill in data
        for i in range(1, len(fields)):
            curr_zip_info[ fields[ i ] ] = row[ i ]

        # Save current zipcode object into main dictionary with key = zipcode
        zip_data[zipcode] = curr_zip_info

    return zip_data


app = Flask(__name__)
filename = "zip_code_database.csv"
zip_data = getData(filename)

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
        # If the user-entered zip is not in our dictionary, return error
        if str(zipcode) not in zip_data:
            return 'Zip code does not exist', 404
        return zip_data[zipcode], 200
    else:
        return 'Method not recognized', 405

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)