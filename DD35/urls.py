from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # url(r'^armors/$', views.armors_list),
    # url(r'^armors/(?P<pk>[0-9]+)/$', views.armors_detail),

    url(r'^armors/$', views.armors_list.as_view(), name='armors'),
    url(r'^armors/(?P<pk>[0-9]+)/$', views.armors_detail.as_view(), name='armorDetail'),


    path('', views.index_list, name='index'),
    path('charac/<int:charac_id>/', views.character_detail, name='perso'),
    path('<int:perso_id>/itemInv/', views.itemInv, name='itemInv'),
    path('<int:perso_id>/spellInv/', views.spellInv, name='vote'),
]

urlpatterns = format_suffix_patterns(urlpatterns)