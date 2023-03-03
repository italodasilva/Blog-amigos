from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Atividade, Esporte
from django.urls import reverse_lazy

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['imagem', 'nome', 'descricao']
    template_name = 'atividade/form.html'
    success_url = reverse_lazy('index')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['imagem', 'nome', 'descricao']
    template_name = 'atividade/form.html'
    success_url = reverse_lazy('index')

class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'atividade/form-excluir.html'
    success_url = reverse_lazy('index')

class AtividadeListView(ListView):
    model = Atividade
    template_name: 'atividade/atividade_list.html'

def mostrar_img(request,id):
    r = get_object_or_404(Atividade, pk=id)

    return HttpResponse(r.img.read)

class EsporteCreate(CreateView):
    model = Esporte
    fields = ['CPF','nome', 'sexo', 'nascimento', 'IdAtividade', 'email', 'celular', 'cep', 'estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento', 'pcd']
    template_name = 'esporte/form.html'
    success_url = reverse_lazy('index')

class EsporteUpdate(UpdateView):
    model = Esporte
    fields = ['CPF','nome', 'sexo', 'nascimento', 'IdEsporte', 'email', 'celular', 'cep', 'estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento', 'pcd']
    template_name = 'esporte/form.html'
    success_url = reverse_lazy('index')

class EsporteDelete(DeleteView):
    model = Esporte
    template_name = 'esporte/form-excluir.html'
    success_url = reverse_lazy('index')

class EsporteListView(ListView):
    model = Esporte
    template_name: 'esporte/esporte_list.html'

def esporte_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    esporte = get_object_or_404(Esporte, pk=pk)

    template_path = 'esporte/pdf2.html'
    context = {'esporte': esporte}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="cursoesporte.pdf"'
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
