from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Company, Vacancy
import json
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer, VacancySerializer


@api_view(['GET', 'POST'])
@csrf_exempt
def get_companies(request):
    try:
        companies = Company.objects.all()
    except Company.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def get_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        company.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@csrf_exempt
def get_company_vacancies(request, company_id):
    try:
        vacs = Vacancy.objects.filter(company_id=company_id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    serializer = VacancySerializer(vacs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class VacanciesAPIView(APIView):
    def get(self, request):
        try:
            vacancies = Vacancy.objects.all()
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacancyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Vacancy.objects.get(id=pk)
        except Vacancy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vacancy = self.get_object(pk)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        vacancy = self.get_object(pk)
        ser = VacancySerializer(instance=vacancy, data=request.data)
        if (ser.is_valid()):
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk=None):
        vacancy = self.get_object(pk)
        vacancy.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@csrf_exempt
def get_top_ten_vacancies(request):
    try:
        vacancies = Vacancy.objects.all().order_by("-salary")[:10]
    except Company.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    serializer = VacancySerializer(vacancies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


