"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from ProyectoFinal.views import login_request, signup, logout_user
from ProyectoFinal import views
from django.contrib.auth.views import LogoutView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


##imagenes

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", include("AppCoder.urls")),
    path('admin/', admin.site.urls),
    #JESUS 15/02
    path('login', login_request, name = 'login'),  
    #JESUS 16/02 
    path('login', views.login_request, name= 'login'),
    path('signup', views.signup, name= 'signup'),
    #JEREMIAS
    path('logout', views.logout_user, name= 'logout'),
]


urlpatterns += staticfiles_urlpatterns()

##imagenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Jesus Test