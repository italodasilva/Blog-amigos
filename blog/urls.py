"""blog URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import paginas
from blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paginas.index, name='index'),
    path('inscrever/', include('customers.urls', namespace='customers')),
    path('beleza/', include('beleza.urls', namespace='beleza')),
    path('esporte/', include('esporte.urls', namespace='esporte')),
    path('index/', paginas.index, name='index'),
    path('sobre/', paginas.sobre, name='sobre'),
    path('curso/', paginas.curso, name='curso'),
    path('noticia/', include('noticia.urls', namespace='noticia')),
    path('secretario/', paginas.secretario, name='secretario'),
    path('accounts/', include('django.contrib.auth.urls'))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
