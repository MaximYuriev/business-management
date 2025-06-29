# Generated by Django 5.2.1 on 2025-05-22 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('manager', 'Manager'), ('subordinate', 'Subordinate')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.company'),
        ),
    ]
