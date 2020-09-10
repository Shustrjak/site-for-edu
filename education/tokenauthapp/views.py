from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AuthView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data = {"message": "TEXT"}
        return Response(data)




