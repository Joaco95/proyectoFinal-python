from django.urls import path
from AppCoder import views
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
    
    path("post/", views.post, name="post"),
        
]