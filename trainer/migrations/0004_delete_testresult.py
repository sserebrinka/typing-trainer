# Generated by Django 5.1.4 on 2024-12-29 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_alter_testresult_options_alter_testresult_accuracy_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestResult',
        ),
    ]
