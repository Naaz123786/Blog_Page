# Generated by Django 4.2.1 on 2023-06-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_author_posts_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=80)),
                ('tags', models.ManyToManyField(null=True, to='blog.post')),
            ],
        ),
    ]
