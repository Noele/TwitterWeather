import requests
import DataCollection.JsonHandler as JH

class ApiRequest():
    def __init__(self):
        self.url = ""


    def CollectWeatherDataFromApi(self):
        # Call our function to get the api key
        self.url = JH.JsonHandler.GetApiUrlAndKey()

        # Request the data from the api
        print("Requesting data from Open Weather map")
        jsonResponce = requests.get(self.url).json()
        print("Checking Responce code")

        # check if the responce code is 200 (success)
        if jsonResponce.get('cod') != 200:
            print(f"Failed to retrive weather data, Error Code - {jsonResponce.get('cod')}")
            return

        print("Responce code is valid, Storing weather data in pos 0\n")
        JH.JsonHandler.SaveReleventDataFromApi(jsonResponce)


ApiRequest = ApiRequest()



