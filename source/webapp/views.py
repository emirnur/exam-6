from webapp.models import HostBook, STATUS_CHOICES
from django.shortcuts import render, get_object_or_404, redirect


def index_view(request, *args, **kwargs):
    hosts = HostBook.objects.filter(status='active').order_by('created_at')
    return render(request, 'index.html', context={
        'hosts': hosts
    })
