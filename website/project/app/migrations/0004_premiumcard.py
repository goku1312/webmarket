# Generated by Django 4.2.6 on 2023-10-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_register_otp_enabled_register_otp_secret'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_img', models.ImageField(upload_to='temp_meadia')),
                ('temp_file', models.FileField(upload_to='templates')),
                ('creator_name', models.CharField(max_length=50)),
                ('model_name', models.CharField(blank=True, max_length=50)),
                ('category_name', models.CharField(default='Premium Templates', max_length=50)),
                ('price', models.IntegerField(default=399)),
            ],
        ),
    ]
