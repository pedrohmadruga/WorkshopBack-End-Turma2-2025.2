import requests, certifi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PostListView(APIView):
    def get(self, request):
        response = requests.get('https://jsonplaceholder.typicode.com/posts', verify=certifi.where())
        if response.status_code == 200:
            dados = response.json()
            return Response(dados, status=status.HTTP_200_OK)
        return Response({'error': 'Não foi possível obter os dados'}, status=status.HTTP_400_BAD_REQUEST)