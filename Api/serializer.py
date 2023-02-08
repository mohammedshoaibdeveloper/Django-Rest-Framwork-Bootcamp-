from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['id']
        # fields = ['id']

    def validate(self,data):

        # if "age" in data:

        if data['age'] < 18:
            raise serializers.ValidationError({'error': 'age cannot be less than 18'})

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError({'error': 'name cannot be numeric'})

        return data


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    class Meta: 
        model = Book
        fields = '__all__'
        # depth = 1
        