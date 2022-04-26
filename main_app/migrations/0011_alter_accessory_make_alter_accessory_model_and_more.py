# Generated by Django 4.0.4 on 2022-04-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_accessory_type_alter_camera_make_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='make',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='model',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='camera',
            name='body_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='camera',
            name='lens_mount',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='camera',
            name='model',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='camera',
            name='sensor_size',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='kit',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lens',
            name='focal_length',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lens',
            name='lens_type',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lens',
            name='max_aperture',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lens',
            name='min_aperture',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lens',
            name='model',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lens',
            name='mount',
            field=models.CharField(max_length=255),
        ),
    ]