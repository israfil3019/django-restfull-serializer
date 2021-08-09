from rest_framework import serializers
from .models import Student

class StudentDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    number = serializers.IntegerField()
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
            
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance