# Generated by Django 4.0.4 on 2022-05-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_advert'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]