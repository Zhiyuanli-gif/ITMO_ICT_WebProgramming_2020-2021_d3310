# Generated by Django 3.1.1 on 2021-01-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksystem', '0002_userinfor'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfor',
            name='number',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
