# Generated by Django 3.2 on 2021-05-18 12:18

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import embed_video.fields
import multiselectfield.db.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_auto_20210517_2318'),
        ('core', '0002_auto_20210518_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_selected', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
                ('item_snippet', models.CharField(default='click to read the blog post ', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('estate_type', models.CharField(choices=[('rent', 'Rent'), ('lease', 'Lease')], default='rent', max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('Jobs', 'Jobs'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture'), ('Property', 'Property'), ('Cars', 'Cars'), ('Mobiles', 'Mobiles'), ('Bikes', 'Bikes'), ('Fashion', 'Fashion'), ('Electronics', 'Electronics')], max_length=100)),
                ('city', models.CharField(choices=[('KA', 'Karnataka'), ('GJ', 'Gujarat'), ('NL', 'Nagaland'), ('AR', 'Arunachal Pradesh'), ('KL', 'Kerala'), ('UK', 'Uttarakhand'), ('CG', 'Chhattisgarh'), ('UP', 'Uttar Pradesh'), ('OD', 'Odisha'), ('JH', 'Jharkhand'), ('GA', 'Goa'), ('PB', 'Punjab'), ('TN', 'Tamil Nadu'), ('MZ', 'Mizoram'), ('AP', 'Andhra Pradesh'), ('WB', 'West Bengal'), ('ML', 'Meghalaya'), ('MN', 'Manipur'), ('MH', 'Maharashtra'), ('HP', 'Haryana'), ('TR', 'Tripura'), ('MP', 'Madhya Pradesh'), ('MI', 'Sikkim'), ('AS', 'Assam'), ('RJ', 'Rajasthan'), ('BR', 'Bihar'), ('TS', 'Telegana')], max_length=70)),
                ('feature_type', multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=195)),
                ('snippet', models.CharField(default='click to read the blog post ', max_length=250)),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('bathrooms', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('garage', models.IntegerField(default=0)),
                ('sqmt', models.IntegerField(blank=True, null=True)),
                ('lot_size', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('post_photo', models.ImageField(blank=True, null=True, upload_to='photos/listings/')),
                ('post_photo_1', models.ImageField(blank=True, null=True, upload_to='photos/listings/')),
                ('post_photo_2', models.ImageField(blank=True, null=True, upload_to='photos/listings/')),
                ('post_photo_3', models.ImageField(blank=True, null=True, upload_to='photos/listings/')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True)),
                ('youtube_link', models.URLField(blank=True, max_length=130, null=True)),
                ('url_link', models.URLField(blank=True, max_length=130, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('no_of_owners', models.CharField(max_length=100)),
                ('is_featured', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
