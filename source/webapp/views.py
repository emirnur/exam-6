from webapp.models import HostBook, STATUS_CHOICES
from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import HostBookForm


def index_view(request, *args, **kwargs):
    hosts = HostBook.objects.filter(status='active').order_by('created_at')
    return render(request, 'index.html', context={
        'hosts': hosts
    })

def hostbook_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = HostBookForm()
        return render(request, 'hostbook_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = HostBookForm(data=request.POST)
        if form.is_valid():
            tracker = HostBook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'],
            )
            return redirect('index')
        else:
            return render(request, 'hostbook_create.html', context={
                'form': form
            })

def hostbook_update_view(request, pk):
    host = get_object_or_404(HostBook, pk=pk)
    if request.method == 'GET':
        form = HostBookForm(data={
            'name': host.name,
            'email': host.email,
            'text': host.text,
        })
        return render(request, 'update.html', context={'form': form, 'host': host})
    elif request.method == 'POST':
        form = HostBookForm(data=request.POST)
        if form.is_valid():
            host.name = form.cleaned_data['name']
            host.email = form.cleaned_data['email']
            host.text = form.cleaned_data['text']
            host.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form, 'host': host})

def hostbook_delete_view(request, pk):
    host = get_object_or_404(HostBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'host': host})
    elif request.method == 'POST':
        host.delete()
        return redirect('index')

