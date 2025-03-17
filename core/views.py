from django.shortcuts import render

from core.models import Charge
from core.serializers import ChargeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


# Create your views here.

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_charge(request):
    serializer = ChargeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def charge_list(request):
    charges = Charge.objects.all()
    serializer = ChargeSerializer(charges, many=True)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_charge(request, pk):
    user = request.user
    charge = Charge.objects.get(id=pk)
    serializer = ChargeSerializer(charge, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def delete_charge(request, pk):
    charge = Charge.objects.get(id=pk)
    charge.delete()
    return Response({"message": "Charge deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
