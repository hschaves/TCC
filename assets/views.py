from django.shortcuts import render, redirect, get_object_or_404
from .models import Notebook
from .forms import NotebookForm

def list_notebooks(request):
    notebooks = Notebook.objects.all()
    return render(request, 'assets/list_notebooks.html', {'notebooks': notebooks})

def add_notebook(request):
    if request.method == 'POST':
        form = NotebookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_notebooks')
    else:
        form = NotebookForm()
    return render(request, 'assets/add_notebook.html', {'form': form})

def edit_notebook(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    if request.method == 'POST':
        form = NotebookForm(request.POST, instance=notebook)
        if form.is_valid():
            form.save()
            return redirect('list_notebooks')
    else:
        form = NotebookForm(instance=notebook)
    return render(request, 'assets/edit_notebook.html', {'form': form})

def delete_notebook(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    if request.method == 'POST':
        notebook.delete()
        return redirect('list_notebooks')
    return render(request, 'assets/delete_notebook.html', {'notebook': notebook})
    
def index_view(request):
    notebooks = Notebook.objects.all()
    return render(request, 'assets/list_notebooks.html', {'notebooks': notebooks})
