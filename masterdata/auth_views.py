from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# REGISTER
@api_view(['POST'])
def register_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username & password harus diisi'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username sudah terdaftar'}, status=400)

    user = User.objects.create_user(username=username, password=password)

    return Response({'message': 'Register berhasil'}, status=201)


# LOGIN
@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Username atau password salah'}, status=400)

    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key})


# LOGOUT
@api_view(['POST'])
def logout_api(request):
    token = request.auth
    if token:
        token.delete()
    return Response({'message': 'Logout berhasil'})
