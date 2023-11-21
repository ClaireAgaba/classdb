# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Branch(models.Model):
    branchno = models.CharField(db_column='BranchNo', primary_key=True, max_length=5)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=25, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=25, blank=True, null=True)  # Field name made lowercase.
    telno = models.IntegerField(db_column='TelNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'branch'


class Member(models.Model):
    memberno = models.CharField(db_column='MemberNo', primary_key=True, max_length=5)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=25, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    branchno = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member'


class Rental(models.Model):
    rentalno = models.CharField(db_column='RentalNo', primary_key=True, max_length=5)  # Field name made lowercase.
    memberno = models.ForeignKey(Member, models.DO_NOTHING, db_column='MemberNo', blank=True, null=True)  # Field name made lowercase.
    videono = models.ForeignKey('Video', models.DO_NOTHING, db_column='VideoNo', to_field='VideoNo', blank=True, null=True)  # Field name made lowercase.
    branchno = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchNo', blank=True, null=True)  # Field name made lowercase.
    rentaldate = models.DateField(db_column='RentalDate', blank=True, null=True)  # Field name made lowercase.
    returndate = models.DateField(db_column='ReturnDate', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rental'


class Staff(models.Model):
    staffno = models.CharField(db_column='StaffNo', primary_key=True, max_length=5)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=25, blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    branchno = models.ForeignKey(Branch, models.DO_NOTHING, db_column='BranchNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staff'


class Video(models.Model):
    catalogno = models.CharField(db_column='CatalogNo', primary_key=True, max_length=5)  # Field name made lowercase.
    videono = models.CharField(db_column='VideoNo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dailyrental = models.IntegerField(db_column='DailyRental', blank=True, null=True)  # Field name made lowercase.
    cost = models.IntegerField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    movieyear = models.TextField(db_column='MovieYear', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'video'
