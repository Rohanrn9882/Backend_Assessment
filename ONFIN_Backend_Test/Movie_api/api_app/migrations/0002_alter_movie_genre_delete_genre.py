# Generated by Django 4.1.6 on 2023-02-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
