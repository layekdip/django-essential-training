from jupyter_client.localinterfaces import is_public_ip

from .forms import NotesForm
from .models import Notes
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

def add_like_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk = pk)
        note.likes += 1
        note.save()
        return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))
    raise Http404

def change_visibility_view(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk = pk)
        note.is_public = not note.is_public
        note.save()
        return HttpResponseRedirect(reverse("notes.detail", args=(pk,)))
    raise Http404

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/notes_details.html'

class NotePublicDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    queryset = Notes.objects.filter(is_public=True)
    template_name = 'notes/notes_details.html'

class PopularNotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gte = 1)

