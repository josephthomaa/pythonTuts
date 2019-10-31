# Generated by Django 2.2.6 on 2019-10-28 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_auto_20191028_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterField(
            model_name='expense',
            name='ExpenseType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='expense', to='rental.ExpenseType'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='rental.Publication')),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
    ]