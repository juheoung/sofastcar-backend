# Generated by Django 3.1 on 2020-09-10 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carzones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoBeforeUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ImagesBeforeUse/%Y/%m/%d')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_owners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(help_text='차 번호판', max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('manufacturer', models.CharField(choices=[('HD', '현대자동차'), ('KIA', '기아자동차'), ('BMW', 'BMW'), ('SSY', '쌍용자동차'), ('RS', '르노삼성자동차'), ('BENZ', '벤츠'), ('POR', '포르쉐')], max_length=20)),
                ('fuel_type', models.CharField(choices=[('DS', '경유'), ('GAS', '휘발유'), ('ELC', '전기')], default='GAS', help_text='연료', max_length=20)),
                ('type_of_vehicle', models.CharField(choices=[('A', '경차'), ('B', '소형'), ('C', '준중형'), ('D', '중형'), ('E', '준대형'), ('F', '대형'), ('S', '스포츠카'), ('M', '미니밴'), ('J', 'SUV')], default='C', help_text='차종', max_length=10)),
                ('shift_type', models.CharField(choices=[('AT', '자동'), ('MT', '수동')], default='AT', help_text='기어', max_length=10)),
                ('riding_capacity', models.PositiveIntegerField(help_text='승차정원')),
                ('is_event_model', models.BooleanField(help_text='쏘카세이브')),
                ('manual_page', models.CharField(default='', max_length=100)),
                ('safety_option', models.CharField(default='', max_length=255)),
                ('convenience_option', models.CharField(default='', max_length=255)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='carzones.carzone')),
            ],
        ),
    ]
