from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Curso, Beleza
from django.urls import reverse_lazy

class CursoCreate(CreateView):
    model = Curso
    fields = ['imagem', 'nome', 'descricao']
    template_name = 'curso/form.html'
    success_url = reverse_lazy('index')

class CursoUpdate(UpdateView):
    model = Curso
    fields = ['imagem', 'nome', 'descricao']
    template_name = 'curso/form.html'
    success_url = reverse_lazy('index')

class CursoDelete(DeleteView):
    model = Curso
    template_name = 'curso/form-excluir.html'
    success_url = reverse_lazy('index')

class CursoListView(ListView):
    model = Curso
    template_name: 'curso/curso_list.html'

def mostrar_img(request,id):
    r = get_object_or_404(Curso, pk=id)

    return HttpResponse(r.img.read)

class BelezaCreate(CreateView):
    model = Beleza
    fields = ['CPF','nome', 'sexo', 'nascimento', 'IdCurso', 'email', 'celular', 'cep', 'estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento', 'pcd']
    template_name = 'beleza/form.html'
    success_url = reverse_lazy('index')

class BelezaUpdate(UpdateView):
    model = Beleza
    fields = ['CPF','nome', 'sexo', 'nascimento', 'IdCurso', 'email', 'celular', 'cep', 'estado', 'cidade', 'bairro', 'rua', 'numero', 'complemento', 'pcd']
    template_name = 'beleza/form.html'
    success_url = reverse_lazy('index')

class BelezaDelete(DeleteView):
    model = Beleza
    template_name = 'beleza/form-excluir.html'
    success_url = reverse_lazy('index')

class BelezaListView(ListView):
    model = Beleza
    template_name: 'beleza/beleza_list.html'

def beleza_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    beleza = get_object_or_404(Beleza, pk=pk)

    template_path = 'beleza/pdf2.html'
    context = {'beleza': beleza}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="cursobeleza.pdf"'
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
    template_path = 'beleza/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="cursobeleza.pdf"'
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
