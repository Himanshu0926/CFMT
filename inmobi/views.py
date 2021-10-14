# Custom created

from django.http import HttpResponse
from django.shortcuts import render
import pyrebase

config={
    "apiKey": "AIzaSyAktSHUf5vchzr63pT2r3EkCuGEXZPghe8",
    "authDomain": "inmobi-1a433.firebaseapp.com",
    "projectId": "inmobi-1a433",
    "storageBucket": "inmobi-1a433.appspot.com",
    "messagingSenderId": "164911697942",
    "appId": "1:164911697942:web:0757c8193d79410c5fa537",
    "databaseURL": "https://inmobi-1a433-default-rtdb.firebaseio.com"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
def index(request):
    var1 = database.child('Data').child('0').get().val()



    return render(request, 'index.html', {
        "fdate":var1
    })

def operations(request):
    return render(request, 'operations.html')