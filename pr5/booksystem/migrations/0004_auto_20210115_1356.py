# Generated by Django 3.1.1 on 2021-01-15 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksystem', '0003_userinfor_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInfor',
            new_name='Document',
        ),
    ]
