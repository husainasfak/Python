# Generated by Django 4.2.3 on 2023-07-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='book_images/'),
        ),
    ]
