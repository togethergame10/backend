from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from game.forms import GameCreationForm
from game.models import Game, Place, Situation, RequiredTime, GameType


class GameCreateView(CreateView):
    model = Game
    context_object_name = 'target_game'
    form_class = GameCreationForm
    template_name = 'game/create.html'

    def form_valid(self, form):
        temp_game = form.save(commit=False)
        temp_game.author = self.request.user
        temp_game.place = Place.objects.get(name=self.request.POST['places_str'])
        temp_game.situation = Situation.objects.get(name=self.request.POST['situation_str'])
        temp_game.save()
        # 태그들 처리
        arr = [0, 0]
        arr[0] = self.request.POST.get('requiredTime_str')
        arr[1] = self.request.POST.get('gameType_str')
        for i in range(len(arr)):
            if arr[i]:
                tag_list = arr[i].strip().replace(',', ';').split(';')
                for t in tag_list:
                    t = t.strip()
                    if t == '':
                        continue
                    if i == 0:
                        tag = RequiredTime.objects.get(name=t)
                        temp_game.requiredTime.add(tag)
                    elif i == 1:
                        tag = GameType.objects.get(name=t)
                        temp_game.gameType.add(tag)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('game:detail', kwargs={'pk':self.object.pk})


class GameUpdateView(UpdateView):
    model = Game
    context_object_name = 'target_game'
    form_class = GameCreationForm
    template_name = 'game/update.html'
    # 수정 폼에 기존 태그들 볼 수 있게 해놔야....

    def get_success_url(self):
        return reverse('game:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        response = super(GameUpdateView, self).form_valid(form)
        self.object.requiredTime.clear()
        self.object.gameType.clear()
        # 태그들 처리
        arr = [0, 0]
        arr[0] = self.request.POST.get('requiredTime_str')
        arr[1] = self.request.POST.get('gameType_str')
        for i in range(len(arr)):
            if arr[i]:
                tag_list = arr[i].strip().replace(',', ';').split(';')
                for t in tag_list:
                    t = t.strip()
                    if t == '':
                        continue
                    if i == 0:
                        tag = RequiredTime.objects.get(name=t)
                        self.object.requiredTime.add(tag)
                    elif i == 1:
                        tag = GameType.objects.get(name=t)
                        self.object.gameType.add(tag)
        return response

class GameDeleteView(DeleteView):
    model = Game
    context_object_name = 'target_game'
    success_url = reverse_lazy('game:list')
    template_name = 'game/delete.html'

class GameListView(ListView):
    model = Game
    context_object_name = 'game_list'
    template_name = 'game/list.html'
    paginate_by = 10
    ordering = '-pk'

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'target_game'
    template_name = 'game/detail.html'

