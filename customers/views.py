from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer, Profissionalizante
from django.urls import reverse_lazy

class CustomerCreate(CreateView):
    model = Customer
    fields = ['CPF','nome', 'sexo', 'nascimento', 'IdProfissionalizante', 'email', 'celular', 'cep', 'estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento', 'pcd']
    template_name = 'customers/form.html'
    success_url = reverse_lazy('index')

class CustomerUpdate(UpdateView):
    model = Customer
    fields = ['CPF','nome', 'sexo', 'nascimento', 'IdProfissionalizante', 'email', 'celular', 'cep', 'estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento', 'pcd']
    template_name = 'customers/form.html'
    success_url = reverse_lazy('index')

class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customers/form-excluir.html'
    success_url = reverse_lazy('index')
class CustomerListView(ListView):
    model = Customer
    template_name: 'customers/customer_list.html'

def customer_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    customer = get_object_or_404(Customer, pk=pk)

    template_path = 'customers/pdf2.html'
    context = {'customer': customer}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="notafiscal.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'customers/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="notafiscal.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

class ProfissionalizanteCreate(CreateView):
    model = Profissionalizante
    fields = ['imagem', 'nome', 'descricao']
    template_name = 'profissionalizante/form.html'
    success_url = reverse_lazy('index')

class ProfissionalizanteUpdate(UpdateView):
    model = Profissionalizante
    fields = ['imagem', 'nome', 'descricao']
    template_name = 'profissionalizante/form.html'
    success_url = reverse_lazy('index')

class ProfissionalizanteDelete(DeleteView):
    model = Profissionalizante
    template_name = 'profissionalizante/form-excluir.html'
    success_url = reverse_lazy('index')

class ProfissionalizanteListView(ListView):
    model = Profissionalizante
    template_name: 'profissionalizante/profissionalizante_list.html'

def mostrar_img(request,id):
    r = get_object_or_404(Profissionalizante, pk=id)

    return HttpResponse(r.img.read)

