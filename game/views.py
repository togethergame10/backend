from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from game.forms import GameCreationForm
from game.models import Game, Place, Situation, GameType, Like


# 게임 등록
from gameplaylist.models import GamePlaylist


class GameCreateView(CreateView):
    model = Game
    context_object_name = 'target_game'
    form_class = GameCreationForm
    template_name = 'game/create.html'

    def form_valid(self, form):
        temp_game = form.save(commit=False)
        temp_game.author = self.request.user
        temp_game.place = Place.objects.get(name=self.request.POST['place_str'])
        temp_game.situation = Situation.objects.get(name=self.request.POST['situation_str'])
        temp_game.save()
        game_type = self.request.POST.get('game_type_str')
        if game_type:
            tag_list = game_type.strip().replace(',', ';').split(';')
            for t in tag_list:
                t = t.strip()
                if t == '':
                    continue
                tag = GameType.objects.get(name=t)
                temp_game.game_type.add(tag)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('game:detail', kwargs={'pk':self.object.pk})

# 게임 수정
class GameUpdateView(UpdateView):
    model = Game
    context_object_name = 'target_game'
    form_class = GameCreationForm
    template_name = 'game/update.html'

    def form_valid(self, form):
        temp_game = form.save(commit=False)
        temp_game.place = Place.objects.get(name=self.request.POST['place_str'])
        temp_game.situation = Situation.objects.get(name=self.request.POST['situation_str'])
        temp_game.save()
        temp_game.game_type.clear()
        game_type = self.request.POST.get('game_type_str')
        if game_type:
            tag_list = game_type.strip().replace(',', ';').split(';')
            for t in tag_list:
                t = t.strip()
                if t == '':
                    continue
                tag = GameType.objects.get(name=t)
                temp_game.game_type.add(tag)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('game:detail', kwargs={'pk': self.object.pk})

# 게임 삭제
class GameDeleteView(DeleteView):
    model = Game
    context_object_name = 'target_game'
    success_url = reverse_lazy('game:list')
    template_name = 'game/delete.html'

# 게임 목록
class GameListView(ListView):
    model = Game
    context_object_name = 'game_list'
    template_name = 'game/list.html'
    paginate_by = 10
    ordering = '-pk'

# 게임 제목 검색
class GameSearchView(GameListView):
    paginate_by = None
    def get_queryset(self):
        q = self.kwargs['q']
        game_list = Game.objects.filter(Q(title__contains=q))#.order_by('-pk')
        game_list = game_list.order_by('-pk')
        return game_list

# 게임 필터 검색
class GameSearchFilter(GameListView):
    paginate_by = None
    def get_queryset(self):
        game_list = None
        q = Q()

        situation = self.request.GET.get('situation_str', False)
        if situation:
            q &= Q(situation_id=Situation.objects.get(name=situation).pk)

        place = self.request.GET.get('place_str', False)
        if place:
            q &= Q(place_id=Place.objects.get(name=place).pk)

        game_type = self.request.GET.get('game_type_str', False)
        if game_type:
            game_type = game_type.split(';')
            if '' in game_type:
                game_type.remove('')
            for i in range(len(game_type)):
               game_type[i] = GameType.objects.get(name=game_type[i])
            q &= Q(game_type__in=game_type)

        sort = self.request.GET.get('sort')
        if sort=="recent":
            game_list = Game.objects.filter(q).distinct().order_by('-pk')
        elif sort=="like":
            game_list = Game.objects.filter(q).distinct().annotate(like_count=Count('likes')).order_by('-like_count')
        return game_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameSearchFilter, self).get_context_data()
        context['place'] = self.request.GET.get('place_str', False)
        context['situation'] = self.request.GET.get('situation_str', False)
        context['game_type'] = self.request.GET.get('game_type_str', False)
        context['sort'] = self.request.GET.get('sort', False)
        return context

# 게임 상세
class GameDetailView(DetailView):
    model = Game
    context_object_name = 'target_game'
    template_name = 'game/detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameDetailView, self).get_context_data()
        if self.request.user.is_authenticated:
            game = Game.objects.get(pk=self.object.pk)
            liked_by_user = game.likes.filter(user=self.request.user).exists()
            context['is_like'] = liked_by_user

            context['gameplaylists'] = GamePlaylist.objects.filter(author=self.request.user)
            context['checked_gameplaylists'] = GamePlaylist.objects.filter(Q(author=self.request.user) & Q(games=game)).distinct()
        else:
            context['is_like'] = False
        return context


# 게임 좋아요 추가/삭제
def update_like(request):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'error': '로그인을 해주세요.'})
    else:
        game_pk = request.POST.get('game_id')
        try:
            game = Game.objects.get(pk=game_pk)
        except Game.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Post not found'})

        user_likes = Like.objects.filter(user=request.user, game=game)

        if user_likes.exists(): # 이미 좋아요를 누른 경우, 좋아요 삭제
            user_likes.delete()
            liked = False
        else:   # 좋아요 추가
            like = Like.objects.create(user=request.user)
            liked = True
            game.likes.add(like)  # 다대다 관계 필드에 사용자 추가

        like_count = game.likes.count()

        return JsonResponse({'success': True, 'liked': liked, 'like_count': like_count})