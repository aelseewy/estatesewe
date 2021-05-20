# Generated by Django 3.2 on 2021-05-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20210519_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='city',
            field=models.CharField(choices=[('AS', 'المتميز'), ('KA', 'الحي اثني عشر'), ('GJ', 'الحي الثالث'), ('JH', 'الحي الحادي عشر'), ('AP', '6 اكتوبر'), ('HP', 'الحي الرابع'), ('CG', 'الحي الاول'), ('AR', 'الشيخ زايد'), ('GA', 'الحي التاني'), ('BR', 'الحصري')], max_length=70),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(choices=[('Property', 'اسكندرية'), ('Cars', 'الجيزة'), ('Mobiles', 'الغردقة'), ('Jobs', 'راس سدر'), ('Bikes', 'الفيوم'), ('Fashion', 'العين السخنة'), ('Electronics', 'القاهرة الكبري'), ('Books&Sports', 'الاسماعيلية'), ('Furniture', 'الساحل الشمالي')], max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='url_link',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
