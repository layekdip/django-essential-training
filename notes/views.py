from .forms import NotesForm
from .models import Notes
from django.views.generic import CreateView, ListView, DetailView, UpdateView

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'

class NoteDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/notes_details.html'

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gte = 1)

