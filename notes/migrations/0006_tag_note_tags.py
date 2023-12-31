# Generated by Django 4.2.7 on 2023-12-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_note_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(to='notes.tag'),
        ),
    ]
