from django.shortcuts import render
from .models import Announcement

def index(request):
     return render(request, 'components/index.html')

def announcement(request):
    announcements = Announcement.objects.all()
    return render(request, 'components/announcement.html', {'announcements': announcements})