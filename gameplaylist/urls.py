from django.urls import path

from game.views import GameCreateView, GameUpdateView, GameDetailView, GameDeleteView, GameListView, GameSearchView, \
    update_like

from game.views import GameSearchFilter
from gameplaylist.views import GamePlaylistCreateView, deleteGameplaylist, GamePlaylistListView, GamePlaylistDetailView

app_name='gameplaylist'

urlpatterns = [
    path('create/', GamePlaylistCreateView.as_view(), name='create'),
    # path('update/<int:pk>/', GameUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', GamePlaylistDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', deleteGameplaylist, name='delete'),
    #
    path('list/', GamePlaylistListView.as_view(), name='list'),

]
