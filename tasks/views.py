import json

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    return Response({"msg": "pong"})

@api_view(["GET"])
def health_check_jwt(request):
    return Response({"msg": "jwt_pong"})
