import requests, certifi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer

class PostListView(APIView):
    def get(self, request):
        response = requests.get('https://jsonplaceholder.typicode.com/posts', verify=certifi.where())
        if response.status_code == 200:
            dados = response.json()

            serializer = PostSerializer(data=dados, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Não foi possível obter os dados'}, status=status.HTTP_400_BAD_REQUEST)