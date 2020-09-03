from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError
import requests
import random
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, ListModelMixin
# Create your views here.


class CustomResponse():
    def successResponse(self, data={}, status=status.HTTP_200_OK, description="SUCCESS"):
        return Response(
            {
                "success": True,
                "errorCode": 0,
                "message": description,
                "info": data
            }, status=status)

    def errorResponse(self, data={}, description="ERROR", errorCode=1, status=status.HTTP_400_BAD_REQUEST):
        return Response(
            {
                "success": False,
                "errorCode": errorCode,
                "message": description,
                "info": data
            }, status=status)


class CRUDBank(generics.GenericAPIView,
               UpdateModelMixin,
               CreateModelMixin,
               ListModelMixin,
               DestroyModelMixin,
               RetrieveModelMixin):
    serializer_class = BankSerializer
    queryset = BankDetails.objects.all()
    lookup_field = "bankId"

    def get(self, request, bankId=None):
        if bankId:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, bankId=None):
        self.update(request, bankId)
        bankObj = BankDetails.objects.filter(bankId=bankId)
        serializer = BankSerializer(bankObj, many=True)
        return CustomResponse().successResponse(serializer.data, description="updated the bank Details.")

    def delete(self, request, bankId=None):
        self.destroy(request, bankId)
        return CustomResponse().successResponse(description="Deleted the bank details.")


class GetDetailsFromIFSC(generics.ListAPIView):

    def post(self, request):
        ifsc = request.data.get("ifsc", "")
        bankObj = BankDetails.objects.filter(ifsc=ifsc)
        if not bankObj:
            return CustomResponse().errorResponse(description="No such bank details present with the given IFSC")
        serializer = BankSerializer(bankObj, many=True)
        return CustomResponse().successResponse(serializer.data, description="Fetched the bank details Successfully")


class GetDetailsFromNameAndCity(generics.ListAPIView):
    def post(self, request):
        name = request.data.get("name", "")
        city = request.data.get("city", "")
        banks = BankDetails.objects.filter(bankName=name, city=city)
        if not banks:
            return CustomResponse().errorResponse(description="No such bank details present with the given details")
        serializer = BankSerializer(banks, many=True)
        return CustomResponse().successResponse(serializer.data, description="Fetched the bank details Successfully")
