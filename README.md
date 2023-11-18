# temp_microservice
Microservice for Saud, Mohamed

## Request Data

To request data from this service, write the command "GetTemp" into the Weather.txt file.

An example of this will be shown below:

### Function Call (Provided by partner):
---
<img width="1340" alt="image" src="https://github.com/vibrahim09/temp_microservice/assets/68801469/400222b0-27d0-413a-963d-f859a91aec7e">




### Waether.txt file containing the command:
---
<img width="663" alt="image" src="https://github.com/vibrahim09/temp_microservice/assets/68801469/10acba71-ea72-4e55-b76f-4af0d38c8138">



---

Once the request has been received, the microservice will check if the Weather file was updated and grab the command. If the command is correct, 
the microservice will grab the weather of Portland through an API call and store the value in the current_temp variable:

https://github.com/vibrahim09/temp_microservice/blob/cbcb2cd63e38ea9a759788594ada4bd80b0c4fe7/team_microservice.py#L31-L33
---

Then, the service will write the temperature in imperial units to the Weather.txt file updating it in the process:

<img width="662" alt="image" src="https://github.com/vibrahim09/temp_microservice/assets/68801469/b34e3481-0a03-4994-ab31-3e3699b1d14e">


---

## Receive Data

To receive the data from this program, make sure to read the Weather.txt file once it has been updated. This will give you the current temperature of the city. 

---
### Basic UML 

![image](https://github.com/vibrahim09/temp_microservice/assets/68801469/27baa50e-559b-431e-a907-1e48f8533255)

