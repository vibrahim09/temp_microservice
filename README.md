# temp_microservice
Microservice for Saud, Mohamed

## Request Data

To request data from this service, write the command "GetTemp" into the Weather.txt file.

An example of this will be shown below:

### Function Call (Provided by partner):
---
<img width="1359" alt="image" src="https://github.com/vibrahim09/temp_microservice/assets/68801469/c6841eff-7883-4255-bb64-ee1351ea3d09">



### Waether.txt file containing the command:
---
<img width="571" alt="image" src="https://github.com/vibrahim09/temp_microservice/assets/68801469/1c114190-f53f-400e-852c-3b5bc70c1580">


---

Once the request has been received, the microservice will check if the Weather file was updated and grab the command. If the command is correct, 
the microservice will grab the weather of Portland through an API call and store the value in the current_temp variable:

https://github.com/vibrahim09/temp_microservice/blob/cbcb2cd63e38ea9a759788594ada4bd80b0c4fe7/team_microservice.py#L31-L33
---

Then, the service will write the temperature in imperial units to the Weather.txt file updating it in the process:

<img width="589" alt="image" src="https://github.com/vibrahim09/temp_microservice/assets/68801469/7449f543-5e3d-4f31-b8c1-cb682ca9cbf7">

---

## Receive Data

To receive the data from this program, make sure to read the Weather.txt file once it has been updated. This will give you the current temperature of the city. 
