# Generated by Django 4.2.2 on 2023-07-11 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipopapel', '0002_remove_tipopapel_idtipopapel_tipopapel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gramatura', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('fktipopapel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipopapel.tipopapel')),
            ],
        ),
    ]