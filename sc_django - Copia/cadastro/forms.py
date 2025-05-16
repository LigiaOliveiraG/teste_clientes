from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class CadastroForm(forms.Form):
    nome = forms.CharField(
        label='Nome Completo',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Seu nome completo',
            'id': 'id_nome',
            'class': 'input-field',
        })
    )
    telefone = forms.CharField(
        label='Telefone',
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': '(00) 00000-0000',
            'id': 'id_telefone',
            'class': 'input-field',
        })
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'placeholder': 'exemplo@dominio.com',
            'id': 'id_email',
            'class': 'input-field',
        })
    )
    cpf = forms.CharField(
        label='CPF',
        max_length=14,
        widget=forms.TextInput(attrs={
            'placeholder': '000.000.000-00',
            'id': 'id_cpf',
            'class': 'input-field',
        })
    )
    rg = forms.CharField(
        label='RG',
        max_length=12,
        widget=forms.TextInput(attrs={
            'placeholder': '00.000.000-0',
            'id': 'id_rg',
            'class': 'input-field',
        })
    )
    profissao = forms.CharField(
        label='Profissão',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Sua profissão',
            'id': 'id_profissao',
            'class': 'input-field',
        })
    )
    rua = forms.CharField(
        label='Rua',
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Endereço / Rua',
            'id': 'id_rua',
            'class': 'input-field',
        })
    )
    numero = forms.CharField(
        label='Número',
        max_length=10,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nº',
            'id': 'id_numero',
            'class': 'input-field',
    })
)

    complemento = forms.CharField(
        label='Complemento',
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Apartamento, bloco, etc.',
            'id': 'id_complemento',
            'class': 'input-field',
    })
)
    estado_civil = forms.ChoiceField(
        label='Estado Civil',
        choices=[
            ('solteiro', 'Solteiro(a)'),
            ('casado', 'Casado(a)'),
            ('divorciado', 'Divorciado(a)'),
            ('viuvo', 'Viúvo(a)'),
        ],
        widget=forms.Select(attrs={
            'id': 'id_estado_civil',
            'class': 'input-field',
        })
    )
    cep = forms.CharField(
        label='CEP',
        max_length=9,
        widget=forms.TextInput(attrs={
            'placeholder': '00000-000',
            'id': 'id_cep',
            'class': 'input-field',
        })
    )
