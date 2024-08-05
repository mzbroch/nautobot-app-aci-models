# Generated by Django 3.2.23 on 2024-07-23 20:26

import uuid

import django.core.serializers.json
import django.db.models.deletion
import nautobot.core.models.fields
import nautobot.extras.models.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0102_set_null_objectchange_contenttype'),
        ('dcim', '0052_fix_interface_redundancy_group_created'),
        ('tenancy', '0008_tagsfield'),
        ('ipam', '0039_alter_ipaddresstointerface_ip_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('tags', nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aci_appprofiles', to='tenancy.tenant')),
            ],
            options={
                'verbose_name': 'Cisco ACI Application Profile',
                'verbose_name_plural': 'Cisco ACI Application Profiles',
                'ordering': ('name',),
                'unique_together': {('tenant', 'name')},
            },
            bases=(models.Model, nautobot.extras.models.mixins.DynamicGroupMixin, nautobot.extras.models.mixins.NotesMixin),
        ),
        migrations.CreateModel(
            name='BridgeDomain',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('ip_addresses', models.ManyToManyField(blank=True, related_name='aci_bridgedomains', to='ipam.IPAddress')),
                ('tags', nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aci_bridgedomains', to='tenancy.tenant')),
                ('vrf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aci_bridgedomains', to='ipam.vrf')),
            ],
            options={
                'verbose_name': 'Cisco ACI Bridge Domain',
                'verbose_name_plural': 'Cisco ACI Bridge Domains',
                'ordering': ('name',),
                'unique_together': {('vrf', 'name', 'tenant')},
            },
            bases=(models.Model, nautobot.extras.models.mixins.DynamicGroupMixin, nautobot.extras.models.mixins.NotesMixin),
        ),
        migrations.CreateModel(
            name='EPG',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aci_epgs', to='nautobot_app_cisco_sdn.applicationprofile')),
                ('bridge_domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aci_epgs', to='nautobot_app_cisco_sdn.bridgedomain')),
                ('tags', nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aci_epgs', to='tenancy.tenant')),
            ],
            options={
                'verbose_name': 'Cisco ACI EPG',
                'verbose_name_plural': 'Cisco ACI EPGs',
                'ordering': ('name',),
                'unique_together': {('name', 'application', 'tenant')},
            },
            bases=(models.Model, nautobot.extras.models.mixins.DynamicGroupMixin, nautobot.extras.models.mixins.NotesMixin),
        ),
        migrations.CreateModel(
            name='ApplicationTermination',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('epg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aci_appterminations', to='nautobot_app_cisco_sdn.epg')),
                ('interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aci_appterminations', to='dcim.interface')),
                ('tags', nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag')),
                ('vlan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aci_appterminations', to='ipam.vlan')),
            ],
            options={
                'verbose_name': 'Cisco ACI App Termination',
                'verbose_name_plural': 'Cisco ACI App Termination',
                'ordering': ('name',),
                'unique_together': {('epg', 'interface', 'vlan')},
            },
            bases=(models.Model, nautobot.extras.models.mixins.DynamicGroupMixin, nautobot.extras.models.mixins.NotesMixin),
        ),
    ]
