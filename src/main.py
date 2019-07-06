# Twitter Weather, Made by Noelee
# 3rd party libs used - PIL scipy matplotlib numpy pathlib requests


import DataCollection.ApiRequest as APIR
import Drawing.Graph as Draw
import OAuth.OAuthMain as OA
class main():
    def __init__(self):
        self.self = 1

    def main(self):
        """Main class to keep everything in order"""
        print("Starting \"CollectWeatherDataFromApi\" from ApiRequest.py")
        #APIR.ApiRequest.CollectWeatherDataFromApi()
        print("Starting \"CreateGraph\" from Graph.py")
        Draw.Graph.CreateGraph()
        print("Starting \"OAuthSend\" from OAuthMain.py")
        OA.OAuthMain.OAuthStart()

main = main()
main.main()
