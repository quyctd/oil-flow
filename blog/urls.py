from django.conf.urls import url, include
from blog import views

from blog.API import api_views

from rest_framework.routers import DefaultRouter
from rest_framework import renderers

router = DefaultRouter()
router.register("question", api_views.QuestionViewSet, base_name="question_viewset")

urlpatterns =[
    url(r'^$', views.index, name = "homepage"),
    url(r'^post$', views.QuestionListView.as_view(), name = "postlist"),
    url(r'^post/(?P<pk>\d+)$', views.question_detail, name = "postDetail"),
    url(r'^api/', include(router.urls)),

]
