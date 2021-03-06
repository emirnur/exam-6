"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import index_view, hostbook_create_view, hostbook_update_view, hostbook_delete_view, search_by_name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('host/add/', hostbook_create_view, name='hostbook_add'),
    path('host/<int:pk>/update', hostbook_update_view, name='hostbook_update'),
    path('host/<int:pk>/delete', hostbook_delete_view, name='hostbook_delete'),
    path('search/', search_by_name, name='search_by_name')
]
