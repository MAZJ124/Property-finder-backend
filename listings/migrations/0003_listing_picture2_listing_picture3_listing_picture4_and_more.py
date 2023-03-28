# Generated by Django 4.1.7 on 2023-03-24 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_picture1'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]