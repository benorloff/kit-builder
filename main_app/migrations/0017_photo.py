# Generated by Django 4.0.4 on 2022-04-28 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_alter_lens_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.camera')),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.kit')),
                ('lens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.lens')),
            ],
        ),
    ]
