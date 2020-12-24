from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from django.views.decorators.csrf import csrf_exempt
import requests as req
from main.dictionaries import *
from main.location import location, weatherforecast
from main.stockexchange import news

# Create your views here.

def treament(string, state):
    state = eval(state + "()")
    for key, value in state.items():
        if key in string:
            string = string.replace(key, value)
    return string

def british_to_american(string):
    b_dict = british_dict()
    for key, value in b_dict.items():
        if value in string:
            string = string.replace(value, key)
    return string

def index(request):
    """ index view """
    t = loader.get_template('index.html')
    forecast = weatherforecast()
    print(british_to_american("aerogramme voila"))
    #the_news = news()
    if request.method == 'POST':
        user_input = request.POST.get('inputValue')
        us_state = request.POST.get('us-state').lower()
        demonym = request.POST.get('demonym').lower()
        print(demonym)
        print(user_input, " ", us_state)
        r = british_to_american(user_input)
        result = r
        result = treament(result, us_state)
        return HttpResponse(result)
    data = {
        "forecast" : forecast["weather"][0]["main"],
        "wind" : round(forecast["wind"]["speed"] * 3.6), 
        "temperature" : round(forecast["main"]["temp"] - 273.15),
        "humidity" : forecast["main"]["humidity"],
        "city" : forecast["name"],
        "country" : forecast["sys"]["country"],
        #"the_news" : the_news
    }
    return HttpResponse(t.render(data, request=request))