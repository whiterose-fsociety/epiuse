# Generated by Django 3.1.3 on 2020-11-15 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201115_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_relation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='underlings', to='main.employee', verbose_name='relation'),
        ),
    ]
