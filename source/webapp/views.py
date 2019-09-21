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
