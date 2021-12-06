from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated


class Checkauth(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'key': 'Hi'})
