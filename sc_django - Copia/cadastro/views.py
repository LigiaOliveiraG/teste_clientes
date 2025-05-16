from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Cliente

def formulario_view(request):
    erro_cpf = None  # Inicializa variável de erro
    
    if request.method == 'POST':
        data = request.POST
        try:
            Cliente.objects.create(
                nome=data['nome'],
                data_nascimento=data['data_nascimento'],
                email=data['email'],
                cpf=data['cpf'],
                rg=data['rg'],
                estado_civil=data['estado_civil'],
                telefone=data['telefone'],
                cep=data['cep'],
                rua=data['rua'],
                numero=data['numero'],
                complemento=data['complemento'],
                bairro=data['bairro'],
                cidade=data['cidade'],
                estado=data['estado'],
                profissao=data['profissao'],
            )
            return redirect('sucesso')  # Redireciona se sucesso
        except IntegrityError:
            erro_cpf = "Esse CPF já está cadastrado."

    # Passa a mensagem de erro para o template (ou None se não houve erro)
    return render(request, 'cadastro/form.html', {'erro_cpf': erro_cpf})

def sucesso_view(request):
    return render(request, 'cadastro/sucesso.html')
