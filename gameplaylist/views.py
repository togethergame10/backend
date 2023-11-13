from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from gameplaylist.forms import GamePlaylistCreationForm
from gameplaylist.models import GamePlaylist


## 게임플리 추가
class GamePlaylistCreateView(CreateView):
    model = GamePlaylist
    context_object_name = 'target_gameplaylist'
    form_class = GamePlaylistCreationForm
    template_name = 'gameplaylist/create.html'

    def form_valid(self, form):
        temp_gameplaylist = form.save(commit=False)
        temp_gameplaylist.author = self.request.user
        form.save(commit=True)
        temp_gameplaylist.collectors.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('page:mypage', kwargs={'pk':self.request.user.pk})

## 게임플리 삭제
def deleteGameplaylist(request, pk):
    if request.user.is_authenticated:
        gameplaylist = GamePlaylist.objects.get(pk=pk)
        if request.user == gameplaylist.author:
            gameplaylist.delete()
        return redirect('page:mypage', pk=request.user.pk)

## 게임플리 목록
class GamePlaylistListView(ListView):
    model = GamePlaylist
    context_object_name = 'gameplaylist_list'
    template_name = 'gameplaylist/list.html'
    ordering = '-pk'

## 게임플리 상세
class GamePlaylistDetailView(DetailView):
    model = GamePlaylist
    context_object_name = 'target_gameplaylist'
    template_name = 'gameplaylist/detail.html'

    def get_context_data(self, **kwargs):
        context = super(GamePlaylistDetailView, self).get_context_data()
        context['games'] = self.object.games.all()
        return context
