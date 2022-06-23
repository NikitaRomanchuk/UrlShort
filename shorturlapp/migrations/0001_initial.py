from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('original_url', models.URLField()),
                ('shorted_url', models.URLField(blank=True, unique=True)),
                ('shares', models.PositiveIntegerField(default=0)),
                ('url_context', models.CharField(blank=True, default='0', max_length=20))
            ],
            options={
                'ordering': ['-shares'],
            },
        ),
    ]
