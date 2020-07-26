# Generated by Django 3.0.8 on 2020-07-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('choice1', models.TextField()),
                ('choice2', models.TextField()),
                ('choice3', models.TextField()),
                ('choice4', models.TextField()),
                ('answer', models.IntegerField()),
            ],
        ),
    ]