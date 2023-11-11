from datetime import datetime, timedelta

from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from game.models import Game, Situation

situations_str = ['술게임', 'MT']

def mainPage(request):
    one_month_ago = datetime.now() - timedelta(days=30)
    liked_ranking = Game.objects.filter(likes__created_at__gte=one_month_ago) \
                    .annotate(like_count=Count('likes')).order_by('-like_count')[:4]

    situations_list = []
    for s in situations_str:
        list = Game.objects.filter(situation_id=Situation.objects.get(name=s).pk) \
                .annotate(like_count=Count('likes')).order_by('-like_count')[:4]
        situations_list.append(list)

    return render(request, 'single_pages/main.html', {
        'liked_ranking': liked_ranking,
        'situation_ranking1': situations_list[0],
        'situation_ranking2': situations_list[1],
        'list': situations_str
    })

def LikedRankingPage(request):
    one_month_ago = datetime.now() - timedelta(days=30)
    liked_ranking = Game.objects.filter(likes__created_at__gte=one_month_ago) \
                    .annotate(like_count=Count('likes')).order_by('-like_count')[:10]
    return render(request, 'single_pages/ranking.html', {
        'title': '좋아요 랭킹',
        'liked_ranking': liked_ranking,
    })

def SituationRankingPage(request, pk):
    situation_ranking = Game.objects.filter(situation_id=Situation.objects.get(name=situations_str[pk]).pk) \
                    .annotate(like_count=Count('likes')).order_by('-like_count')[:10]
    return render(request, 'single_pages/ranking.html', {
        'title': '상황별 랭킹',
        'situation': situations_str[pk],
        'situation_ranking': situation_ranking,
    })
