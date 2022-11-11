# CS361_shaoxi_microservice
A simple web scraper REST API service that takes in a user-input zipcode and returns information about that zipcode via JSON.
## Requesting Data
With a zipcode in mind, send a GET request to the URL https://shaoxi-cs361-microservice.uc.r.appspot.com/<zipcode\><br/><br/>
Sample call: https://shaoxi-cs361-microservice.uc.r.appspot.com/78704  (Click me, this works!)<br/>
## Receiving Data
Once the request is received, the service will make a separate call to an external website, scrape the resultant HTML data, and return to the user a JSON object in the response body consisting of housing-related information about the zipcode.<br/><br/>
Sample response from sample call:
```json
{
  "area_codes": "512,737",
  "county": "Travis County",
  "irs_estimated_population": "38520",
  "latitude": "30.24",
  "longitude": "-97.77",
  "primary_city": "Austin",
  "state": "TX",
  "timezone": "America/Chicago"
}
```
## UML Sequence Diagram
![UML sequence](https://github.com/XiuzhuShao/CS361_shaoxi_microservice/blob/master/microservice%20uml.png)
## Important Notes
Although rudimentary error-checking has been implemented to account for invalid zipcodes, the user should attempt to request info for valid zipcodes only, so that the number of API calls made to the external site can be minimized.
