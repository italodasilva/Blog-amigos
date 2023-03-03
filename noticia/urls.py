from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import NoticiaCreate, NoticiaUpdate, NoticiaListView, NoticiaDelete, NoticiaDetailView

app_name = 'noticia'

urlpatterns = [
    path('', NoticiaListView.as_view(), name='noticia-list-view'),
    path('editar/noticia/<pk>/', NoticiaUpdate.as_view(), name='editar noticia'),
    path('excluir/noticia/<pk>/', NoticiaDelete.as_view(), name='excluir noticia'),
    path('news/<pk>/', NoticiaDetailView.as_view(), name='noticia-html-view'),
    path('criar/news/', NoticiaCreate.as_view(), name='criar noticia'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)