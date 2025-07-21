from rest_framework import serializers
from .models import Student
from django.contrib.auth import authenticate


class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ['reg_number', 'full_name', 'institution_code', 'password']

    def create(self, validated_data):
        return Student.objects.create_user(**validated_data)




class StudentLoginSerializer(serializers.Serializer):
    reg_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(reg_number=data['reg_number'], password=data['password'])
        if user:
            return {'reg_number': user.reg_number, 'full_name': user.full_name}
        raise serializers.ValidationError("Invalid registration number or password")