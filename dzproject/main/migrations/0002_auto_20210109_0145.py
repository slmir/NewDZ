# Generated by Django 3.1.5 on 2021-01-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Category',
            field=models.CharField(choices=[('Мебель', 'Мебель'), ('Стройматериалы', 'Строительные материалы'), ('Инструменты', 'Инструменты для выполнения строительных,отделочных работ'), ('Техника', 'Технические средства, машины для строительных, отделочных работ')], max_length=50, verbose_name='Категория'),
        ),
    ]
