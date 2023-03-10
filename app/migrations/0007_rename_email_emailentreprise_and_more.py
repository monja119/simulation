# Generated by Django 4.1.1 on 2023-02-23 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_entreprise_email_remove_entreprise_telephone_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Email',
            new_name='EmailEntreprise',
        ),
        migrations.RenameField(
            model_name='emailentreprise',
            old_name='etudiant',
            new_name='entreprise',
        ),
        migrations.CreateModel(
            name='EmailEtudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='app.etudiant')),
            ],
        ),
    ]
