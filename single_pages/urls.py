from django.urls import path

from game.views import GameCreateView, GameUpdateView, GameDetailView, GameDeleteView, GameListView, GameSearchView, \
    update_like

from game.views import GameSearchFilter

app_name='page'

urlpatterns = [
    # path('', mainPage, name='main'),
    # path('mypage/<int:pk>/', myPage, name='mypage'),

]
