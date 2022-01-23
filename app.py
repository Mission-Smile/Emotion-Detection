from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}


api.add_resource(HelloWorld, "/helloWorld")

recom_sad = ["Go and take a break!", 
            "Watch this video on Youtube: https://youtu.be/0Bmhjf0rKe8", 
            "Watch this video on Youtube: https://youtu.be/pNtNxMt_b7I",
            "Listen to some music: https://open.spotify.com/playlist/2RafGqDeCijhZjctf8brvD?si=92bd36e8f04b4e89",
            "Eat a snack"]
recom_happy = ["Write down the reason", 
                "Some music for you: https://open.spotify.com/playlist/2RafGqDeCijhZjctf8brvD?si=92bd36e8f04b4e89"]
recom_angry = ["Watch this video: https://youtu.be/hbH53mfC24c", 
                "Let's do this workout: https://www.tk.de/techniker/magazin/sport/spezial/gesunder-ruecken/trainingsflaeche-buero/8-minuten-workout-fuers-buero-2009264", 
                "Calm down and do some exercise https://youtu.be/bnoZko9hfzo 3"]
recom_neutral = ["Here is some music for your concentration https://open.spotify.com/playlist/37i9dQZF1DWSsWHHnufwMM?si=9adc0496125f45cd"]
recom_fear = ["Take a break and talk with a friend about your fear",
                "Take a break and find a game to distract you on this website: http://www.xn--langeweile-im-bro-h3b.de/buerospiele/"]
recom_surprise= ["Write down the reason"]
recom_disgust= ["Some exercise will be good for you: https://www.youtube.com/watch?v=sk0gL4WSmPU",
                "Listen to some music https://open.spotify.com/playlist/5wPDEfZJzo7lpRYMWDBIyB?si=11c477dd36514bb4"]


class Emotion(Resource):
    def get(self, emotion):
        if emotion == "happy":
            return {"answer": random.choice(recom_happy)}
        if emotion == "sad":
            return {"answer": random.choice(recom_sad)}
        if emotion == "angry":
            return {"answer": random.choice(recom_angry)}
        if emotion == "neutral":
            return {"answer": random.choice(recom_neutral)}
        if emotion == "fear":
            return {"answer": random.choice(recom_fear)}
        if emotion == "surprise":
            return {"answer": random.choice(recom_surprise)}
        if emotion == "disgust":
            return {"answer": random.choice(recom_disgust)}

api.add_resource(Emotion, "/recom/<string:emotion>")

if __name__ == "__main__":
    app.run(debug=True)
