from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body.get("username")
        password = body.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({"message": "User registered", "id": user.id})

    return JsonResponse({"error": "Only POST allowed"}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body.get("username")
        password = body.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            return JsonResponse({"error": "Invalid credentials"}, status=400)

        login(request, user)
        return JsonResponse({"message": "Login success"})

    return JsonResponse({"error": "Only POST allowed"}, status=405)


@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Logout success"})
    return JsonResponse({"error": "Only POST allowed"}, status=405)
