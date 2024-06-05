# import viewsets
from django.http import HttpResponse
from django.views import View
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView

import requests

class Users(APIView):
    def get(self, request):
        """
        Retrieves a list of random users from an external API.
        Args:
            request: The HTTP request object.

        Returns:
            An HTTP response containing the retrieved user data in JSON format.
        """
        count = 5
        response = requests.get('https://randomuser.me/api/?results=' + str(count))

        r = response.json()
        users = r['results']
        #check if id value is None
        for user in users:
            d = user['id']
            v = d['value']
            if v is None:
                user['id']['value'] = 'None'
        return HttpResponse(response, content_type="application/json")
