import tweepy
import DataCollection.JsonHandler as JH
from pathlib import Path

class tokenvalidationerror(Exception):
    def __init__(self):
        self.error = "Critical Error, Failed to get request token."
    def __str__(self):
        return repr(self.error)

class OAuthMain():
    def __init__(self):
        current_path = Path(__file__).parents[1]
        self.pathtoimage = str(Path(current_path / 'Data/Drawing/BuiltImages/finaloutput.png'))

    def OAuthStart(self):
        """Start the authentication process"""
        #Get our auth using the tokens in config.json
        api = tweepy.API(self.GetAuth())

        #upload our image to twitter
        result = api.media_upload(self.pathtoimage)
        #create a blank list
        media_ids = []
        #append the media id of the image we uploaded to twitter to the blank list we created
        media_ids.append(result.media_id)
        #Add a status to twitter with the image attached
        api.update_status(status = 'Weather data for the last 10 days !', media_ids = media_ids)

    def GetAuth(self):
        """Responsible for getting authentication to the twitter servers"""
        auth = tweepy.OAuthHandler(JH.JsonHandler.RetriveTwitterApiKey(), JH.JsonHandler.RetriveTwitterSecretApiKey())
        auth.set_access_token(JH.JsonHandler.RetriveTwitterAccessToken(), JH.JsonHandler.RetriveTwitterSecretAccessToken())
        return auth

OAuthMain = OAuthMain()