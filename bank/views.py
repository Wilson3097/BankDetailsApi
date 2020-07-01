from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.utils.datastructures import MultiValueDictKeyError
import requests
import random

# Create your views here.


class GetDetailsFromIFSC(generics.ListAPIView):

    def post(self, request):
        ifsc = request.data.get("ifsc", "")
        bankObj = BankDetails.objects.filter(ifsc=ifsc).first()
        if not bankObj:
            return Response({"Type": "Failed",
                             "Message": "No such bank with this IFSC code."},
                            status=status.HTTP_400_BAD_REQUEST)
        bank = []
        dic = {}
        dic['Bank Name'] = bankObj.bank_name
        dic['IFSC Code'] = bankObj.ifsc
        dic['Bank Id'] = bankObj.bank_id
        dic['branch'] = bankObj.branch
        dic['City'] = bankObj.city
        dic['State'] = bankObj.state
        dic['District'] = bankObj.district
        dic['Address'] = bankObj.address
        bank.append(dic)

        return Response({"Type": "Success",
                         "Message": "Fetched the bank details Successfully",
                         "Bank Details": bank}, status=status.HTTP_200_OK)


class GetDetailsFromNameAndCity(generics.ListAPIView):
    def post(self, request):
        name = request.data.get("name", "")
        city = request.data.get("city", "")
        banks = BankDetails.objects.filter(bank_name=name, city=city)
        if not banks:
            return Response({"Type": "Failed",
                             "Message": "No such bank with this name and city present."},
                            status=status.HTTP_400_BAD_REQUEST)
        bank = []
        for bankObj in banks:
            dic = {}
            dic['Bank Name'] = bankObj.bank_name
            dic['IFSC Code'] = bankObj.ifsc
            dic['Bank Id'] = bankObj.bank_id
            dic['branch'] = bankObj.branch
            dic['City'] = bankObj.city
            bank.append(dic)

        return Response({"Type": "Success",
                         "Message": "Fetched the bank details Successfully",
                         "Bank Details": bank}, status=status.HTTP_200_OK)


# Some extra APIs

class GetAllBanks(generics.ListAPIView):

    def get(self, request,):
        bank_list = BankDetails.objects.all()
        serializer = BankSerializer(bank_list, many=True)
        return Response({"Type": "Success",
                         "Message": "All Banks displayed successfully",
                         "banks": serializer.data},
                        status=status.HTTP_200_OK)
