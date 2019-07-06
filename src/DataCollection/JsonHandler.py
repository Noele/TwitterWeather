import json, time, datetime, sys
from pathlib import Path
import numpy as np

class JsonHandler():
    def __init__(self):
        #Get the path of Config.json
        current_path = Path(__file__).parents[1]
        self.configPath = Path(current_path / 'Data/DataCollection/Config.json')
        self.weatherDataPath = Path(current_path / 'Data/DataCollection/WeatherData.json')

        self.url = "https://api.openweathermap.org/data/2.5/weather?q=Edinburgh,uk&appid=";
        self.apiKey = ""

        #Open Config.json
        with self.configPath.open() as file:
            self.configJson = json.load(file)

        #Open WeatherData.json
        with self.weatherDataPath.open() as file:
            self.WeatherDataJson = json.load(file)

        for value in self.configJson:
            if self.configJson[value] == "":
                print(f"{value} in Config.json is empty, Exiting.")
                sys.exit()
    #Method for saving data to WeatherData.json
    def SaveWeatherData(self):
        with open(self.weatherDataPath, 'w') as fp:
            json.dump(self.WeatherDataJson, fp, indent=3)


    #Get the apikey from Config.json and append it to self.url
    def GetApiUrlAndKey(self):
        """Collect the weather api key from config.json"""
        print("Collecting api key from Config.json")
        self.apiKey = self.configJson["OWMAPIKEY"]
        return self.url + self.apiKey


    def SaveReleventDataFromApi(self, jsonResponce):
        """Save the data we need from OpenWeatherMaps"""
        # Create an inventory of the data we collected
        default_inv = {"name": jsonResponce.get('name'), "temprature": round(jsonResponce.get('main').get('temp') - 273.15),
                       "condition": jsonResponce.get('weather')[0].get('main')}

        new_inventory = {int(time.time()): default_inv} #Set the key as the current unix time
        self.WeatherDataJson["WeatherData"].insert(0, new_inventory) #Append that value to "WeatherData" at pos 0
        self.SaveWeatherData() #Save our information to WeatherData.json by calling the SaveWeatherData function

        #Print what we saved to the console
        print(jsonResponce.get('name'))
        print(f"Temprature : {round(jsonResponce.get('main').get('temp') - 273.15)}°c")
        print(f"Weather Condition: {jsonResponce.get('weather')[0].get('main')}")


    def RetrivePastTenTempratures(self):
        """Return the past 10 tempratures in WeatherData.json"""
        listOfTemps = np.array([])
        loopCount = 0
        if len(self.WeatherDataJson["WeatherData"]) < 10:
            return False
        for data in self.WeatherDataJson["WeatherData"]:
            loopCount += 1
            if loopCount == 11:
                break
            for key in data.keys():
                listOfTemps = np.append(listOfTemps, data[key]["temprature"])
        return listOfTemps

    def RetrivePastTenDates(self):
        """Return the past 10 dates in WeatherData.json"""
        listOfDates = np.array([])
        loopCount = 0
        if len(self.WeatherDataJson["WeatherData"]) < 10:
            return False
        for data in self.WeatherDataJson["WeatherData"]:
            loopCount += 1
            if loopCount == 11:
                break
            for key in data.keys():
                date = datetime.datetime.fromtimestamp(float(key)).strftime("%B %d, %Y")
                listOfDates = np.append(listOfDates, str(date))
        return listOfDates

    def RetrivePastTenConditions(self):
        """Return the past 10 Conditions in WeatherData.json"""
        listOfConditions = np.array([])
        loopCount = 0
        if len(self.WeatherDataJson["WeatherData"]) < 10:
            return False
        for data in self.WeatherDataJson["WeatherData"]:
            loopCount += 1
            if loopCount == 11:
                break
            for key in data.keys():
                listOfConditions = np.append(listOfConditions, data[key]["condition"])
        return listOfConditions

    def RetriveTwitterApiKey(self):
        """Return the twitter api key"""
        return self.configJson["TWITTER-API-KEY"]

    def RetriveTwitterSecretApiKey(self):
        """Return the secret twitter api key"""
        return self.configJson["TWITTER-SECRET-API-KEY"]

    def RetriveTwitterAccessToken(self):
        """Return the twitter access token"""
        return self.configJson["TWITTER-ACCESS-TOKEN"]

    def RetriveTwitterSecretAccessToken(self):
        """Return the secret twitter access token"""
        return self.configJson["TWITTER-SECRET-ACCESS-TOKEN"]
JsonHandler = JsonHandler()