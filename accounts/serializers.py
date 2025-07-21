from rest_framework import serializers
from .models import Student

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
        reg_number = data.get('reg_number')
        password = data.get('password')

        student = Student.objects.filter(reg_number=reg_number).first()
        if student is None:
            raise serializers.ValidationError("Invalid registration number")

        if not student.check_password(password):
            raise serializers.ValidationError("Incorrect password")

        return {
            'reg_number': student.reg_number,
            'full_name': student.full_name,
            'institution_code': student.institution_code,
        }