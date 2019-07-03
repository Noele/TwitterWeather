import DataCollection.JsonHandler as JH
import numpy as np
import matplotlib.pyplot as plt
class Graph():
    def __init__(self):
        self.x = 1

    def testGraph(self):
        tempratures = JH.JsonHandler.RetrivePastTenTempratures()
        dates = JH.JsonHandler.RetrivePastTenDates()
        try:
            if tempratures == False:
                return print("Not enough data in WeatherData.json")
            if dates == False:
                return print("Not enough data in WeatherData.json")
        except(ValueError):
            pass

        dayNumber = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


        plt.plot(dayNumber, tempratures, 'k')
        plt.xlabel('Day')
        plt.ylabel('Temprature')
        plt.xticks(dayNumber, dates, rotation=45)

        figure = plt.gcf()
        figure.set_size_inches(18.5, 10.5)
        figure.savefig('output.png', dpi=100)





Graph = Graph()