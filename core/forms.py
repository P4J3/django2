from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto, Cliente


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-Mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    Mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())


    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['Mensagem']

        conteudo = f'Nome: {nome}\n Email:{email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema django2',
            body= conteudo,
            from_email= 'qualquer',
            to= ['qualquer'],
            headers= {'Reply-To': email}
        )

        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque','imagem']


class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'telefone', 'registro']