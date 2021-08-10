from django.db import models


class Room(models.Model):
    room_name = models.CharField(max_length=20)
    room_no = models.IntegerField()


    def __str__(self):
        return self.room_name
    
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField()
    register_date = models.DateTimeField(auto_now_add=True)
    student_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='students')
    
    
    
    def __str__(self):
        return self.first_name
    
    
    
