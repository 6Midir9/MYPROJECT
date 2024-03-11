from django.shortcuts import render, redirect
from .models import Announcement
from .forms import AnnounForm

def index(request):
     return render(request, 'components/index.html')

def announcement(request):
    announcements = Announcement.objects.all()
    return render(request, 'components/announcement.html', {'announcements': announcements})

def new_announ(request):
    form = AnnounForm(data=request.POST)

    if request.method == 'POST':
        form = AnnounForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('components:announcement')

    context = {'form': form}
    return render(request, 'components/new_announ.html', context)

def edit_announ(request, announcement_id):
     announcement = Announcement.objects.get(id=announcement_id)
     if request.method != 'POST':
          form = AnnounForm(instance=announcement)
     else: 
          form = AnnounForm(instance=announcement, data=request.POST)
          if form.is_valid():
             form.save()
             return redirect('components:announcement')
        
     context = {'announcement' : announcement, 'form': form}
     return render(request, 'components/edit_announ.html', context)

def delete_announ(request, announcement_id):
    announcement = Announcement.objects.get(pk=announcement_id)
    if request.method == 'POST':
        announcement.delete()
        return redirect('components:announcement')
    
    context = {'announcement' : announcement}
    return render(request, 'components/delete_announ.html', context)