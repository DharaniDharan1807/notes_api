from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Note
from .serializers import NoteSerializer, UserSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(author=self.request.user)
        return Note.objects.filter(is_public=True)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(author=self.request.user)
        return Note.objects.filter(is_public=True)

class PublicNotesView(generics.ListAPIView):
    queryset = Note.objects.filter(is_public=True)
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def api_overview(request):
    api_urls = {
        'API Overview': '/api/',
        'All Public Notes': '/api/notes/public/',
        'My Notes (auth required)': '/api/notes/',
        'Create Note (auth required)': '/api/notes/',
        'Note Detail': '/api/notes/<int:pk>/',
        'Admin': '/admin/',
    }
    return Response(api_urls)