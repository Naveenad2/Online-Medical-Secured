from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.http import HttpResponse

# Create your views here.
def main_page(request):

     if (request.user.id is not None):
        
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        if(Patient.objects.filter(patient_name = user.username).exists()):
             
             return redirect("/patientMainPage")
        
        if(Doctor.objects.filter(doctor_name = user.username).exists()):
             
             return redirect("/doctorMainPage")
        
     elif(request.user.id == 1):
       
       return redirect("/admin")
    
     else:

       return render(request,'main.html')
    
   

def doctor_registration(request):

       return render(request,'doctor_registration.html')


def doctor_r_auth(request):

    name=request.POST.get('doctorname')
    email=request.POST.get('email')
    phno=request.POST.get('phno')
  
    specialization=request.POST.get('specialization')
    age=request.POST.get('age')
    qualification=request.POST.get('qualification')

    hospital=request.POST.get('hospital')

    password=request.POST.get('password')
    repeatpass=request.POST.get('repeatpass')

    if password == repeatpass:

            user = User.objects.filter(username=name)
            isuser = user.exists()
            if isuser is False:
                new_user = User.objects.create_user(username=name,password=password)
                new_user.save()


                #save the user
                doctor = Doctor(
                connection =new_user,
                doctor_name=name,
                age=age,
                qualification=qualification,
                hospital=hospital,
                specialization=specialization,
                email=email,
                phoneno=phno,
               )
                
                doctor.save()

                authuser = authenticate(username=name,password=password)
                login(request,authuser)

    else:
        return render(request,'doctor_registration.html')

    
    return redirect('/doctorMainPage')

   
def patient_reg(request):
   
   return render(request,'patient_reg.html')

def patient_r_auth(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    phno=request.POST.get('phno')
    address=request.POST.get('address')

    age=request.POST.get('age')


    blood_group=request.POST.get('blood_group')

    password=request.POST.get('password')
    repeatpass=request.POST.get('repassword')

    if password == repeatpass:

            user = User.objects.filter(username=name)
            isuser = user.exists()
            if isuser is False:
                new_user = User.objects.create_user(username=name,password=password)
                new_user.save()


                #save the user
                patient = Patient(
                connection =new_user,
                patient_name=name,
                age=age,
                email=email,
                phone_number=phno,
                blood_group=blood_group,
                address=address)
                
                patient.save()

                authuser = authenticate(username=name,password=password)
                login(request,authuser)

    else:
        return render(request,'patient_reg.html')

    
    return redirect('/patientMainPage')



def patient_login(request):

     if request.method == 'POST':
        username = request.POST.get('pname')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('patientMainPage')
        else:
            return HttpResponse("Wrong password")
    
     return render(request,"patientLogin.html")



def doctor_login(request):

     if request.method == 'POST':
        username = request.POST.get('doctorname')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('doctorMainPage')
        else:
            return HttpResponse("Wrong password")
    
     return render(request,"doctor_login.html")


def Sregistration(request):

    return render(request,"Sregistration.html")


def Slogin(request):

    return render(request,"Slogin.html")


def doctorMainPage(request):

    user_id = request.user.id
   # print(user_id)
    user_obj = User.objects.get(id=user_id)

    user = Doctor.objects.get(connection=user_obj)

    consult = Consultation.objects.filter(doctor=user)
    #print(consult)
    
    return render(request,"doctorMainPage.html",{"user":user,"consult":consult})

def patientMainPage(request):

    user_id = request.user.id
    user_obj = User.objects.get(id=user_id)

    user = Patient.objects.get(connection=user_obj)


    consult = Consultation.objects.filter(Patient=user)

    return render(request,"patientMainPage.html",{"user":user,"consult":consult})


def viewAllDoctors(request):

    doctors = Doctor.objects.all()
    
    return render(request,"viewAllDoctors.html",{"doctor":doctors})

def doctorCosult(request,id):
    doctor = Doctor.objects.get(id=id)
    return render(request,"doctorCosult.html",{"doctor":doctor,})

def cosultation_imp(request):

     if request.method == 'POST':
        doctor = request.POST.get('doctorName')
        hospital = request.POST.get('hospitalName')
        message = request.POST.get('message')
        print(doctor)

        user_id = request.user.id
        user_obj = User.objects.get(id=user_id)

        user = Patient.objects.get(connection=user_obj)

        doctor_obj = Doctor.objects.get(doctor_name=doctor)

        consult = Consultation(Patient=user,doctor=doctor_obj,message=message,hospital=hospital)
        consult.save()

     return redirect("/")
    


def addTimmingDoctor(request,id):

     return render(request,"addTimmingDoctor.html",{"id":id})
    
def addTimmingDoctorImplementation(request):

      
     if request.method == 'POST':
        timming = request.POST.get('timming')
        id_pa = request.POST.get('pa_id')
      

        user_id = request.user.id
   # print(user_id)
        user_obj = User.objects.get(id=user_id)

        user = Doctor.objects.get(connection=user_obj)


        patient = Patient.objects.get(id=id_pa)

        consultation = Consultation.objects.filter(Patient=patient, doctor=user).first()

        consultation.assainged_time = timming
        consultation.save()


     return redirect("/")

def editPatient(request):

      if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pno = request.POST.get('pno')
        age = request.POST.get('age')
        blood = request.POST.get('blood')
        

        user_id = request.user.id
  
        user_obj = User.objects.get(id=user_id)

        user = Patient.objects.get(connection=user_obj)

        user.patient_name = name
        user.email = email
        user.address = address
        user.age = age
        user.blood_group = blood
        user.phone_number = pno

        user.save()


        return redirect("/")

      else:
            
        user_id = request.user.id

        user_obj = User.objects.get(id=user_id)

        user = Patient.objects.get(connection=user_obj)


        return render(request,"editPatient.html",{"user":user})


def editDoctor(request):

      if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Specialization = request.POST.get('Specialization')
        pno = request.POST.get('pno')
        age = request.POST.get('age')
        Qualification = request.POST.get('Qualification')
        hospital = request.POST.get('Hospital')
        

        user_id = request.user.id
  
        user_obj = User.objects.get(id=user_id)

        user = Doctor.objects.get(connection=user_obj)

        user.patient_name = name
        user.email = email
        user.specialization = Specialization
        user.age = age
        user.qualification = Qualification
        user.phone_number = pno
        user.hospital = hospital

        user.save()


        return redirect("/")

      else:
            
        user_id = request.user.id

        user_obj = User.objects.get(id=user_id)

        user = Doctor.objects.get(connection=user_obj)
     

      return render(request,"editDoctor.html",{"user":user})

def Logout_(request):
       logout(request)
       return redirect("/")