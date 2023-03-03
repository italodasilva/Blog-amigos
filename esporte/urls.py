from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import mostrar_img, EsporteCreate, EsporteDelete, EsporteUpdate, EsporteListView, esporte_render_pdf_view, AtividadeCreate, AtividadeDelete, AtividadeListView, AtividadeUpdate

app_name = 'esporte'

urlpatterns = [
    path('', EsporteListView.as_view(), name='esporte-list-view'),
    path('editar/esporte/<pk>/', EsporteUpdate.as_view(), name='editar esporte'),
    path('excluir/esporte/<pk>/', EsporteDelete.as_view(), name='excluir esporte'),
    path('pdf/<pk>/', esporte_render_pdf_view, name='esporte-pdf-view'),
    path('cadastrar/esporte/', EsporteCreate.as_view(), name='cadastrar esporte'),

    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar atividade'),
    path('editar/atividade/<pk>/', AtividadeUpdate.as_view(), name='editar atividade'),
    path('excluir/atividade/<pk>/',AtividadeDelete.as_view(), name='excluir atividade'),
    path('atividade/', AtividadeListView.as_view(), name='atividade-list-view'),
    path('atividade/img/<pk>/', mostrar_img, name='atividade-img-view'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)