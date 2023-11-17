import time
import os
import requests
import sys


def open_file(file: str) -> str:
    """Open a file and stores its contents in a variable
    args: file (str): The name of the file

    returns: contents (str): The contents of the file
    """
    originalTime = os.path.getmtime(file)

    while True:
        if os.path.getmtime(file) > originalTime:
            with open(file, "r") as read_file:
                contents = read_file.readline()
            originalTime = os.path.getmtime(file)
            return contents
        time.sleep(1)


def get_weather(trigger: str, data: dict) -> float:
    """checks if the program is running. If so, it returns the temp.

    Args: trigger (str): check is the program is running.

    Returns: current_temp(float): The current temp of the city in imperial units.
    """
    if trigger == "GetTemp":
        current_temp = data["main"]["temp"]
        return current_temp
    else:
        print("Program Not Running")


def write_to_file(file: str, temp: float) -> None:
    """Write the temp to the file so our program can read it.

    Args: file(str): Name of the file we are writing to.
        temp (float): The temperature to write in the file.

    """
    with open(file, "w") as opened_file:
        opened_file.write(str(temp))


def Open_weather_API(city: str, units: str):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "API KEY"  ###### TODO
    url = base_url + "appid=" + api_key + "&q=" + city + "&units=" + units
    response = requests.get(url).json()
    return response


def main():
    while True:
        try:
            text_file = "Weather.txt"
            start = open_file(text_file)
            data = Open_weather_API("Portland", "imperial")
            temp = get_weather(start, data)
            write_to_file(text_file, temp)
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    main()
