# Generated by Django 2.0.1 on 2018-01-27 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('creative_p', '0002_auto_20180127_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ques',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='creative_p.Questions'),
        ),
    ]
