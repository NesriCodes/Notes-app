from django.urls import path
from .views import NotesListView, NotesDetailView, NotesCreateView, NotesUpdateView, NotesDeleteView, CatagoryNoteListView

urlpatterns = [
	path('', NotesListView.as_view(), name='home'),
	path('note/<int:pk>', NotesDetailView.as_view(), name='notes-detail'),
	path('note/create', NotesCreateView.as_view(), name='notes-create'),
	path('note/<int:pk>/update', NotesUpdateView.as_view(), name='notes-update'),
	path('note/<int:pk>/delete', NotesDeleteView.as_view(), name='notes-delete'),
	path('catagory/<slug:slug>/', CatagoryNoteListView.as_view(), name='catagory')
]