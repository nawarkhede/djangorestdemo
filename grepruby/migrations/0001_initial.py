# Generated by Django 3.1.7 on 2021-03-03 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(null=True)),
                ('author_name', models.CharField(max_length=30)),
            ],
            options={
                'unique_together': {('title', 'author_name')},
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='grepruby.article')),
            ],
        ),
    ]