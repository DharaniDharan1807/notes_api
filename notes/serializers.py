from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User

class NoteSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author', 'author_name', 'is_public']
        read_only_fields = ['author', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    notes_count = serializers.IntegerField(source='notes.count', read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'notes_count']