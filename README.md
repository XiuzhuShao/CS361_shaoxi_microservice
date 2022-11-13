# CS361_shaoxi_microservice
A simple web scraper REST API service that takes in a user-input zipcode and returns information about that zipcode via JSON.
## Requesting Data
With a zipcode in mind, send a GET request to the URL https://shaoxi-cs361-microservice.uc.r.appspot.com/<zipcode\><br/><br/>
Sample call: https://shaoxi-cs361-microservice.uc.r.appspot.com/78704  (Click me, this works!)<br/>
## Receiving Data
Once the request is received, the service return information about the zipcode if this zipcode exists in the local csv data file, and an error message if the zipcode does not exist.<br/><br/>
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
![UML sequence](https://github.com/XiuzhuShao/CS361_shaoxi_microservice/blob/master/microservice%20uml%20v2.png)
