from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CreateNote
from django.contrib import messages
from .models import Note, Tag
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



""" 
welcome view
home page
notespage
a note page
new notes
update notes
delete notes


islamlife,n

"""


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/home.html'
    context_object_name = 'notes'


    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return redirect('guest_home')
        return Note.objects.filter(user=self.request.user).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['has_notes'] = Note.objects.filter(user=user).exists()
        return context

class CatagoryNoteListView(LoginRequiredMixin, ListView):
    template_name = 'notes/catagory.html'
    context_object_name = 'tags'

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Note.objects.filter(tags=tag).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['has_notes'] = Note.objects.filter(user=user).exists()
        return context

    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        tags = self.get_queryset()
        context['tags'] = tags 

        return context

class NotesDetailView(LoginRequiredMixin, DetailView):
    model = Note

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'content', 'tags']
    def form_valid(self, form):
        form.instance.user = self.request.user
        note = form.save(commit=False)
    
        note.save()
        form.save_m2m()

        tags = form.cleaned_data['tags']
        note.tags.set(tags)

        return super().form_valid(form)

   

    def test_func(self):
        note = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'content', 'tags']

    def form_valid(self, form):
        form.instance.user =self.request.user
        form.save(commit=False)
        form.save_m2m()
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True

        return False


class NotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.user:
            return True

        return False



# def catagory_view(request, tag):
#     notes = Note.objects.filter(tags__slug=tag)
#     return render(request, 'notes/home.html', {'notes' : notes})