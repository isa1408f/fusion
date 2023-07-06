# Generated by Django 4.2.3 on 2023-07-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_servico_icone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('feature', models.CharField(max_length=100, verbose_name='Recurso')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuários'), ('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico')], max_length=12, verbose_name='Icone'),
        ),
    ]
