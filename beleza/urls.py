from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import beleza_render_pdf_view ,BelezaListView, BelezaCreate, BelezaDelete, BelezaUpdate, mostrar_img, CursoCreate, CursoDelete, CursoListView, CursoUpdate

app_name = 'beleza'

urlpatterns = [
    path('', BelezaListView.as_view(), name='beleza-list-view'),
    path('editar/beleza/<pk>/', BelezaUpdate.as_view(), name='editar beleza'),
    path('excluir/beleza/<pk>/', BelezaDelete.as_view(), name='excluir beleza'),
    path('pdf/<pk>/', beleza_render_pdf_view, name='beleza-pdf-view'),
    path('cadastrar/beleza/', BelezaCreate.as_view(), name='cadastrar beleza'),

    path('cadastrar/curso/', CursoCreate.as_view(), name='cadastrar curso'),
    path('editar/curso/<pk>/', CursoUpdate.as_view(), name='editar curso'),
    path('excluir/curso/<pk>/',CursoDelete.as_view(), name='excluir curso'),
    path('curso/', CursoListView.as_view(), name='curso-list-view'),
    path('curso/img/<pk>/', mostrar_img, name='curso-img-view'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)