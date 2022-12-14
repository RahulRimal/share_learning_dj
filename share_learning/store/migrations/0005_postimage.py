# Generated by Django 4.1.1 on 2022-09-14 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_post_author_alter_post_book_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post/images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.post')),
            ],
        ),
    ]
