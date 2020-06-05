from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirectMain),
    path('shows/', views.showList),
    path('shows/new/', views.showAdd),
    path('shows/new/create/', views.createShow),
    path('shows/<int:showid>/', views.showDetails),
    path('shows/<int:showid>/edit/', views.showEdit),
    path('shows/<int:showid>/alterShow/', views.alterShow),
    path('shows/<int:showid>/deleteShow/', views.deleteShow),
]