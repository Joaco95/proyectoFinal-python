from django.urls import path
from AppCoder import views
from AppCoder.views import PostView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView,EditProfile

urlpatterns = [
    path("", views.inicio, name="inicio"),
    
    path("post/", PostView.as_view(), name="post"),
    
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    
    path("add_post/", AddPostView.as_view(), name="add-post"),
    
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="edit-post"),
    
    path("article/<int:pk>/delete/", DeletePostView.as_view(), name="delete-post"),
    
    path("miprofile/",views.miPerfil,name="miProfile"),
    
    path("profile/",views.perfilEdit, name="profile"),
    
    path("imageProfile/<int:pk>",EditProfile.as_view(),name="imageProfile"),
    
    

        
]