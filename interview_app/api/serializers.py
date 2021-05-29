from rest_framework import serializers
from .models import Author, Quiz, Matter

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['id', 'name', 'added_by', 'created_date']

class QuizSerializer(serializers.ModelSerializer):
  class Meta:
    model = Quiz
    fields = ['id', 'title', 'description', 'author', 'matter', 'added_by', 'created_date']

class MatterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Matter
    fields = ['id', 'title', 'description', 'author', 'added_by', 'created_date']