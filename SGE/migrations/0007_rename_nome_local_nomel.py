# Generated by Django 5.2.1 on 2025-05-16 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SGE', '0006_alter_participante_telefone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='local',
            old_name='nome',
            new_name='nomeL',
        ),
    ]
