from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from datetime import datetime
from rest_framework.views import APIView
from rest_framework import serializers
from django.db.models import Q
from django.utils import timezone
from rest_framework.decorators import api_view
from django.db import transaction
from django.db import models
from django.shortcuts import get_object_or_404
from django.http import Http404
from medicify_project.models import * 
from medicify_project.serializers import *

# Create your views here.

######################### DOCTOR APPOINTMENT ###################################
###################### GET ##################
@api_view(['GET'])
def get_doctor_appointments(request):
    response_data = {
        'message_code': 999,
        'message_text': 'Functional part is commented.',
        'message_data': [],
        'message_debug': ""
    }

    doctor_id = request.GET.get('Doctor_Id', '')
    appointment_date_time = request.GET.get('Appointment_DateTime', '')

    if not doctor_id:
        response_data = {'message_code': 999, 'message_text': 'Doctor id is required.'}
    elif not appointment_date_time:
        response_data = {'message_code': 999, 'message_text': 'Appointment Date and Time is required.'}
    else:
        try:
            # Convert provided datetime to start and end timestamps
            appointment_date_time_s = datetime.strptime(appointment_date_time, '%Y-%m-%d %H:%M:%S').replace(hour=0, minute=0, second=0)
            appointment_date_time_e = datetime.strptime(appointment_date_time, '%Y-%m-%d %H:%M:%S').replace(hour=23, minute=59, second=59)

            # Fetch data using Django ORM
            appointments = Tbldoctorappointments.objects.filter(
                Q(appointment_datetime__gte=appointment_date_time_s.timestamp()) &
                Q(appointment_datetime__lte=appointment_date_time_e.timestamp()) &
                Q(doctor_id=doctor_id) &
                Q(isdeleted=0)
            )

            # Serialize the data
            serializer = TbldoctorappointmentsSerializer(appointments, many=True)
            result = serializer.data

            if result:
                response_data = {
                    'message_code': 1000,
                    'message_text': "Appointment information retrieved successfully.",
                    'message_data': result,
                    'message_debug': ""
                }
            else:
                response_data = {
                    'message_code': 999,
                    'message_text': "Appointments for this doctor ID not found.",
                    'message_data': [],
                    'message_debug': ""
                }

        except Exception as e:
            response_data = {'message_code': 999, 'message_text': f"Error: {str(e)}"}

    return Response(response_data, status=status.HTTP_200_OK)

###################### Update ##################
@api_view(['POST'])
def update_appointment_status(request):
    response_data = {
        'message_code': 999,
        'message_text': 'Functional part is commented.',
        'message_data': [],
        'message_debug': ""
    }

    # Extract data from request
    appointment_id = request.data.get('appointment_id', '')
    appointment_status = request.data.get('appointment_status', '')

    # Validate appointment_id
    if not appointment_id:
        response_data = {'message_code': 999,'message_text': 'Appointment Id is required'}

    # Validate appointment_status
    elif not appointment_status:
        response_data = {'message_code': 999,'message_text': 'Appointment Status is required'}
         
    else:
        try:
            # Retrieve the appointment instance using ORM
            appointment = Tbldoctorappointments.objects.get(appointment_id=appointment_id)

            # Update the appointment status
            appointment.appointment_status = appointment_status
            appointment.save()

            response_data = {
                'message_code': 1000,
                'message_text': 'Appointment Status updated successfully',
                'message_data':"Appointment Id: "+ str(appointment_id),
                'message_debug': ""
            }

        except Tbldoctorappointments.DoesNotExist:
            response_data = {'message_code': 999, 'message_text': 'Appointment not found'}

        except Exception as e:
            response_data = {'message_code': 999, 'message_text': f'Error: {str(e)}'}

    return Response(response_data, status=status.HTTP_200_OK)

###################### DELETE ##################
@api_view(['DELETE'])
def cancel_appointment(request):
    response_data = {
        'message_code': 999,
        'message_text': 'Functional part is commented.',
        'message_data': [],
        'message_debug': ""
    }

    # Extract data from request
    appointment_id = request.data.get('appointment_id', None)

    # Validate appointment_id
    if not appointment_id:
        response_data={'message_code': 999, 'message_text': 'Appointment id is required'}
    
    else:
        try:
            # Retrieve the appointment instance using ORM
            appointment = Tbldoctorappointments.objects.get(appointment_id=appointment_id)

            # Set IsDeleted flag to 1
            appointment.isdeleted = 1
            appointment.save()

            response_data = {
                'message_code': 1000,
                'message_text': 'Appointment Cancelled successfully',
                'message_data': "Appointment Id: "+ str(appointment_id),
                'message_debug': ""
            }

        except Tbldoctorappointments.DoesNotExist:
            response_data = {'message_code': 999, 'message_text': 'Appointment not found'}

        except Exception as e:
            response_data = {'message_code': 999, 'message_text': f'Error: {str(e)}'}

    return Response(response_data, status=status.HTTP_200_OK)

###################### INSERT ##################
@api_view(['POST'])
@transaction.atomic
def insert_appointment_data(request):
    response_data = {
        'message_code': 999,
        'message_text': 'Functional part is commented.',
        'message_data': {},
        'message_debug': ""
    }

    # Validations for required fields
    required_fields = ['Doctor_Id', 'Appointment_DateTime', 'Appointment_Name', 'Appointment_MobileNo', 'Appointment_Gender']
    missing_fields = [field for field in required_fields if not request.data.get(field)]

    if missing_fields:
        response_data['message_code'] = 999
        response_data['message_text'] = 'Failure'
        response_data['message_data'] = {f"Missing required fields: {', '.join(missing_fields)}"}

    else:
        try:
            # Convert the provided date and time to epoch time
            epoch_time = int(datetime.strptime(request.data.get('Appointment_DateTime'), '%Y-%m-%d %H:%M:%S').timestamp())

            # Get the maximum appointment token from the database
            max_appointment_token = Tbldoctorappointments.objects.filter(
                doctor_id=request.data.get('Doctor_Id'),
                appointment_datetime=epoch_time
            ).aggregate(max_token=models.Max('appointment_token'))['max_token']

            # Calculate the new appointment token
            appointment_token = max_appointment_token + 1 if max_appointment_token is not None else 1

            # Map gender to 0 for male and 1 for female
            gender_mapping = {'Male': 0, 'Female': 1}
            appointment_gender = gender_mapping.get(request.data.get('Appointment_Gender'), None)

            if appointment_gender is None:
                response_data['message_code'] = 999
                response_data['message_text'] = 'Failure'
                response_data['message_data'] = {'Invalid gender value'}
            else:
                # Create a new appointment instance using the ORM model
                new_appointment = Tbldoctorappointments(
                    doctor_id=request.data.get('Doctor_Id'),
                    appointment_datetime=epoch_time,
                    appointment_name=request.data.get('Appointment_Name'),
                    appointment_mobileno=request.data.get('Appointment_MobileNo'),
                    appointment_gender=appointment_gender,
                    appointment_token=appointment_token,
                    appointment_status=1,
                    isdeleted=0
                )

                # Save the new appointment instance
                new_appointment.save()

                response_data['message_code'] = 1000
                response_data['message_text'] = 'Data inserted successfully'

        except Exception as e:
            response_data['message_code'] = 500
            response_data['message_text'] = f'Error: {str(e)}'

    return Response(response_data, status=status.HTTP_200_OK)
