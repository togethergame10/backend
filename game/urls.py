from django.urls import path

from game.views import GameCreateView, GameUpdateView, GameDetailView, GameDeleteView, GameListView, GameSearchView, \
    update_like

from game.views import GameSearchFilter

app_name='game'

urlpatterns = [
    path('create/', GameCreateView.as_view(), name='create'),
    path('update/<int:pk>/', GameUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', GameDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', GameDeleteView.as_view(), name='delete'),

    path('list/', GameListView.as_view(), name='list'),
    path('search/', GameSearchFilter.as_view(), name='search_filter'),
    path('search/<str:q>/', GameSearchView.as_view(), name='search'),
    path('like/', update_like, name='like')\

]
