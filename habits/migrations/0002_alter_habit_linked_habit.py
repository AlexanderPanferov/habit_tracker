# Generated by Django 4.2.5 on 2024-03-10 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='linked_habit',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_pleasant': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Связанная привычка'),
        ),
    ]
