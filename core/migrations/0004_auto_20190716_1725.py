# Generated by Django 2.2.3 on 2019-07-16 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190716_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Answer'),
        ),
    ]