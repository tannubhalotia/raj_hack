from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.http import Http404
from .models import Table1
from .serializers import Table1Serializer
from .models import Table2
from .serializers import Table2Serializer

class Table1View(APIView):
    def get(self,request,format=None):
        data = Table1.objects.all()
        serializer = Table1Serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Table1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, format=None): 
        data = Table1.objects.all().delete()
        if data.is_valid():
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class Table2View(APIView):
    def get(self, request, format=None):
        data = Table2.objects.all()
        serializer = Table2Serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Table2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):  
        data = Table2.objects.all().delete()
        if data.is_valid():
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Table3View(APIView):
    def get(self, request, format=None):
        data = Table3.objects.all()
        serializer = Table3Serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Table3Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):  
        data = Table3.objects.all()
        if data.is_valid():
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)




	
