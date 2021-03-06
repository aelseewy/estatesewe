# Generated by Django 3.2 on 2021-05-20 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_auto_20210519_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='city',
            field=models.CharField(choices=[('الحي اثني عشر', 'الحي اثني عشر'), ('الحصري', 'الحصري'), ('الشيخ زايد', 'الشيخ زايد'), ('المتميز', 'المتميز'), ('اكتوبر 6', '6 اكتوبر'), ('الحي الحادي عشر', 'الحي الحادي عشر'), ('مدينة نصر', 'مدينة نصر'), ('الحي الاول', 'الحي الاول'), ('الحي التاني', 'الحي التاني'), ('الحي الرابع', 'الحي الرابع'), ('الحي الثالث', 'الحي الثالث')], max_length=70),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(choices=[('الاسماعيلية', 'الاسماعيلية'), ('الساحل الشمالي', 'الساحل الشمالي'), ('الجيزة', 'الجيزة'), ('القاهرة الكبري', 'القاهرة الكبري'), ('الغردقة', 'الغردقة'), ('الفيوم', 'الفيوم'), ('العين السخنة', 'العين السخنة'), ('اسكندرية', 'اسكندرية'), ('راس سدر', 'راس سدر')], max_length=100),
        ),
    ]
