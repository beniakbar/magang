from django.shortcuts import render, redirect, get_object_or_404
from .models import Pengguna
from .models import Satpam

# Create your views here.

def tes(request):
    return render(request, 'tes.html')

# ------------------ Pengguna Views ------------------

#  READ
def pengguna_list(request):
    data = Pengguna.objects.all()
    return render(request, 'masterdata/pengguna_list.html', {'data': data})

#  CREATE
def pengguna_create(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        Pengguna.objects.create(nama=nama, username=username, password=password, role=role)
        return redirect('pengguna_list')
    return render(request, 'masterdata/pengguna_form.html')

#  UPDATE
def pengguna_update(request, id):
    pengguna = get_object_or_404(Pengguna, id=id)
    if request.method == 'POST':
        pengguna.nama = request.POST['nama']
        pengguna.username = request.POST['username']
        pengguna.password = request.POST['password']
        pengguna.role = request.POST['role']
        pengguna.save()
        return redirect('pengguna_list')
    return render(request, 'masterdata/pengguna_form.html', {'pengguna': pengguna})

#  DELETE
def pengguna_delete(request, id):
    pengguna = get_object_or_404(Pengguna, id=id)
    if request.method == 'POST':
        pengguna.delete()
        return redirect('pengguna_list')
    return render(request, 'masterdata/pengguna_confirm_delete.html', {'pengguna': pengguna})

# ------------------ Satpam Views ------------------

#  READ
def satpam_list(request):
    data = Satpam.objects.all()
    return render(request, 'masterdata/satpam_list.html', {'data': data})

#  CREATE
def satpam_create(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        nik = request.POST['nik']
        alamat = request.POST['alamat']
        no_hp = request.POST['no_hp']
        shift = request.POST['shift']
        Satpam.objects.create(nama=nama, nik=nik, alamat=alamat, no_hp=no_hp, shift=shift)
        return redirect('satpam_list')
    return render(request, 'masterdata/satpam_form.html')

#  UPDATE
def satpam_update(request, id):
    satpam = get_object_or_404(Satpam, id=id)
    if request.method == 'POST':
        satpam.nama = request.POST['nama']
        satpam.nik = request.POST['nik']
        satpam.alamat = request.POST['alamat']
        satpam.no_hp = request.POST['no_hp']
        satpam.shift = request.POST['shift']
        satpam.save()
        return redirect('satpam_list')
    return render(request, 'masterdata/satpam_form.html', {'satpam': satpam})

#  DELETE
def satpam_delete(request, id):
    satpam = get_object_or_404(Satpam, id=id)
    if request.method == 'POST':
        satpam.delete()
        return redirect('satpam_list')
    return render(request, 'masterdata/satpam_confirm_delete.html', {'satpam': satpam})