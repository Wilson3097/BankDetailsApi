from .models import *
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankDetails
        fields = "__all__"
