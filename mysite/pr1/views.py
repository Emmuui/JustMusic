from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import *


def index(request):
    context = {
        'last_musics': sorted(Music.objects.all(),
                              key=lambda x: -x.id)[:6],
        'authors': Author.objects.order_by('-id')[:6],
    }
    return render(request, 'pr1/index.html', context)

class MusicDetailView(DetailView):
    model = Music

class MusicListView(ListView):
    model = Music

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author
    model1 = Music

def search(request):
    search = request.POST.get('search')
    if search:
        musics = [music for music in Music.objects.all() if search.lower()
                  in music.title.lower()]
        authors = [author for author in Author.objects.all() if search.lower()
                  in author.pseudonym.lower()]
        context = {
            'search': search,
            'musics': musics,
            'authors': authors,

        }
        return render(request, 'pr1/search.html', context)
    else:
        return redirect(reverse('pr1:index'))