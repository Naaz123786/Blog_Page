from django.urls import path 

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),
    path("addpost", views.AddPostView.as_view(), name="add-post"),
    path("readlater", views.ReadLaterView.as_view(), name="addtoread"),
    path("deletefromlater", views.DeleteView.as_view(), name="delete"),
    path("readlaterpost", views.AllReadLaterView.as_view(), name="read"),
    path("posts/<slug:slug>", views.post_detail.as_view(), name="post-detail-page"),
]
