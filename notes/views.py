from django.shortcuts import render
from .models import Notes
from django.http import Http404

# Create your views here.
def list_notes(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def note_details(request, search_key):
    try:
        note = Notes.objects.get(pk = search_key)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist....")
    return render(request, 'notes/notes_details.html', {'note': note})