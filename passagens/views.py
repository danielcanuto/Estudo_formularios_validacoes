from django.shortcuts import render
from passagens.forms import PassagemForms, Pessoaforms

# Create your views here.

def index(request):
    form = PassagemForms()
    pessoa_form = Pessoaforms()
    context = {'form':form, 'pessoa_form':pessoa_form}
    return render(request, 'passagens/index.html', context)
  

def result(request):
    if request.method =="POST":
        form = PassagemForms(request.POST)
        pessoa_form = Pessoaforms(request.POST)
       

        if form.is_valid():
            context = {'form':form, 'pessoa_form':pessoa_form}
            return render(request, 'passagens/result.html', context)
        else:
            print("Dados inesperado!")
            context = {'form':form, 'pessoa_form':pessoa_form}
            return render(request, 'passagens/index.html', context)
