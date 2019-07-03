import DataCollection.ApiRequest as APIR
import Drawing.Graph as draw

class main():
    def __init__(self):
        self.self = 1

    def main(self):
        print("Starting \"CollectWeatherDataFromApi\" from ApiRequest.py")
        APIR.ApiRequest.CollectWeatherDataFromApi()
        draw.Graph.testGraph()

main = main()
main.main()