# Generated by Django 4.2.4 on 2023-08-15 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('contact_number', models.CharField(max_length=15)),
                ('profile_picture', models.ImageField(upload_to='profile_pic_author/')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publication_date', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
                ('genre', models.CharField(max_length=50)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='books/covers/')),
                ('summary', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneTomany.author')),
            ],
        ),
    ]
