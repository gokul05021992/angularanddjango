# from django.conf.urls import url
from django.urls import include,path
from.models import Tutorial
from.views import tutorialview

urlpatterns = [
    # path(r'^api/tutorials$', views.tutorial_list),
    # path(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # path(r'^api/tutorials/published$', views.tutorial_list_published),
    # path('apiview',views.APIView.as_view())
    path('api/',tutorialview.as_view(),name = 'tutorialview')
]