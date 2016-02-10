from django.shortcuts import render
from django.http import JsonResponse
import json


def index(request):
    return render(request, 'index.html')


def ajax(request):
    b = json.loads(request.POST.get('data'))

    response = "the values are not equal"

    if b[0]['value'] == b[1]['value']:
        response = "The two values are equal"

    if b[0]['value'] > b[1]['value']:
        response = "The first value is greater than the second"

    if b[0]['value'] < b[1]['value']:
        response = "The second value is greater than the first"

    return JsonResponse({'response': response})
