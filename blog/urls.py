from django.conf.urls import url
from blog import views

urlpatterns =[
    url(r'^$', views.index, name = "homepage"),
    url(r'^post$', views.PostListView.as_view(), name = "postlist"),
    url(r'^post/(?P<pk>\d+)$', views.post_detail, name = "postDetail"),
]
