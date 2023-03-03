from django.shortcuts import get_object_or_404, redirect, render
from blog.models import Inscricao
from django.forms import ModelForm

class InscricaoForm(ModelForm):
    class Meta:
        model = Inscricao
        fields = '__all__'

def listar(request):
    inscricao =  Inscricao.objects.all()

    return render(request, 'inscricao/inicio.html', {
        'inscricao': inscricao
    })


def criar(request):
    frm = InscricaoForm(request.POST or None)

    if frm.is_valid():
        frm.save()
        return redirect('inscricao')

    return render(request, 'inscricao/form.html',{
        'titulo' : 'Fazer Matricula',
        'frm':frm
    })

def editar(request,id):
    inscricao = get_object_or_404(Inscricao, pk=id)
    frm = InscricaoForm(request.POST or None, instance=inscricao)

    if frm.is_valid():
        frm.save()
        return redirect('index')

    return render(request, 'inscricao/form.html',{
        'titulo' : 'Editar Inscrição',
        'frm':frm
    })

def excluir(request,id):
    inscricao = get_object_or_404(Inscricao, pk=id)
    inscricao.delete()

    return redirect('inscricao')