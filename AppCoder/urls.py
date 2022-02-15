from django.urls import path
from AppCoder import views
from AppCoder.views import PostView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
from AppCoder.models import reseñas



reseñas_list_view = views.reseñasListView.as_view(
    queryset=reseñas.objects.order_by("-fecha")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="AppCoder/reseñas.html",
)




urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    
    path("registro/", views.registro, name="registro"),
    
    path("usuarios/", views.Usuarios, name="usuarios"),
    
    path("buscar/", views.busquedaUsuarios, name="buscar"),
    
    path("contacto/", views.contacto, name="contacto"),
    
    path("reseñas/historial", reseñas_list_view, name="reseñas/historial"),
    
    path("reseñas/", views.reseñas, name="reseñas"),
    
    path("discos/", views.discos, name="discos"),
    
    path("post/", PostView.as_view(), name="post"),
    
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    
    path("add_post/", AddPostView.as_view(), name="add-post"),
    
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="edit-post"),
    
    path("article/<int:pk>/delete/", DeletePostView.as_view(), name="delete-post"),
        
]