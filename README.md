# temp_microservice
Microservice for Saud, Mohamed

## Request Data

To request data from this service, write the command "GetTemp" into the Weather.txt file.

An example of this will be shown below:

<img width="1359" alt="image" src="https://github.com/vibrahim09/temp_microservice/assets/68801469/c6841eff-7883-4255-bb64-ee1351ea3d09">

Once the request has been received, the microservice will check if the Weather file was updated and grab the command. If the command is correct, 
the microservice will grab the weather of Portland through an API call and store the value in the current_temp variable:

https://github.com/vibrahim09/temp_microservice/blob/cbcb2cd63e38ea9a759788594ada4bd80b0c4fe7/team_microservice.py#L31-L33

Then, the service will write the temperature in imperial units to the Weather.txt file updating it in the process. 

## Receive Data

To receive the data from this program, make sure to read the Weather.txt file once it has been updated. This will give you the current temperature of the city. 
