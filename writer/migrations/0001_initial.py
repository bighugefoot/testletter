# Generated by Django 3.2.4 on 2021-06-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='인편',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('작성자', models.CharField(max_length=7)),
                ('제목', models.CharField(max_length=50)),
                ('내용', models.TextField()),
                ('작성일', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
