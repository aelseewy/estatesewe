# Generated by Django 3.2 on 2021-05-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20210519_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='city',
            field=models.CharField(choices=[('AR', 'الشيخ زايد'), ('CG', 'الحي الاول'), ('HP', 'الحي الرابع'), ('KA', 'الحي اثني عشر'), ('BR', 'الحصري'), ('AP', '6 اكتوبر'), ('AS', 'المتميز'), ('GJ', 'الحي الثالث'), ('JH', 'الحي الحادي عشر'), ('GA', 'الحي التاني')], max_length=70),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(choices=[('Furniture', 'الساحل الشمالي'), ('Cars', 'الجيزة'), ('Books&Sports', 'الاسماعيلية'), ('Electronics', 'القاهرة الكبري'), ('Fashion', 'العين السخنة'), ('Jobs', 'راس سدر'), ('Mobiles', 'الغردقة'), ('Bikes', 'الفيوم'), ('Property', 'اسكندرية')], max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='url_link',
            field=models.URLField(blank=True, max_length=270, null=True),
        ),
    ]