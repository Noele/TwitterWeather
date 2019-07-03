import DataCollection.ApiRequest as APIR

class main():
    def __init__(self):
        self.self = 1

    def main(self):
        print("Starting \"CollectWeatherDataFromApi\" from ApiRequest.py")
        APIR.ApiRequest.CollectWeatherDataFromApi()

main = main()
main.main()