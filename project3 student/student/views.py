from .models import Student
from rest_framework.views import APIView
from student.serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StudentDetails(APIView):
    def get (self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class StudentInfo(APIView):
    def get(self, request, id):
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            msg = {'msg':'Record Does Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            emp = Student.objects.get(id=id)
        except Student.DoesNotExist:
            msg = {'msg':'Record Does Not Found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(emp,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            msg = {'msg':'Record Does Not Found'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id):
        stu = Student.objects.get(id=id) 
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



