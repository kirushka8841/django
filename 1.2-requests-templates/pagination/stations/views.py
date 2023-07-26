from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from django.conf import settings


def get_data():
    bus_stat = []
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            bus_stat.append(row)
    return bus_stat

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stat = get_data()
    paginator = Paginator(bus_stat, 10)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    
    context = {
        'page': page,
        'bus_stations': page.object_list
    }
    return render(request, 'stations/index.html', context)
