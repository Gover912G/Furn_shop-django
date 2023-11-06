# Generated by Django 3.2.22 on 2023-11-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('sname', models.CharField(max_length=50)),
                ('description', models.TextField(default='')),
                ('btnShopNow', models.CharField(max_length=10)),
                ('btnExplore', models.CharField(max_length=20)),
                ('image', models.ImageField(default='profile.png', upload_to='images')),
            ],
        ),
    ]