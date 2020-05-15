# Generated by Django 2.2.7 on 2020-05-14 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OmniDB_app', '0011_auto_20200513_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='SnippetFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OmniDB_app.SnippetFolder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SnippetFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField()),
                ('text', models.TextField(default='')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OmniDB_app.SnippetFolder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
