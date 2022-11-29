from django.db import models

# Create your models here.
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)
class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
        
class TblCasesummary(models.Model):
    csummaryid = models.AutoField(db_column='CSummaryId', primary_key=True)  # Field name made lowercase.
    casedetailid = models.IntegerField(db_column='CaseDetailId')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate')  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_CaseSummary'


class TblCasetypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    casetypes = models.TextField(db_column='CaseTypes', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_CaseTypes'
    def __str__(self):
        return self.casetypes





class TblCompany(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    company = models.TextField(db_column='Company', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    code = models.TextField(db_column='Code', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.      

    class Meta:
        managed = False
        db_table = 'tbl_Company'

    def __str__(self):
        return self.code


class TblDepartment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    department = models.TextField(db_column='Department', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Department'


class TblDesignation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    designation = models.TextField(db_column='Designation', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    departmentid = models.IntegerField(db_column='DepartmentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Designation'


class TblDivisions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    divisions = models.TextField(db_column='Divisions', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Divisions'


class TblDocuments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    caseid = models.IntegerField(db_column='CaseId')  # Field name made lowercase.
    casedetailid = models.IntegerField(db_column='CaseDetailId')  # Field name made lowercase.
    casesummaryid = models.IntegerField(db_column='CaseSummaryId')  # Field name made lowercase.
    documentdata = models.BinaryField(db_column='DocumentData')  # Field name made lowercase.
    documentname = models.TextField(db_column='DocumentName', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    doctype = models.TextField(db_column='DocType', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    uploadeddate = models.DateTimeField(db_column='UploadedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Documents'


class TblPriority(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Priority'
    def __str__(self):
        return self.priority


class TblUser(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.TextField(db_column='UserName', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    password = models.TextField(db_column='Password', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    email = models.TextField(db_column='Email', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    designationid = models.IntegerField(db_column='DesignationID')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    companyid = models.IntegerField(db_column='CompanyID')  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    membertype = models.TextField(db_column='MemberType', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_User'
    # def __str__(self):
    #     return self.name

class TblCases(models.Model):
    caseid = models.AutoField(db_column='CaseId', primary_key=True)  # Field name made lowercase.
    casecode = models.CharField(db_column='CaseCode', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    topic = models.TextField(db_column='Topic', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    priority = models.ForeignKey(TblPriority,on_delete=models.CASCADE,db_column='Priority')  # Field name made lowercase.
    userid = models.ForeignKey(TblUser,on_delete=models.CASCADE,db_column='UserID',related_name='assigned_by')  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate')  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified')  # Field name made lowercase.
    assigneddpt = models.IntegerField(db_column='AssignedDpt')  # Field name made lowercase.
    casetype = models.ForeignKey(TblCasetypes,on_delete=models.CASCADE,db_column='CaseType')  # Field name made lowercase.
    assignedto = models.ForeignKey(TblUser,on_delete=models.CASCADE,db_column='AssignedTo', blank=True, null=True,related_name='assigned_to')  # Field name made lowercase.
    companyid = models.ForeignKey(TblCompany,on_delete=models.CASCADE,db_column='CompanyId', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Cases'

class TblCasedetails(models.Model):
    casedetailid = models.AutoField(db_column='CaseDetailId', primary_key=True)  # Field name made lowercase.
    caseid = models.IntegerField(db_column='CaseId')  # Field name made lowercase.
    topic = models.TextField(db_column='Topic', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate')  # Field name made lowercase.
    modified = models.DateTimeField(db_column='Modified')  # Field name made lowercase.
    iscompleted = models.IntegerField(db_column='IsCompleted')  # Field name made lowercase.
    completiondate = models.DateTimeField(db_column='CompletionDate', blank=True, null=True)  # Field name made lowercase.
    expcompletion = models.DateTimeField(db_column='ExpCompletion', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    userid = models.ForeignKey(TblUser,on_delete=models.CASCADE,db_column='UserId')  # Field name made lowercase.
    priority = models.ForeignKey(TblPriority,on_delete=models.CASCADE,db_column='Priority')  # Field name made lowercase.
    casetype = models.ForeignKey(TblCasetypes,on_delete=models.CASCADE,db_column='CaseType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_CaseDetails'