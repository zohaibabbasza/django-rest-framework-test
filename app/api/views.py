from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from app.models import User
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET', 'POST'])
def user_api(request):
    if request.method == 'GET':
        qs = User.objects.all()
        serializer = UserSerializer(qs, many=True)
        return Response({'data':serializer.data})
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
