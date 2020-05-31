# Generated by Django 3.0.6 on 2020-05-31 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mynews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_to_read', models.IntegerField(choices=[(1, 'easy'), (2, 'medium-easy'), (3, 'medium'), (4, 'medium-hard'), (5, 'hard')])),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mynews.Author')),
            ],
        ),
    ]
