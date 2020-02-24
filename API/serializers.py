from classes.models import Classroom
from rest_framework import serializers

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'name', 'year', 'teacher', 'id']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'year', 'teacher', 'id']

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'year', 'name']

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        exclude = ['teacher']
