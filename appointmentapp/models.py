# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class Tblconsultations(models.Model):
#     consultation_id = models.AutoField(db_column='Consultation_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     patient_status = models.SmallIntegerField(db_column='Patient_Status')  # Field name made lowercase.
#     consultation_datetime = models.IntegerField(db_column='Consultation_DateTime')  # Field name made lowercase.
#     consultation_mode = models.SmallIntegerField(db_column='Consultation_Mode')  # Field name made lowercase.
#     visit_reason = models.CharField(db_column='Visit_Reason', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     consultation_duration = models.IntegerField(db_column='Consultation_Duration', blank=True, null=True)  # Field name made lowercase.
#     further_assited = models.IntegerField(db_column='Further_Assited')  # Field name made lowercase.
#     followup_datetime = models.IntegerField(db_column='Followup_DateTime', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deleted_reason = models.CharField(db_column='Deleted_Reason', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblconsultations'


# class Tbldatacodemaster(models.Model):
#     datacodeid = models.AutoField(db_column='DataCodeId', primary_key=True)  # Field name made lowercase.
#     datacodename = models.CharField(db_column='DataCodeName', max_length=20)  # Field name made lowercase.
#     datacodevalue = models.CharField(db_column='DataCodeValue', max_length=5)  # Field name made lowercase.
#     datacodedescription = models.TextField(db_column='DataCodeDescription')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tbldatacodemaster'


# class TbldoctorMedicines(models.Model):
#     doctor_medicine_id = models.AutoField(db_column='Doctor_Medicine_Id', primary_key=True)  # Field name made lowercase.
#     medicine_code = models.CharField(db_column='Medicine_Code', max_length=5)  # Field name made lowercase.
#     medicine_name = models.CharField(db_column='Medicine_Name', max_length=100)  # Field name made lowercase.
#     medicine_form = models.SmallIntegerField(db_column='Medicine_Form')  # Field name made lowercase.
#     medicine_frequency = models.CharField(db_column='Medicine_Frequency', max_length=3)  # Field name made lowercase.
#     medicine_duration = models.IntegerField(db_column='Medicine_Duration')  # Field name made lowercase.
#     medicine_dosages = models.IntegerField(db_column='Medicine_Dosages')  # Field name made lowercase.
#     medicine_manufacture = models.CharField(db_column='Medicine_Manufacture', max_length=100)  # Field name made lowercase.
#     medicine_packsize = models.IntegerField(db_column='Medicine_PackSize')  # Field name made lowercase.
#     medicine_preservation = models.IntegerField(db_column='Medicine_Preservation')  # Field name made lowercase.
#     medicine_minstock = models.IntegerField(db_column='Medicine_MinStock')  # Field name made lowercase.
#     medicine_gst = models.IntegerField(db_column='Medicine_GST')  # Field name made lowercase.
#     medicine_content_name = models.CharField(db_column='Medicine_Content_Name', max_length=100)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deletedreason = models.CharField(db_column='DeletedReason', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tbldoctor_medicines'


# class Tbldoctorappointments(models.Model):
#     appointment_id = models.AutoField(db_column='Appointment_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     appointment_datetime = models.BigIntegerField(db_column='Appointment_DateTime')  # Field name made lowercase.
#     appointment_token = models.IntegerField(db_column='Appointment_Token')  # Field name made lowercase.
#     appointment_name = models.CharField(db_column='Appointment_Name', max_length=100)  # Field name made lowercase.
#     appointment_mobileno = models.CharField(db_column='Appointment_MobileNo', max_length=10)  # Field name made lowercase.
#     appointment_gender = models.IntegerField(db_column='Appointment_Gender')  # Field name made lowercase.
#     appointment_status = models.IntegerField(db_column='Appointment_Status')  # Field name made lowercase.
#     consultation_id = models.IntegerField(db_column='Consultation_Id', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tbldoctorappointments'


# class Tbldoctorlocationavailability(models.Model):
#     doctor_location_availability_id = models.AutoField(db_column='Doctor_Location_Availability_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     doctor_location_id = models.IntegerField(db_column='Doctor_Location_Id')  # Field name made lowercase.
#     availability_day = models.SmallIntegerField(db_column='Availability_Day')  # Field name made lowercase.
#     availability_starttime = models.CharField(db_column='Availability_StartTime', max_length=8)  # Field name made lowercase.
#     availability_endtime = models.IntegerField(db_column='Availability_EndTime')  # Field name made lowercase.
#     availability_status = models.IntegerField(db_column='Availability_Status')  # Field name made lowercase.
#     availability_order = models.IntegerField(db_column='Availability_Order')  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deletedreason = models.IntegerField(db_column='DeletedReason', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tbldoctorlocationavailability'


# class Tbldoctorlocations(models.Model):
#     doctor_location_id = models.AutoField(db_column='Doctor_Location_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     location_title = models.CharField(db_column='Location_Title', max_length=100)  # Field name made lowercase.
#     location_type = models.IntegerField(db_column='Location_Type')  # Field name made lowercase.
#     location_address = models.CharField(db_column='Location_Address', max_length=255)  # Field name made lowercase.
#     location_latitute = models.CharField(db_column='Location_Latitute', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     location_longitute = models.CharField(db_column='Location_Longitute', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     location_city_id = models.IntegerField(db_column='Location_City_Id')  # Field name made lowercase.
#     location_state_id = models.IntegerField(db_column='Location_State_Id')  # Field name made lowercase.
#     location_country_id = models.IntegerField(db_column='Location_Country_Id')  # Field name made lowercase.
#     location_pincode = models.CharField(db_column='Location_Pincode', max_length=6)  # Field name made lowercase.
#     location_status = models.IntegerField(db_column='Location_Status')  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deletedreason = models.CharField(db_column='DeletedReason', max_length=200, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tbldoctorlocations'


# class Tbldoctors(models.Model):
#     doctor_id = models.AutoField(db_column='Doctor_Id', primary_key=True)  # Field name made lowercase.
#     doctor_firstname = models.CharField(db_column='Doctor_Firstname', max_length=50)  # Field name made lowercase.
#     doctor_lastname = models.CharField(db_column='Doctor_Lastname', max_length=50)  # Field name made lowercase.
#     doctor_mobileno = models.CharField(db_column='Doctor_MobileNo', max_length=10)  # Field name made lowercase.
#     doctor_email = models.CharField(db_column='Doctor_Email', max_length=100)  # Field name made lowercase.
#     doctor_dateofbirth = models.IntegerField(db_column='Doctor_DateofBirth', blank=True, null=True)  # Field name made lowercase.
#     doctor_maritalstatus = models.IntegerField(db_column='Doctor_MaritalStatus')  # Field name made lowercase.
#     doctor_gender = models.SmallIntegerField(db_column='Doctor_Gender')  # Field name made lowercase.
#     doctor_aadharnumber = models.CharField(db_column='Doctor_AadharNumber', max_length=16)  # Field name made lowercase.
#     doctor_address = models.CharField(db_column='Doctor_Address', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     doctor_cityid = models.IntegerField(db_column='Doctor_CityId', blank=True, null=True)  # Field name made lowercase.
#     doctor_stateid = models.IntegerField(db_column='Doctor_StateId', blank=True, null=True)  # Field name made lowercase.
#     doctor_countryid = models.IntegerField(db_column='Doctor_CountryId', blank=True, null=True)  # Field name made lowercase.
#     doctor_pincode = models.CharField(db_column='Doctor_Pincode', max_length=6, blank=True, null=True)  # Field name made lowercase.
#     doctor_registrationno = models.CharField(db_column='Doctor_RegistrationNo', max_length=50)  # Field name made lowercase.
#     doctor_profilleimageurl = models.IntegerField(db_column='Doctor_ProfilleImageURL', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tbldoctors'


# class TblmedicineInstructions(models.Model):
#     doctor_instruction_id = models.AutoField(db_column='Doctor_Instruction_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     instruction_language = models.CharField(db_column='Instruction_Language', max_length=2)  # Field name made lowercase.
#     instruction_text = models.CharField(db_column='Instruction_Text', max_length=100, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblmedicine_instructions'


# class TblpateintCharges(models.Model):
#     pateint_charges_id = models.AutoField(db_column='Pateint_Charges_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     patient_status = models.IntegerField(db_column='Patient_Status')  # Field name made lowercase.
#     charges_referencetype = models.IntegerField(db_column='Charges_ReferenceType')  # Field name made lowercase.
#     charges_reference_id = models.IntegerField(db_column='Charges_Reference_Id')  # Field name made lowercase.
#     charges_type = models.IntegerField(db_column='Charges_Type')  # Field name made lowercase.
#     charges_category = models.IntegerField(db_column='Charges_Category')  # Field name made lowercase.
#     charges_notes = models.CharField(db_column='Charges_Notes', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     charges_units = models.IntegerField(db_column='Charges_Units')  # Field name made lowercase.
#     charges_rate = models.IntegerField(db_column='Charges_Rate')  # Field name made lowercase.
#     charges_amount = models.IntegerField(db_column='Charges_Amount')  # Field name made lowercase.
#     charges_discount = models.IntegerField(db_column='Charges_Discount', blank=True, null=True)  # Field name made lowercase.
#     charges_discount_reason = models.IntegerField(db_column='Charges_Discount_Reason', blank=True, null=True)  # Field name made lowercase.
#     charges_discountby = models.CharField(db_column='Charges_DiscountBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deleted_reason = models.IntegerField(db_column='Deleted_Reason', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblpateint_charges'


# class TblpatientComplaints(models.Model):
#     patient_complaint_id = models.AutoField(db_column='Patient_Complaint_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     complaint_datetime = models.IntegerField(db_column='Complaint_DateTime')  # Field name made lowercase.
#     complaint_details = models.TextField(db_column='Complaint_Details')  # Field name made lowercase.
#     appointment_id = models.IntegerField(db_column='Appointment_Id', blank=True, null=True)  # Field name made lowercase.
#     consultation_id = models.IntegerField(db_column='Consultation_Id', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deleted_reason = models.IntegerField(db_column='Deleted_Reason', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblpatient_complaints'


# class TblpatientFindingsandsymtoms(models.Model):
#     patient_findings_id = models.AutoField(db_column='Patient_Findings_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     patient_status = models.SmallIntegerField(db_column='Patient_Status')  # Field name made lowercase.
#     findgings_datetime = models.IntegerField(db_column='Findgings_DateTime')  # Field name made lowercase.
#     consultation_id = models.IntegerField(db_column='Consultation_Id', blank=True, null=True)  # Field name made lowercase.
#     findings = models.TextField(db_column='Findings')  # Field name made lowercase.
#     symtoms = models.TextField(db_column='Symtoms')  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deleted_reason = models.CharField(db_column='Deleted_Reason', max_length=100)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblpatient_findingsandsymtoms'


# class TblpatientLabinvestigations(models.Model):
#     patient_labinvestigation_id = models.AutoField(db_column='Patient_LabInvestigation_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     patient_status = models.IntegerField(db_column='Patient_Status')  # Field name made lowercase.
#     consultation_id = models.IntegerField(db_column='Consultation_Id')  # Field name made lowercase.
#     prescription_id = models.IntegerField(db_column='Prescription_Id')  # Field name made lowercase.
#     labinvestigation_datetime = models.IntegerField(db_column='LabInvestigation_DateTime')  # Field name made lowercase.
#     labinvestigation_category = models.IntegerField(db_column='LabInvestigation_Category')  # Field name made lowercase.
#     patient_labtestid = models.IntegerField(db_column='Patient_LabTestId')  # Field name made lowercase.
#     patient_labtestreport = models.CharField(db_column='Patient_LabTestReport', max_length=100)  # Field name made lowercase.
#     patient_labtestsample = models.IntegerField(db_column='Patient_LabTestSample')  # Field name made lowercase.
#     patient_labtestreport_check = models.IntegerField(db_column='Patient_LabTestReport_Check')  # Field name made lowercase.
#     lattest_extrafield1 = models.IntegerField(db_column='LatTest_ExtraField1', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     deletedon = models.IntegerField(db_column='DeletedOn', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deleted_reason = models.CharField(db_column='Deleted_Reason', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblpatient_labinvestigations'


# class TblpatientMedications(models.Model):
#     patient_medication_id = models.AutoField(db_column='Patient_Medication_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     patient_status = models.IntegerField(db_column='Patient_Status')  # Field name made lowercase.
#     consultation_id = models.IntegerField(db_column='Consultation_Id')  # Field name made lowercase.
#     prescription_id = models.IntegerField(db_column='Prescription_Id')  # Field name made lowercase.
#     medication_datetime = models.IntegerField(db_column='Medication_DateTime')  # Field name made lowercase.
#     medicine_id = models.IntegerField(db_column='Medicine_Id')  # Field name made lowercase.
#     medicine_form = models.CharField(db_column='Medicine_Form', max_length=5)  # Field name made lowercase.
#     medicine_name = models.CharField(db_column='Medicine_Name', max_length=100)  # Field name made lowercase.
#     medicine_duration = models.IntegerField(db_column='Medicine_Duration')  # Field name made lowercase.
#     medicine_doses = models.IntegerField(db_column='Medicine_Doses')  # Field name made lowercase.
#     medicine_dose_interval = models.CharField(db_column='Medicine_Dose_Interval', max_length=15)  # Field name made lowercase.
#     medicine_instruction_id = models.IntegerField(db_column='Medicine_Instruction_Id', blank=True, null=True)  # Field name made lowercase.
#     medicine_category = models.IntegerField(db_column='Medicine_Category', blank=True, null=True)  # Field name made lowercase.
#     medicine_extrafield1 = models.IntegerField(db_column='Medicine_ExtraField1', blank=True, null=True)  # Field name made lowercase.
#     medicine_extrafield2 = models.IntegerField(db_column='Medicine__ExtraField2', blank=True, null=True)  # Field name made lowercase. Field renamed because it contained more than one '_' in a row.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deleted_reason = models.CharField(db_column='Deleted_Reason', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblpatient_medications'


# class TblpatientPayments(models.Model):
#     patient_payment_id = models.AutoField(db_column='Patient_Payment_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     patient_status = models.IntegerField(db_column='Patient_Status')  # Field name made lowercase.
#     payment_mode = models.IntegerField(db_column='Payment_Mode')  # Field name made lowercase.
#     payment_amount = models.IntegerField(db_column='Payment_Amount')  # Field name made lowercase.
#     payment_transaction_no = models.CharField(db_column='Payment_Transaction_No', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deleted_reason = models.IntegerField(db_column='Deleted_Reason', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblpatient_payments'


# class Tblpatientbiometrics(models.Model):
#     patient_biometricid = models.AutoField(db_column='Patient_Biometricid', primary_key=True)  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     consultation_id = models.IntegerField(db_column='Consultation_Id', blank=True, null=True)  # Field name made lowercase.
#     operator_id = models.IntegerField(db_column='Operator_Id', blank=True, null=True)  # Field name made lowercase.
#     patient_status = models.IntegerField(db_column='Patient_Status')  # Field name made lowercase.
#     patient_height = models.FloatField(db_column='Patient_Height', blank=True, null=True)  # Field name made lowercase.
#     patient_weight = models.FloatField(db_column='Patient_Weight', blank=True, null=True)  # Field name made lowercase.
#     patient_bmi = models.FloatField(db_column='Patient_BMI', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblpatientbiometrics'


# class Tblpatients(models.Model):
#     patient_id = models.AutoField(db_column='Patient_Id', primary_key=True)  # Field name made lowercase.
#     patient_mobileno = models.CharField(db_column='Patient_MobileNo', max_length=10)  # Field name made lowercase.
#     patient_firstname = models.CharField(db_column='Patient_Firstname', max_length=50)  # Field name made lowercase.
#     patient_fateherhusbandname = models.CharField(db_column='Patient_FateherHusbandName', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     patient_lastname = models.CharField(db_column='Patient_Lastname', max_length=50)  # Field name made lowercase.
#     patient_gender = models.SmallIntegerField(db_column='Patient_Gender')  # Field name made lowercase.
#     patient_dateofbirth = models.BigIntegerField(db_column='Patient_DateOfBirth', blank=True, null=True)  # Field name made lowercase.
#     patient_maritalstatus = models.IntegerField(db_column='Patient_MaritalStatus')  # Field name made lowercase.
#     patient_aadharnumber = models.CharField(db_column='Patient_AadharNumber', max_length=16, blank=True, null=True)  # Field name made lowercase.
#     patient_universalhealthid = models.IntegerField(db_column='Patient_UniversalHealthId')  # Field name made lowercase.
#     patient_bloodgroup = models.IntegerField(db_column='Patient_BloodGroup')  # Field name made lowercase.
#     patient_level = models.CharField(db_column='Patient_Level', max_length=1)  # Field name made lowercase.
#     patient_emergencycontact = models.CharField(db_column='Patient_EmergencyContact', max_length=10)  # Field name made lowercase.
#     patient_address = models.CharField(db_column='Patient_Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     patient_cityid = models.IntegerField(db_column='Patient_CityId', blank=True, null=True)  # Field name made lowercase.
#     patient_stateid = models.IntegerField(db_column='Patient_StateId', blank=True, null=True)  # Field name made lowercase.
#     patient_countryid = models.IntegerField(db_column='Patient_CountryId')  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.BigIntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     istestpatient = models.IntegerField(db_column='IsTestPatient')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblpatients'


# class Tblpatientvitals(models.Model):
#     patient_biometricid = models.AutoField(db_column='Patient_Biometricid', primary_key=True)  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     consultation_id = models.IntegerField(db_column='Consultation_Id', blank=True, null=True)  # Field name made lowercase.
#     operator_id = models.IntegerField(db_column='Operator_Id', blank=True, null=True)  # Field name made lowercase.
#     patient_status = models.IntegerField(db_column='Patient_Status')  # Field name made lowercase.
#     patient_heartratepluse = models.FloatField(db_column='Patient_HeartRatePluse')  # Field name made lowercase.
#     patient_bpsystolic = models.FloatField(db_column='Patient_BPSystolic')  # Field name made lowercase.
#     patient_bpdistolic = models.FloatField(db_column='Patient_BPDistolic')  # Field name made lowercase.
#     patient_painscale = models.FloatField(db_column='Patient_PainScale')  # Field name made lowercase.
#     patient_respiratoryrate = models.FloatField(db_column='Patient_RespiratoryRate')  # Field name made lowercase.
#     patient_temparature = models.FloatField(db_column='Patient_Temparature')  # Field name made lowercase.
#     patient_chest = models.CharField(db_column='Patient_Chest', max_length=100)  # Field name made lowercase.
#     patient_ecg = models.CharField(db_column='Patient_ECG', max_length=100)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblpatientvitals'


# class Tblprescriptions(models.Model):
#     prescriptions_id = models.AutoField(db_column='Prescriptions_Id', primary_key=True)  # Field name made lowercase.
#     doctor_id = models.IntegerField(db_column='Doctor_Id')  # Field name made lowercase.
#     patient_id = models.IntegerField(db_column='Patient_Id')  # Field name made lowercase.
#     patient_status = models.IntegerField(db_column='Patient_Status')  # Field name made lowercase.
#     consultation_id = models.IntegerField(db_column='Consultation_Id')  # Field name made lowercase.
#     prescription_datetime = models.IntegerField(db_column='Prescription_DateTime')  # Field name made lowercase.
#     prescription_details = models.TextField(db_column='Prescription_Details', blank=True, null=True)  # Field name made lowercase.
#     createdon = models.IntegerField(db_column='CreatedOn', blank=True, null=True)  # Field name made lowercase.
#     createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedon = models.IntegerField(db_column='LastModifiedOn', blank=True, null=True)  # Field name made lowercase.
#     lastmodifiedby = models.IntegerField(db_column='LastModifiedBy', blank=True, null=True)  # Field name made lowercase.
#     isdeleted = models.IntegerField(db_column='IsDeleted', blank=True, null=True)  # Field name made lowercase.
#     deletedby = models.IntegerField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.
#     deleted_reason = models.IntegerField(db_column='Deleted_Reason', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'tblprescriptions'
