# Generated by Django 4.2.3 on 2023-07-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_feature_icone_alter_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-leaf', 'Folha'), ('lni-layers', 'Design'), ('lni-laptop-phone', 'Laptop'), ('lni-cog', 'Engrenagem')], default='', max_length=16, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-stats-up', 'Gráfico'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-cog', 'Engrenagem'), ('lni-users', 'Usuários')], max_length=12, verbose_name='Icone'),
        ),
    ]
