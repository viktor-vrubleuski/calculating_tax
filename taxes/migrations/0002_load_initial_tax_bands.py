import os

from django.db import migrations
from django.core import serializers
from django.core.serializers import python


fixture_dir = os.path.abspath(os.path.dirname(__file__))
fixture_filename = '0002_load_initial_tax_bands.json'
fixture_file = os.path.join(fixture_dir, fixture_filename)


def load_fixture(apps, schema_editor):
    original_apps = serializers.python.apps
    serializers.python.apps = apps
    with open(fixture_file, 'rb') as file:
        objects = serializers.deserialize('json', file, ignorenonexistent=True)
        for obj in objects:
            obj.save()
    serializers.python.apps = original_apps


def unload_fixture(apps, schema_editor):
    """Brutally deleting all entries"""
    original_apps = serializers.python.apps
    serializers.python.apps = apps
    with open(fixture_file, 'rb') as file:
        objects = serializers.deserialize('json', file, ignorenonexistent=True)
        for obj in reversed(objects):
            obj.delete()
    serializers.python.apps = original_apps


class Migration(migrations.Migration):
    dependencies = [
        ('taxes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),

    ]