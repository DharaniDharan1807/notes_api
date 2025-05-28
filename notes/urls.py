from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('notes/', views.NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('notes/public/', views.PublicNotesView.as_view(), name='public-notes'),
]