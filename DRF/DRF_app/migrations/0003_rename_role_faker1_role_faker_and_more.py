# Generated by Django 4.2.2 on 2023-07-20 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DRF_app', '0002_rename_role_faker_role_faker1_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Role_Faker1',
            new_name='Role_Faker',
        ),
        migrations.RenameModel(
            old_name='Task_Faker1',
            new_name='Task_Faker',
        ),
        migrations.RenameModel(
            old_name='User_Faker1',
            new_name='User_Faker',
        ),
    ]
