# Generated by Django 3.2.8 on 2021-11-09 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211109_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.livro')),
            ],
        ),
    ]
