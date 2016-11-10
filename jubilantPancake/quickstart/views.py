from django.conf.urls import url, include
from rest_framework import routers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from bs4 import BeautifulSoup
import json

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
def distance(firstString, secondString):
    if len(secondString) > len(firstString):
        return distance(secondString, firstString)
    if len(secondString) == 0:
        return len(firstString)
    return min(distance(firstString[1:], secondString[1:])+(firstString[0] != secondString[0]), distance(firstString[1:], secondString)+1, distance(firstString, secondString[1:])+1)

class calcDistance(APIView):

    def post(self, request, format=None):
        inputStrings = BeautifulSoup(request.body, "html.parser")
        inputStrings = json.loads(str(inputStrings))

        return Response(distance(inputStrings['firstString'], inputStrings['secondString']))
