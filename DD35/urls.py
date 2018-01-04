from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:perso_id>/', views.perso, name='perso'),
    path('<int:perso_id>/itemInv/', views.results, name='results'),
    path('<int:perso_id>/spellInv/', views.vote, name='vote'),
]