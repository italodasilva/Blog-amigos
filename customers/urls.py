from django.urls import path
from .views import render_pdf_view, CustomerListView, customer_render_pdf_view, CustomerCreate, CustomerUpdate, CustomerDelete, ProfissionalizanteListView, ProfissionalizanteCreate, ProfissionalizanteUpdate, ProfissionalizanteDelete, mostrar_img
from django.conf import settings
from django.conf.urls.static import static

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list-view'),
    path('test/', render_pdf_view, name='pdf-view'),
    path('editar/customer/<pk>/', CustomerUpdate.as_view(), name='editar customer'),
    path('excluir/customer/<pk>/', CustomerDelete.as_view(), name='excluir customer'),
    path('pdf/<pk>/', customer_render_pdf_view, name='customer-pdf-view'),
    path('cadastrar/customer/', CustomerCreate.as_view(), name='cadastrar customer'),

    path('cadastrar/profissionalizante/', ProfissionalizanteCreate.as_view(), name='cadastrar profissionalizante'),
    path('editar/profissionalizante/<pk>/', ProfissionalizanteUpdate.as_view(), name='editar profissionalizante'),
    path('excluir/profissionalizante/<pk>/', ProfissionalizanteDelete.as_view(), name='excluir profissionalizante'),
    path('profissionalizante/', ProfissionalizanteListView.as_view(), name='profissionalizante-list-view'),
    path('profissionalizante/img/<pk>/', mostrar_img, name='profissionalizante-img-view'),  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)