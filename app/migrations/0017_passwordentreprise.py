# Generated by Django 4.1.1 on 2023-02-23 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_commentaire_forum_alter_commentaire_commentateur'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordEntreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
                ('entreprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.entreprise')),
            ],
        ),
    ]
