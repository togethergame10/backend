from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.edit import FormMixin

from game.models import Game
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
        return reverse('gameplaylist:list')

## 게임플리 삭제
def deleteGameplaylist(request, pk):
    if request.user.is_authenticated:
        gameplaylist = GamePlaylist.objects.get(pk=pk)
        if request.user == gameplaylist.author:
            gameplaylist.delete()
        return redirect('page:mypage', pk=request.user.pk)

## 게임플리 목록
class GamePlaylistListView(ListView, FormMixin):
    model = GamePlaylist
    context_object_name = 'gameplaylist_list'
    template_name = 'gameplaylist/list.html'
    ordering = '-pk'

    form_class = GamePlaylistCreationForm

    def form_valid(self, form):
        temp_gameplaylist = form.save(commit=False)
        temp_gameplaylist.author = self.request.user
        form.save(commit=True)
        temp_gameplaylist.collectors.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('page:mypage', kwargs={'pk':self.request.user.pk})

## 게임플리 상세
class GamePlaylistDetailView(DetailView):
    model = GamePlaylist
    context_object_name = 'target_gameplaylist'
    template_name = 'gameplaylist/detail.html'

    def get_context_data(self, **kwargs):
        context = super(GamePlaylistDetailView, self).get_context_data()
        context['games'] = self.object.games.all()
        return context

## 게임플리에 게임 추가/삭제
def addOrRemoveGame(request):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': '로그인을 해주세요.'})
    else:
        gameplaylist = GamePlaylist.objects.get(pk=request.POST.get('gameplaylist_id'))
        game = Game.objects.get(pk=request.POST.get('game_id'))
        if game in gameplaylist.games.all():
            gameplaylist.games.remove(game)
            collected = False
        else:
            gameplaylist.games.add(game)
            collected = True
        return  JsonResponse({'success': True, 'collected': collected})


## 게임플리 속 게임 삭제
def removeGame(request, pk1, pk2):
    if request.user.is_authenticated:
        gamelist = get_object_or_404(GamePlaylist, pk=pk1)
        game = get_object_or_404(Game, pk=pk2)

        if game in gamelist.games.all():
            gamelist.games.remove(game)
    return redirect('gameplaylist:detail', pk=pk1)
