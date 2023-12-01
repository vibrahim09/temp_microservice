import requests
import json
import time


def call_api_and_save_to_json(url: str, filename: str):
    """
    Calls an API and saves the response to a JSON file.

    Parameters:
    - url: str
        The URL of the API to call.
    - filename: str
        The name of the JSON file to save the response to.

    Raises:
    - requests.exceptions.RequestException:
        If there is an error while making the API request.
    - IOError:
        If there is an error while saving the response to the JSON file.
    """
    try:
        # Make the API request
        response = requests.get(url).json()
        json_Obj = json.dumps(response)

        with open(filename, "w") as file:
            file.write(json_Obj)

        print(f"Response saved to {filename} successfully.")

    except requests.exceptions.RequestException as e:
        print(f"Error while making API request: {e}")

    except IOError as e:
        print(f"Error while saving response to JSON file: {e}")


# Example usage:
with open("APIKey.txt", "r") as file:
    APIKey = file.readline().strip()
base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_url = base_url + "appid=" + APIKey + "&q=" + "PORTLAND"
json_filename = "response.json"


# call_api_and_save_to_json(api_url, json_filename)

while True:
    time.sleep(1)
    f = open("Request.txt", "r+")
    ReadData = f.readline().strip()
    if ReadData == "run":
        call_api_and_save_to_json(api_url, json_filename)
        f.seek(0)
        f.truncate(0)
        f.close()
    f.close()
