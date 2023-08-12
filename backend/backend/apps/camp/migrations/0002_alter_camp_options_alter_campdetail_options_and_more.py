# Generated by Django 4.2.4 on 2023-08-12 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("camp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="camp",
            options={"verbose_name": "Стоянка", "verbose_name_plural": "Стоянки"},
        ),
        migrations.AlterModelOptions(
            name="campdetail",
            options={
                "verbose_name": "Детали стоянки",
                "verbose_name_plural": "Детали стоянок",
            },
        ),
        migrations.AlterModelOptions(
            name="otherpht",
            options={
                "verbose_name": "Дополнительное фото",
                "verbose_name_plural": "Дополнительные фото",
            },
        ),
        migrations.AddField(
            model_name="campdetail",
            name="attractions",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="Достопримечательности"
            ),
        ),
        migrations.AddField(
            model_name="campdetail",
            name="size",
            field=models.CharField(blank=True, max_length=150, verbose_name="Размер"),
        ),
        migrations.AddField(
            model_name="campdetail",
            name="sunset",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="Закаты/рассветы"
            ),
        ),
        migrations.AlterField(
            model_name="camp",
            name="latitude",
            field=models.FloatField(verbose_name="Широта"),
        ),
        migrations.AlterField(
            model_name="camp",
            name="longitude",
            field=models.FloatField(verbose_name="Долгота"),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="ashore",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="Тип берега"
            ),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="camp",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="camp.camp",
                verbose_name="Стоянка",
            ),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="connection",
            field=models.CharField(blank=True, max_length=150, verbose_name="Связь"),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="conveniences",
            field=models.CharField(blank=True, max_length=150, verbose_name="Удобства"),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="description",
            field=models.TextField(blank=True, verbose_name="Дополнительно"),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="firewood",
            field=models.CharField(blank=True, max_length=150, verbose_name="Дрова"),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="mosquitoes",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="Комары/продуваемость"
            ),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="number_tents",
            field=models.IntegerField(blank=True, verbose_name="Мест для палаток"),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="pht_camping",
            field=models.ImageField(
                blank=True, upload_to="static/", verbose_name="Фото стоянки"
            ),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="pht_from_water",
            field=models.ImageField(
                blank=True, upload_to="static/", verbose_name="Фото с воды"
            ),
        ),
        migrations.AlterField(
            model_name="campdetail",
            name="visibility",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="Видимость с воды"
            ),
        ),
        migrations.AlterField(
            model_name="otherpht",
            name="image",
            field=models.ImageField(upload_to="static/", verbose_name="Фото"),
        ),
    ]
