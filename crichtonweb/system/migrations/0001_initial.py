# Crichton, Admirable Source Configuration Management
# Copyright 2012 British Broadcasting Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#
# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'EnvironmentAuditLogEntry'
        db.create_table('system_environmentauditlogentry', (
            ('id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128, db_index=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_environment_audit_log_entry')),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('system', ['EnvironmentAuditLogEntry'])

        # Adding model 'Environment'
        db.create_table('system_environment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('system', ['Environment'])

        # Adding model 'InternetAddress'
        db.create_table('system_internetaddress', (
            ('address', self.gf('django.db.models.fields.CharField')(max_length=45, primary_key=True)),
        ))
        db.send_create_signal('system', ['InternetAddress'])

        # Adding model 'NodeAuditLogEntry'
        db.create_table('system_nodeauditlogentry', (
            ('id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('is_virtual', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('environment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Environment'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_node_audit_log_entry')),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('system', ['NodeAuditLogEntry'])

        # Adding model 'Node'
        db.create_table('system_node', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('is_virtual', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('environment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Environment'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('system', ['Node'])

        # Adding M2M table for field internet_addresses on 'Node'
        db.create_table('system_node_internet_addresses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('node', models.ForeignKey(orm['system.node'], null=False)),
            ('internetaddress', models.ForeignKey(orm['system.internetaddress'], null=False))
        ))
        db.create_unique('system_node_internet_addresses', ['node_id', 'internetaddress_id'])

        # Adding model 'PoolAuditLogEntry'
        db.create_table('system_poolauditlogentry', (
            ('id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(max_length=128, db_index=True)),
            ('environment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_auditlog_pools', to=orm['system.Environment'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_pool_audit_log_entry')),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('system', ['PoolAuditLogEntry'])

        # Adding model 'Pool'
        db.create_table('system_pool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=128, db_index=True)),
            ('environment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pools', to=orm['system.Environment'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('system', ['Pool'])

        # Adding model 'PoolAssignmentAuditLogEntry'
        db.create_table('system_poolassignmentauditlogentry', (
            ('id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_auditlog_pool_assignments', to=orm['prodmgmt.Application'])),
            ('pool', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_auditlog_assignments', to=orm['system.Pool'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_poolassignment_audit_log_entry')),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('system', ['PoolAssignmentAuditLogEntry'])

        # Adding model 'PoolAssignment'
        db.create_table('system_poolassignment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pool_assignments', to=orm['prodmgmt.Application'])),
            ('pool', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assignments', to=orm['system.Pool'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('system', ['PoolAssignment'])

        # Adding unique constraint on 'PoolAssignment', fields ['application', 'pool']
        db.create_unique('system_poolassignment', ['application_id', 'pool_id'])

        # Adding model 'PoolMembershipAuditLogEntry'
        db.create_table('system_poolmembershipauditlogentry', (
            ('id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_auditlog_pool_memberships', to=orm['system.Node'])),
            ('pool', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_auditlog_members', to=orm['system.Pool'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_poolmembership_audit_log_entry')),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('system', ['PoolMembershipAuditLogEntry'])

        # Adding model 'PoolMembership'
        db.create_table('system_poolmembership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('node', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pool_memberships', to=orm['system.Node'])),
            ('pool', self.gf('django.db.models.fields.related.ForeignKey')(related_name='members', to=orm['system.Pool'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('system', ['PoolMembership'])

        # Adding unique constraint on 'PoolMembership', fields ['node', 'pool']
        db.create_unique('system_poolmembership', ['node_id', 'pool_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'PoolMembership', fields ['node', 'pool']
        db.delete_unique('system_poolmembership', ['node_id', 'pool_id'])

        # Removing unique constraint on 'PoolAssignment', fields ['application', 'pool']
        db.delete_unique('system_poolassignment', ['application_id', 'pool_id'])

        # Deleting model 'EnvironmentAuditLogEntry'
        db.delete_table('system_environmentauditlogentry')

        # Deleting model 'Environment'
        db.delete_table('system_environment')

        # Deleting model 'InternetAddress'
        db.delete_table('system_internetaddress')

        # Deleting model 'NodeAuditLogEntry'
        db.delete_table('system_nodeauditlogentry')

        # Deleting model 'Node'
        db.delete_table('system_node')

        # Removing M2M table for field internet_addresses on 'Node'
        db.delete_table('system_node_internet_addresses')

        # Deleting model 'PoolAuditLogEntry'
        db.delete_table('system_poolauditlogentry')

        # Deleting model 'Pool'
        db.delete_table('system_pool')

        # Deleting model 'PoolAssignmentAuditLogEntry'
        db.delete_table('system_poolassignmentauditlogentry')

        # Deleting model 'PoolAssignment'
        db.delete_table('system_poolassignment')

        # Deleting model 'PoolMembershipAuditLogEntry'
        db.delete_table('system_poolmembershipauditlogentry')

        # Deleting model 'PoolMembership'
        db.delete_table('system_poolmembership')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'issue.issue': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('name', 'project'),)", 'object_name': 'Issue'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issues'", 'to': "orm['issue.IssueTrackerProject']"})
        },
        'issue.issuetracker': {
            'Meta': {'ordering': "('name',)", 'object_name': 'IssueTracker'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_url_pattern': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'tracker_type': ('django.db.models.fields.CharField', [], {'default': "'jira'", 'max_length': '12'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        'issue.issuetrackerproject': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('name', 'issue_tracker'),)", 'object_name': 'IssueTrackerProject'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_tracker': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['issue.IssueTracker']"}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'})
        },
        'prodmgmt.application': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Application'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': "orm['prodmgmt.Product']"})
        },
        'prodmgmt.person': {
            'Meta': {'ordering': "('username',)", 'object_name': 'Person'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'distinguished_name': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'prodmgmt.product': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Product'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_products'", 'to': "orm['prodmgmt.Person']"}),
            'pipeline_issue': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': "orm['issue.Issue']"})
        },
        'system.environment': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Environment'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'system.environmentauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'EnvironmentAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_environment_audit_log_entry'"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_index': 'True'})
        },
        'system.internetaddress': {
            'Meta': {'object_name': 'InternetAddress'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '45', 'primary_key': 'True'})
        },
        'system.node': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Node'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internet_addresses': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': "orm['system.InternetAddress']"}),
            'is_virtual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'system.nodeauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'NodeAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_node_audit_log_entry'"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'is_virtual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'system.pool': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Pool'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pools'", 'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'})
        },
        'system.poolassignment': {
            'Meta': {'ordering': "('pool', 'application')", 'unique_together': "(('application', 'pool'),)", 'object_name': 'PoolAssignment'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pool_assignments'", 'to': "orm['prodmgmt.Application']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignments'", 'to': "orm['system.Pool']"})
        },
        'system.poolassignmentauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'PoolAssignmentAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_poolassignment_audit_log_entry'"}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_pool_assignments'", 'to': "orm['prodmgmt.Application']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_assignments'", 'to': "orm['system.Pool']"})
        },
        'system.poolauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'PoolAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_pool_audit_log_entry'"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_pools'", 'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'})
        },
        'system.poolmembership': {
            'Meta': {'ordering': "('pool', 'node')", 'unique_together': "(('node', 'pool'),)", 'object_name': 'PoolMembership'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pool_memberships'", 'to': "orm['system.Node']"}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'to': "orm['system.Pool']"})
        },
        'system.poolmembershipauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'PoolMembershipAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_poolmembership_audit_log_entry'"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_pool_memberships'", 'to': "orm['system.Node']"}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_members'", 'to': "orm['system.Pool']"})
        }
    }

    complete_apps = ['system']
