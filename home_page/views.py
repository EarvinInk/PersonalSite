from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ContactSerializer


class Contacts(APIView):
    def get(self, request,format=None):
        data = {
            "name": "Kevin Nair",
            "email": "kevin@gmail.in",
            "contact_no": "9999999999"
        }
        # serializer = ContactSerializer(data=data)
        return Response(data)
