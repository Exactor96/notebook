from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteCreateForm

def notes_list_index(request):
    notes = Note.objects.all()
    context={'notes':notes}
    return render(request,'note/index.html',context=context)


def add_note(request):
    if request.method == "GET":
        form = NoteCreateForm()
        return render(request,'note/add.html',{'form':form})
    if request.method == "POST":
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            note = form.save()
        else:
            return '<h1>Error with form</h1>'
        return redirect(f'/detail/{note.id}')


def detail_note(request,id):
    note = get_object_or_404(Note, id=id)
    return render(request,'note/detail.html', {'note':note})
