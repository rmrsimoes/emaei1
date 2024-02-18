from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto

class ContactoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=150)
    email = forms.CharField(label='E-mail', max_length=150)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema emaei1',
            body=conteudo,
            from_email='contacto@seudominio.com.br',
            to=['contacto@seudominio.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'stock', 'imagem']