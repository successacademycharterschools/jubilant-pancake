from django.conf.urls import url, include
from rest_framework import routers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

class calcDistance(APIView):

    def get(self, request, format=None):
        return Response('ok')

    def post(self, request, pk, format=None):
        collection = self.get_object(pk)

        return Response('ok')
