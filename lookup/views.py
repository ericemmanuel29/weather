from django.shortcuts import render

def home(request):
    import json
    import requests

    api_requests = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07621&distance=3&API_KEY=E78E0735-54F1-4DCD-B15D-5CC524B55DFD')
    
    try:
        api = json.loads(api_requests.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
