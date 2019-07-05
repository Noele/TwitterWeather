import DataCollection.JsonHandler as JH
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from PIL import Image

class Graph():
    def __init__(self):
        self.DrawingBuiltImagesPath = "Data/Drawing/BuiltImages/"
        self.DrawingConditionsPath = "Data/Drawing/Conditions/"

    def CreateGraph(self):
        #Grab the past 10 datasets
        tempratures = JH.JsonHandler.RetrivePastTenTempratures()
        dates = JH.JsonHandler.RetrivePastTenDates()
        conditions = JH.JsonHandler.RetrivePastTenConditions()

        #Make sure that the data doesnt return as False
        validationLayer = self.ValidateDataSets(tempratures, dates, conditions)
        if validationLayer == False:
            return

        #Draw the main frame and save it as background
        background = self.DrawGraphMain(tempratures, dates, conditions)

        #Apply the Conditions to background
        self.DrawGraphConditionImages(background, conditions)

        #Save the result
        background.save(f"{self.DrawingBuiltImagesPath}/new.png", "PNG")


    def ValidateDataSets(self, tempratures, dates, conditions):
        try:
            if tempratures == False:
                print("Not enough data in WeatherData.json")
                return False
            if dates == False:
                print("Not enough data in WeatherData.json")
                return False
            if conditions == False:
                print("Not enough data in WeatherData.json")
                return False
        except(ValueError):
            pass
        return True

    def DrawGraphMain(self, tempratures, dates, conditions):
        #Draw all of the main graph features

        # Create an array 1 - 10, This will act as our x layer.
        dayNumber = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        #Smoothen the line, This makes it look alot more clean and user friendly
        xnew = np.linspace(dayNumber.min(), dayNumber.max(), 300)
        spl = make_interp_spline(dayNumber, tempratures, k=3)
        power_smooth = spl(xnew)
        plt.plot(xnew,power_smooth)

        #Set the x label and y label
        plt.xlabel('Day')
        plt.ylabel('Temprature')

        #This small method makes sure the x layer does not get condenced, it also rotates the labels
        plt.xticks(dayNumber, dates, rotation=45)

        #Adjust the graph frame
        plt.gcf().subplots_adjust(bottom=0.30)
        figure = plt.gcf()
        figure.set_size_inches(7.5, 3.5)
        ax = plt.gca()
        ax.set_ylim(bottom=0)

        #Add "Edinburgh" to the graph with the colour line
        ax.legend(['Edinburgh'])

        #Save our graph and paste it onto bg.png
        figure.savefig(f'{self.DrawingBuiltImagesPath}output.png', dpi=100, bbox_inches = "tight")
        background = Image.open(f"{self.DrawingBuiltImagesPath}bg.png")
        overlay = Image.open(f"{self.DrawingBuiltImagesPath}output.png")
        background = background.convert("RGBA")
        overlay = overlay.convert("RGBA")
        background.paste(overlay, (130, 20), overlay)

        return background


    def DrawGraphConditionImages(self, background, conditions):
        #Paste the condition (ie, rain, cloudy, Thunderstorms) to the graph with the correct spacing
        #The lack of a switch statement in python makes this a little less clean, So i opt for if elif
        for i in range(0, 10):
            conditionImage = Image.open(f"{self.DrawingConditionsPath}{conditions[i]}.png")
            conditionImage.thumbnail((64, 64))

            y = 340
            x = 178
            xDif = 60

            if i == 0:
                background.paste(conditionImage, (x, y), conditionImage)
            elif i == 1:
                background.paste(conditionImage, ((x + (i * xDif)), y), conditionImage)
            elif i == 2:
                background.paste(conditionImage, ((x + (i * xDif)), y), conditionImage)
            elif i == 3:
                background.paste(conditionImage, ((x + (i * xDif)), y), conditionImage)
            elif i == 4:
                background.paste(conditionImage, ((x + (i * xDif)), y), conditionImage)
            elif i == 5:
                background.paste(conditionImage, ((x + (i * xDif)), y), conditionImage)
            elif i == 6:
                background.paste(conditionImage, ((x + (i * xDif)), y), conditionImage)
            elif i == 7:
                background.paste(conditionImage, ((x + (i * xDif)), y), conditionImage)
            elif i == 8:
                background.paste(conditionImage, ((x + (i * xDif)), y), conditionImage)
            elif i == 9:
                background.paste(conditionImage, ((x + (i * xDif)), y), conditionImage)

        return background


Graph = Graph()
