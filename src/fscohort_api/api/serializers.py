from rest_framework import serializers
from fscohort_api.models import Student, Room
from django.utils.timezone import now



class StudentSerializer(serializers.ModelSerializer):
    
    # student_room= RoomSerializer()
    # student_room = serializers.StringRelatedField() # problem about adding student with framework
    days_since_joined = serializers.SerializerMethodField()
    
    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['first_name', 'number']
        # exclude = ['number']
        # read_only_fields = ['id']

    def get_days_since_joined(self, obj):
        return (now() - obj.register_date).days

    def validate_first_name(self, value):  # field level
        if len(value) < 3:
            raise serializers.ValidationError("name sould be more then 3 char !")
        return value
    
class RoomSerializer(serializers.ModelSerializer):
    
    # students = StudentSerializer(many=True,read_only=True)
    students = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        lookup_field='id',
        view_name='detail',
    )
    class Meta:
        model = Room
        fields = '__all__'

# class StudentDefaultSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     number = serializers.IntegerField()
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
            
#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance

#     def validate(self,data):  # object level
#         if data['first_name'] == data['last_name']:
#             raise serializers.ValidationError("first name and last name must be different !")
        
#     def validate_first_name(self, value):  # field level
#         if len(value) < 3:
#             raise serializers.ValidationError("name sould be more then 3 char !")
#         return value