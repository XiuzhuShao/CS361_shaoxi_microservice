# CS361_shaoxi_microservice
A simple web scraper REST API service that takes in a user-input zipcode and returns information about that zipcode via JSON.
## Requesting Data
With a zipcode in mind, send a GET request to the URL https://shaoxi-cs361-microservice.uc.r.appspot.com/78704/<zipcode\><br/><br/>
Sample call: https://shaoxi-cs361-microservice.uc.r.appspot.com/78704  (Click me, this works!)<br/>
## Receiving Data
Once the request is received, the service will make a separate call to an external website, scrape the resultant HTML data, and return to the user a JSON object in the response body consisting of housing-related information about the zipcode.<br/><br/>
Sample response from sample call:
```json
{
  "city_state": "Austin, TX",
  "county": "Travis County",
  "housing_occupancy_types_by_number_of_people": {
    "owned_outright": 2090,
    "owned_with_mortgage": 5009,
    "renter_occupied": 14236,
    "vacant": 2240
  },
  "housing_units_by_number": 23575,
  "living_arrangements_by_number_of_people": {
    "married": 4741,
    "single": 9824,
    "single_guardian": 2557,
    "single_with_roommates": 4213
  },
  "median_age": 32,
  "median_home_value_by_dollar": "$347500",
  "median_household_income_by_dollar": "$50930",
  "population": 42117,
  "rental_property_by_number": {
    "one_bedroom": 5864,
    "studio": 1026,
    "three+_bedroom": 1343,
    "two_bedroom": 5559
  },
  "timezone": "Central"
}
```
## UML Sequence Diagram
![UML sequence](https://github.com/XiuzhuShao/CS361_shaoxi_microservice/blob/master/microservice%20uml.png)
## Important Notes
Although rudimentary error-checking has been implemented to account for invalid zipcodes, the user should attempt to request info for valid zipcodes only, so that the number of API calls made to the external site can be minimized.
