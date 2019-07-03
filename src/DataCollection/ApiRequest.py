from pathlib import Path
import json, requests, time

class ApiRequest():
    def __init__(self):
        #Get the path of Config.json
        current_path = Path(__file__).parents[0]
        self.configPath = Path(current_path / 'Data/Config.json')
        self.weatherDataPath = Path(current_path / 'Data/WeatherData.json')

        #Set our variables that we will need across the class
        self.url = "https://api.openweathermap.org/data/2.5/weather?q=Edinburgh,uk&appid=";
        self.apiKey = ""

        #Open Config.json
        with self.configPath.open() as file:
            self.configJson = json.load(file)
        #Open WeatherData.json
        with self.weatherDataPath.open() as file:
            self.WeatherDataJson = json.load(file)

    #Method for saving data to WeatherData.json
    def SaveWeatherData(self):
        with open(self.weatherDataPath, 'w') as fp:
            json.dump(self.WeatherDataJson, fp, indent=3)

    #Get the apikey from Config.json and append it to self.url
    def GetApiKey(self):
        print("Collecting api key from Config.json")
        self.apiKey = self.configJson["APIKEY"]
        self.url = self.url + self.apiKey

    def CollectWeatherDataFromApi(self):
        self.GetApiKey() #Call our function to get the api key
        print("Requesting data from Open Weather map")
        jsonResponce = requests.get(self.url).json() #Request the data from the api
        print("Checking Responce code")
        if jsonResponce.get('cod') != 200: # check if the responce code is 200 (success)
            print(f"Failed to retrive weather data, Error Code - {jsonResponce.get('cod')}")
            return
        print("Responce code is valid, Storing weather data in pos 0\n")

        default_inv = {"name": jsonResponce.get('name'), "temprature": round(jsonResponce.get('main').get('temp') - 273.15),
                       "condition": jsonResponce.get('weather')[0].get('main')} #Create an inventory of the data we collected

        new_inventory = {int(time.time()): default_inv} #Set the key as the current unix time
        self.WeatherDataJson["WeatherData"].insert(0, new_inventory) #Append that value to "WeatherData" at pos 0
        self.SaveWeatherData() #Save our information to WeatherData.json by calling the SaveWeatherData function

        #Print what we saved to the console
        print(jsonResponce.get('name'))
        print(f"Temprature : {round(jsonResponce.get('main').get('temp') - 273.15)}°c")
        print(f"Weather Condition: {jsonResponce.get('weather')[0].get('main')}")


ApiRequest = ApiRequest()



