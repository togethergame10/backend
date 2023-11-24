from django.urls import path


from gameplaylist.views import GamePlaylistCreateView, deleteGameplaylist, GamePlaylistListView, GamePlaylistDetailView, \
    addOrRemoveGame, removeGame

app_name='gameplaylist'

urlpatterns = [
    path('create/', GamePlaylistCreateView.as_view(), name='create'),
    # path('update/<int:pk>/', GameUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', GamePlaylistDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/delete/', deleteGameplaylist, name='delete'),
    path('list/delete/<int:pk>/', deleteGameplaylist, name='delete'),
    path('list/', GamePlaylistListView.as_view(), name='list'),

    path('add_or_remove_game/', addOrRemoveGame, name='add_or_remove_game'),
    path('detail/<int:pk1>/remove_game/<int:pk2>/', removeGame, name='remove_game'),

]
