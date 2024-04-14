from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Computer, Monitor
from django.urls import reverse


def index(request):
    categories = Category.objects.all()
    return render(request, 'marketplace/categories.html', {'categories': categories})


def all_computers(request):
    computers = Computer.objects.all()
    return render(request, 'marketplace/computers.html', {'computers': computers})


def all_monitors(request):
    monitors = Monitor.objects.all()
    return render(request, 'marketplace/monitors.html', {'monitors': monitors})


def single_computer(request, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    return render(request, 'marketplace/single_computer.html', {'computer': computer})


def single_monitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, pk=monitor_id)
    return render(request, 'marketplace/single_monitor.html', {'monitor': monitor})
