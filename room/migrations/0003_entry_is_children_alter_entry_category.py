# Generated by Django 4.1.5 on 2023-01-24 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_entry_votes_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='is_children',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entries', to='room.category'),
        ),
    ]
