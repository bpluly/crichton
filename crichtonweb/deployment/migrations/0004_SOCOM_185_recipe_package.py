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
        
        # Adding model 'RecipePackage'
        db.create_table('deployment_recipepackage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(related_name='packages', to=orm['deployment.Recipe'])),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recipes', to=orm['package.PackageName'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('deployment', ['RecipePackage'])

        # Adding unique constraint on 'RecipePackage', fields ['recipe', 'package']
        db.create_unique('deployment_recipepackage', ['recipe_id', 'package_id'])

        # Adding model 'RecipePackageAuditLogEntry'
        db.create_table('deployment_recipepackageauditlogentry', (
            ('id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_auditlog_packages', to=orm['deployment.Recipe'])),
            ('package', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_auditlog_recipes', to=orm['package.PackageName'])),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('action_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('action_user', self.gf('audit_log.models.fields.LastUserField')(related_name='_recipepackage_audit_log_entry')),
            ('action_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('deployment', ['RecipePackageAuditLogEntry'])

        # Removing M2M table for field packages on 'Recipe'
        db.delete_table('deployment_recipe_packages')


    def backwards(self, orm):
        
        # Removing unique constraint on 'RecipePackage', fields ['recipe', 'package']
        db.delete_unique('deployment_recipepackage', ['recipe_id', 'package_id'])

        # Deleting model 'RecipePackage'
        db.delete_table('deployment_recipepackage')

        # Deleting model 'RecipePackageAuditLogEntry'
        db.delete_table('deployment_recipepackageauditlogentry')

        # Adding M2M table for field packages on 'Recipe'
        db.create_table('deployment_recipe_packages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['deployment.recipe'], null=False)),
            ('packagename', models.ForeignKey(orm['package.packagename'], null=False))
        ))
        db.create_unique('deployment_recipe_packages', ['recipe_id', 'packagename_id'])


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
        'deployment.applicationdeployment': {
            'Meta': {'ordering': "('insert_date',)", 'object_name': 'ApplicationDeployment'},
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'application_deployments'", 'null': 'True', 'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'log': ('core.fields.CompressedTextField', [], {'null': 'True', 'blank': 'True'}),
            'pool': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'deployments'", 'null': 'True', 'to': "orm['system.Pool']"}),
            'product_deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'application_deployments'", 'null': 'True', 'to': "orm['deployment.ProductDeployment']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deployments'", 'to': "orm['deployment.Recipe']"})
        },
        'deployment.deploymentpreference': {
            'Meta': {'ordering': "('environment', 'preference_number')", 'unique_together': "(('environment', 'preference_number'),)", 'object_name': 'DeploymentPreference'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deployment_system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'environment_usages'", 'to': "orm['deployment.DeploymentSystem']"}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deployment_preferences'", 'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preference_number': ('django.db.models.fields.SmallIntegerField', [], {'default': '999'})
        },
        'deployment.deploymentpreferenceauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'DeploymentPreferenceAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_deploymentpreference_audit_log_entry'"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deployment_system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_environment_usages'", 'to': "orm['deployment.DeploymentSystem']"}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_deployment_preferences'", 'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'preference_number': ('django.db.models.fields.SmallIntegerField', [], {'default': '999'})
        },
        'deployment.deploymentsystem': {
            'Meta': {'ordering': "('name',)", 'object_name': 'DeploymentSystem'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deployment_system_type': ('django.db.models.fields.CharField', [], {'default': "'puppet'", 'max_length': '12'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'takes_specific_pool': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'takes_specific_version': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        'deployment.deploymentsystemauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'DeploymentSystemAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_deploymentsystem_audit_log_entry'"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deployment_system_type': ('django.db.models.fields.CharField', [], {'default': "'puppet'", 'max_length': '12'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'takes_specific_pool': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'takes_specific_version': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        'deployment.nodedeployment': {
            'Meta': {'ordering': "('started',)", 'object_name': 'NodeDeployment'},
            'application_deployment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'node_deployments'", 'to': "orm['deployment.ApplicationDeployment']"}),
            'finished': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('core.fields.CompressedTextField', [], {'null': 'True', 'blank': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deployments'", 'to': "orm['system.Node']"}),
            'started': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'succeeded': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'deployment.productdeployment': {
            'Meta': {'ordering': "('insert_date',)", 'object_name': 'ProductDeployment'},
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'product_deployments'", 'null': 'True', 'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'log': ('core.fields.CompressedTextField', [], {'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deployments'", 'to': "orm['prodmgmt.Product']"})
        },
        'deployment.recipe': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('name', 'deployment_system'),)", 'object_name': 'Recipe'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deployment_system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipes'", 'to': "orm['deployment.DeploymentSystem']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'deployment.recipeauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'RecipeAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_recipe_audit_log_entry'"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deployment_system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_recipes'", 'to': "orm['deployment.DeploymentSystem']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'deployment.recipepackage': {
            'Meta': {'unique_together': "(('recipe', 'package'),)", 'object_name': 'RecipePackage'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipes'", 'to': "orm['package.PackageName']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'packages'", 'to': "orm['deployment.Recipe']"})
        },
        'deployment.recipepackageauditlogentry': {
            'Meta': {'ordering': "('-action_date',)", 'object_name': 'RecipePackageAuditLogEntry'},
            'action_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'action_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'action_user': ('audit_log.models.fields.LastUserField', [], {'related_name': "'_recipepackage_audit_log_entry'"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'package': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_recipes'", 'to': "orm['package.PackageName']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_auditlog_packages'", 'to': "orm['deployment.Recipe']"})
        },
        'issue.issue': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('name', 'project'),)", 'object_name': 'Issue'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issues'", 'to': "orm['issue.IssueTrackerProject']"}),
            'summary': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
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
        'package.packagename': {
            'Meta': {'ordering': "('name',)", 'object_name': 'PackageName'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
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
        'system.node': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Node'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_virtual': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'system.pool': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Pool'},
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'environment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pools'", 'to': "orm['system.Environment']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pools'", 'to': "orm['system.Role']"})
        },
        'system.role': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Role'},
            'applications': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'roles'", 'blank': 'True', 'to': "orm['prodmgmt.Application']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'})
        }
    }

    complete_apps = ['deployment']
