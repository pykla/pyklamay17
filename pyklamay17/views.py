import requests
from django.shortcuts import render


def numberView(request, number):
    r = requests.get('http://numbersapi.com/{}?json'.format(number))
    print(r.json())
    number_json = r.json()
    return render(request, 'index.html', {"number": number_json})
