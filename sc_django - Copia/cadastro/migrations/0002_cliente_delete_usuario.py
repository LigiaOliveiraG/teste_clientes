from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('rg', models.CharField(max_length=20)),
                ('estado_civil', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=9)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('profissao', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
