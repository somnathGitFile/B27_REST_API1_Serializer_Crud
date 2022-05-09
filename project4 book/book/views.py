from ast import Delete
from functools import partial
from django.shortcuts import render
from .models import Book
from rest_framework.views import APIView
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class BookView(APIView):
    def get(self, request):
        bk = Book.objects.all()
        serializer = BookSerializer(bk, many=True)
        return Response(serializer.data) 

    def post(self, request):
        serializer = BookSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class BookInfo(APIView):
    def get(self,request, id):
        try:
            bk=Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg ={'msg':'Record does not found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(bk)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        try:
            bk = Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg = {'msg':'Record does not found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(bk, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            bk = Book.objects.get(id=id)
        except Book.DoesNotExist:
            msg = {'msg':'Record does not Found'}
            return Response(msg)
        bk.delete()
        msg = {'msg':'Record deleted successfully'}
        
        return Response(msg, status=status.HTTP_410_GONE)

        
