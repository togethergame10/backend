from django.urls import path

from single_pages.views import mainPage, LikedRankingPage, SituationRankingPage, myPage

app_name='page'

urlpatterns = [
    path('', mainPage, name='main'),
    path('ranking/liked/', LikedRankingPage, name='likedRanking'),
    path('ranking/situation/<int:pk>', SituationRankingPage, name='situationRanking'),
    path('mypage/<int:pk>/', myPage, name='mypage'),

]
