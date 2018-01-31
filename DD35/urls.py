from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    # url(r'^armors/$', views.armors_list),
    # url(r'^armors/(?P<pk>[0-9]+)/$', views.armors_detail),
    # url(r'^chat/', include('chatrooms.urls')),
    url(r'^armors/$', views.armors_list.as_view(), name='armors'),
    url(r'^armors/(?P<pk>[0-9]+)/$', views.armors_detail.as_view(), name='armorDetail'),
    url(r'ajax/chat/', views.broadcast),
    path('chat', views.chat_list, name='chat_list'),
    path('chat/<int:chat_room_id>', views.chat_detail, name='chat_detail'),
    path('', views.index, name='index'),
    path('charac/<int:charac_id>/', views.character_detail, name='perso'),
    path('<int:perso_id>/itemInv/', views.itemInv, name='itemInv'),
    path('<int:perso_id>/spellInv/', views.spellInv, name='vote'),
    url(r'^signup/$', views.signup, name='signup'),
    url('^', include('django.contrib.auth.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)