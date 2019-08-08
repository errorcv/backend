# Generated by Django 2.1.5 on 2019-04-23 06:39

import json
import urllib

from django.db import migrations


class Migration(migrations.Migration):

    def populate_data(apps, schema_editor):
        College = apps.get_model('college', 'College')
        with urllib.request.urlopen(
                "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json") as json_file:
            data = json.load(json_file)
            for d in data:
                name = d['name']
                alpha_two_code = d['alpha_two_code']
                state_province = d['state-province']
                if state_province is None or state_province == 'null':
                    state_province = ''
                country = d['country']
                web_pages = []
                domains = []
                for w in d['web_pages']:
                    web_pages.append(w)
                for domain in d['domains']:
                    domains.append(domain)
                college = College.objects.create(web_pages=web_pages, domains=domains, name=name,
                                                 alpha_two_code=alpha_two_code, state_province=state_province,
                                                 country=country)
                college.save()

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data, reverse_code=migrations.RunPython.noop)
    ]
