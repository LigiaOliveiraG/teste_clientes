from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_cliente_delete_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='profissao',
        ),
        migrations.AddField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
