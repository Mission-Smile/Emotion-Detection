from flask import Flask
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}


api.add_resource(HelloWorld, "/helloWorld")

recom_sad = ["Go and take a break!", "Watch this video on Youtube: https://youtu.be/0Bmhjf0rKe8", "Watch this video on Youtube: https://youtu.be/pNtNxMt_b7I"]
recom_happy = ["Write down the reason", "recommendation happy 2", "recommendation happy 3"]
recom_angry = ["Watch this video: https://youtu.be/hbH53mfC24c", "Let's do this workout: https://www.tk.de/techniker/magazin/sport/spezial/gesunder-ruecken/trainingsflaeche-buero/8-minuten-workout-fuers-buero-2009264", "recommendation angry 3"]
recom_confused= []
recom_disgusted= []
recom_suprised= []
recom_calm = []
recom_unknown= []
recom_fear= []

class Emotion(Resource):
    def get(self, emotion):
        if emotion == "happy":
            return {"answer": random.choice(recom_happy)}
        if emotion == "sad":
            return {"answer": random.choice(recom_sad)}
        if emotion == "angry":
            return {"answer": random.choice(recom_angry)}
        if emotion == "confused":
            return {"answer": random.choice(recom_confused)}
        if emotion == "disgusted":
            return {"answer": random.choice(recom_disgusted)}
        if emotion == "suprised":
            return {"answer": random.choice(recom_suprised)}
        if emotion == "calm":
            return {"answer": random.choice(recom_calm)}
        if emotion == "unknown":
            return {"answer": random.choice(recom_unknown)}     
        if emotion == "fear":
            return {"answer": random.choice(recom_fear)}

api.add_resource(Emotion, "/recom/<string:emotion>")

if __name__ == "__main__":
    app.run(debug=True)
