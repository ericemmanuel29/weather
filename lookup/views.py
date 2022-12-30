from django.shortcuts import render

def home(request):
    import json
    import requests

    api_requests = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07621&distance=3&API_KEY=E78E0735-54F1-4DCD-B15D-5CC524B55DFD')
    
    try:
        api = json.loads(api_requests.content)
    except Exception as e:
        api = "Error..."
    
    if api[0]['Category']['Name'] == "Good":
        category_description = "Air quality is considered good good."
        category_color = 'good'
    elif api[0]['Category']['Name'] == "Moderate":
        category_description = "Air quality is considered aight."
        category_color = 'moderate'
    elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
        category_description = "Air quality is considered stay at home."
        category_color = 'usg'
    elif api[0]['Category']['Name'] == "Unhealthy":
        category_description = "Air quality is considered don't go outside."
        category_color = 'unhealthy'
    elif api[0]['Category']['Name'] == "Very Unhealthy":
        category_description = "Air quality is for real bro?"
        category_color = 'veryUnhealthy'
    elif api[0]['Category']['Name'] == "Hazardous":
        category_description = "Air quality is ayo."
        category_color = 'hazardous'

    return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

def about(request):
    import requests

    if request.method == "POST":
        originalText = request.POST['lisper']
        return render(request, 'about.html', {'originalText': originalText})
    else: #GET
        pass

    return render(request, 'about.html', {})
