from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Noticia
from django.urls import reverse_lazy

class NoticiaCreate(CreateView):
    model = Noticia
    fields = ['imagem', 'titulo', 'descricao']
    template_name = 'noticia/form.html'
    success_url = reverse_lazy('index')

class NoticiaUpdate(UpdateView):
    model = Noticia
    fields = ['imagem', 'titulo', 'descricao']
    template_name = 'noticia/form.html'
    success_url = reverse_lazy('index')

class NoticiaDelete(DeleteView):
    model = Noticia
    template_name = 'noticia/form-excluir.html'
    success_url = reverse_lazy('index')

class NoticiaListView(ListView):
    model = Noticia
    template_name: 'noticia/noticia_list.html'

class NoticiaDetailView(DetailView):
    model = Noticia
    template_name: 'noticia/noticia_detail.html'

def mostrar_img(request,id):
    r = get_object_or_404(Noticia, pk=id)

    return HttpResponse(r.img.read)




