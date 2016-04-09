from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    if request.method == 'POST':
        response = JsonResponse({'edit_distance': 5})
        #return str(response.content, encoding='UTF-8')
        return response
    return render(request, 'home.html')
