from django.shortcuts import render, redirect
from .forms import ContatoForm, ProdutoModelForm, ClienteModelForm
from django.contrib import messages

from .models import Cliente, Produto

# Create your views here.

def index(request):
    prod = Produto.objects.all()

    context ={
        'prod': prod
    }
    return render(request, 'index.html', context)



def contato(request):
    form = ContatoForm(request.POST or None)

    if(str(request.method) == 'POST'):
        if form.is_valid():
            form.send_email()

            messages.success(request, 'Email enviado com sucesso')
            form = ContatoForm

        else:
            messages.error(request, 'Falha ao enviar email')

    context = {
        'form': form
    }

    return render(request, 'contato.html', context)

def produto(request):
    print(dir(request))
    print(dir(request.user))
    print(request.user.is_authenticated)

    if (request.user.is_authenticated == True):
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'Produto salvo com sucesso')
            else:
                messages.error(request, 'Erro ao salvar produto')
            form = ProdutoModelForm()
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }
        return render(request, 'produto.html', context)

    else:
        return redirect(index)


def cliente(request):
    if str(request.method) == 'POST':
        form = ClienteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Cliente cadastrado com sucesso')
        else:
            messages.error(request,'Não foi possível cadastrar o cliente')
        form = ClienteModelForm()
    else:
        form = ClienteModelForm()

    context = {
        'form': form
    }
    return render(request, 'clientes.html', context)


def mostra_cliente(request):
    clientes = Cliente.objects.all()

    context ={
        'clientes': clientes
    }
    return render(request,'mostra_cliente.html', context)