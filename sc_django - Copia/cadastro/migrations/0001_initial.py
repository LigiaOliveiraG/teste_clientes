from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=14)),
                ('rg', models.CharField(max_length=12)),
                ('estado_civil', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=15)),
                ('profissao', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=9)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
    ]
