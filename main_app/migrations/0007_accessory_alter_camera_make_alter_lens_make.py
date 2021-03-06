# Generated by Django 4.0.4 on 2022-04-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_camera_make_alter_lens_image_stab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('BAC', 'Backpack'), ('FIL', 'Filter'), ('LIG', 'Lighting'), ('TRI', 'Tripod')], max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='camera',
            name='make',
            field=models.CharField(choices=[('AGF', 'Agfa'), ('CAN', 'Canon'), ('CAS', 'Casio'), ('CON', 'Contax'), ('DXO', 'DxO Labs'), ('FUJ', 'Fujifilm'), ('HAS', 'Hasselblad'), ('KOD', 'Kodak'), ('MIN', 'Minolta'), ('KYO', 'Kyocera'), ('LEI', 'Leica'), ('NIK', 'Nikon'), ('OLY', 'Olympus'), ('PAN', 'Panasonic'), ('PEN', 'Pentax'), ('RIC', 'Ricoh'), ('SAM', 'Samsung'), ('SIG', 'Sigma'), ('SON', 'Sony'), ('ZEI', 'Zeiss')], max_length=255),
        ),
        migrations.AlterField(
            model_name='lens',
            name='make',
            field=models.CharField(choices=[('BOW', 'Bower'), ('CAN', 'Canon'), ('IRI', 'Irix'), ('KOW', 'Kowa'), ('LEN', 'Lensbaby'), ('MEI', 'Meike'), ('MEY', 'Meyer-Optik Gorlitz'), ('MIT', 'Mitakon Zhongyi'), ('NIK', 'Nikon'), ('OPT', 'Opteka'), ('PEN', 'Pentax'), ('ROK', 'Rokinon'), ('SAM', 'Samyang'), ('SCH', 'Schneider'), ('SIG', 'Sigma'), ('SON', 'Sony'), ('TAM', 'Tamron'), ('TOK', 'Tokina'), ('VEN', 'Venus Optics'), ('VIV', 'Vivitar'), ('VOI', 'Voigtlander'), ('YON', 'Yongnuo'), ('ZEI', 'Zeiss'), ('ZEN', 'Zenit')], max_length=255),
        ),
    ]
