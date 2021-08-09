from django.shortcuts import render, get_object_or_404
from fscohort_api.models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from rest_framework import status
from fscohort_api.models import Student, Room
from .serializers import StudentSerializer, RoomSerializer

@api_view(["GET","POST"])
def room_list_crate_api(request):
    
    if request.method == "GET":
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True,context={'request': request}) # birden fazla obje döndügü için. yoksa hata verir.
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Room created successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","POST"])
def student_list_crate_api(request):
    
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True) # birden fazla obje döndügü için. yoksa hata verir.
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Student created successfully"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(["GET", "PUT", "DELETE"])
def student_get_update_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "GET" :
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": "Student updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)