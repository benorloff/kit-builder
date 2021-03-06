# Generated by Django 4.0.4 on 2022-04-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_max_aperature_lens_max_aperture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='make',
            field=models.CharField(choices=[('AGFA', 'Agfa'), ('CANON', 'Canon'), ('CASIO', 'Casio'), ('CONTAX', 'Contax'), ('DXO_LABS', 'DxO Labs'), ('FUJIFILM', 'Fujifilm'), ('HASSELBLAD', 'Hasselblad'), ('KODAK', 'Kodak'), ('MINOLTA', 'Minolta'), ('KYOCERA', 'Kyocera'), ('LEICA', 'Leica'), ('NIKON', 'Nikon'), ('OLYMPUS', 'Olympus'), ('PANASONIC', 'Panasonic'), ('PENTAX', 'Pentax'), ('RICOH', 'Ricoh'), ('SAMSUNG', 'Samsung'), ('SIGMA', 'Sigma'), ('SONY', 'Sony'), ('ZEISS', 'Zeiss')], max_length=30),
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cameras', models.ManyToManyField(to='main_app.camera')),
                ('lenses', models.ManyToManyField(to='main_app.lens')),
            ],
        ),
    ]
