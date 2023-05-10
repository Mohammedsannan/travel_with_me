import json
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#admin
from travel_planning.models import *
from travel_planning.rec_restaurant import recommendor
def main(request):
    return  render(request,"home.html")
def index(request):
    return  render(request,"index.html")

def admdashboard(request):
    return render(request, "admin/dashboardadmin.html")

def lgn(request):
    username=request.POST['username']
    password=request.POST['password']
    try:
        ob=Login.objects.get(username=username,password=password)
        if ob.type == 'admin':
            return HttpResponse('''<script>alert("login successfully");window.location='admdashboard'</script>''')
        elif ob.type == 'restaurant':
            request.session['lid']=ob.id
            obb=restaurant.objects.get(lid__id=request.session['lid'])
            request.session['sname']=obb.name
            return HttpResponse('''<script>alert("login successfully");window.location='restaurant_home'</script>''')
        elif ob.type == 'resort':
            request.session['lid'] = ob.id
            obb = resorts.objects.get(lid__id=request.session['lid'])
            request.session['sname'] = obb.name
            return HttpResponse('''<script>alert("login successfully");window.location='resortdashboard'</script>''')
        else:
            return HttpResponse('''<script>alert("error messsage");window.location='/'</script>''')
    except:
       return HttpResponse('error')


def viewrestaurant(request):
    ob=restaurant.objects.all()
    return render(request,"admin/view restaurant.html",{'val':ob})

def acceptrestaurant(request,id):
    ob=Login.objects.get(id=id)
    ob.type='restaurant'
    ob.save()
    return HttpResponse('''<script>alert("accepted");window.location='/viewrestaurant'</script>''')

def rejectrestaurant(request,id):
    ob = Login.objects.get(id=id)
    ob.type = 'reject'
    ob.save()
    return HttpResponse('''<script>alert("rejected");window.location='/viewrestaurant'</script>''')


def viewresort(request):
    ob = resorts.objects.all()
    return render(request,"admin/view resort.html",{'val':ob})

def acceptresort(request,id):
    ob=Login.objects.get(id=id)
    ob.type='resort'
    ob.save()
    return HttpResponse('''<script>alert("accepted");window.location='/viewresort'</script>''')

def rejectresort(request,id):
    ob = Login.objects.get(id=id)
    ob.type = 'reject'
    ob.save()
    return HttpResponse('''<script>alert("rejected");window.location='/viewresort'</script>''')




def managerestaurant(request):
    ob=restaurant.objects.all()
    return render(request,"admin/Manage restaurant.html",{'val':ob})

def blockrestaurant(request,id):
    ob=Login.objects.get(id=id)
    ob.type='block'
    ob.save()
    return HttpResponse('''<script>alert("blocked");window.location='/managerestaurant'</script>''')

def unblockrestaurant(request,id):
    ob = Login.objects.get(id=id)
    ob.type = 'restaurant'
    ob.save()
    return HttpResponse('''<script>alert("unblocked");window.location='/managerestaurant'</script>''')



def manageresort(request):
    ob=resorts.objects.all()
    return render(request,"admin/manage resort.html",{'val':ob})


def blockresort(request,id):
    ob=Login.objects.get(id=id)
    ob.type='block'
    ob.save()
    return HttpResponse('''<script>alert("blocked");window.location='/manageresort'</script>''')

def unblockresort(request,id):
    ob = Login.objects.get(id=id)
    ob.type = 'resort'
    ob.save()
    return HttpResponse('''<script>alert("unblocked");window.location='/manageresort'</script>''')










def viewtouristplace(request):
    ob=touristplace.objects.all()
    return render(request,"admin/view tourist place.html",{'val':ob})

def addtouristplace(request):
    return render(request,"admin/add tourist place.html")

def addtp(request):
    place=request.POST['textfield']
    image=request.FILES['file']
    fs = FileSystemStorage()
    fp = fs.save(image.name, image)
    description=request.POST['textfield2']
    iob=touristplace()
    iob.place=place
    iob.image=fp
    iob.description=description
    iob.latitude='0'
    iob.longitude='0'
    iob.save()
    request.session['locid'] = iob.id
    return HttpResponse('''<script>alert("success");window.location="/map_tp"</script>''')

def map_tp(request):
    return render(request,"admin/map_tp.html")

def map1_tp(request):
    lat=request.POST['lat']
    lon=request.POST['lon']
    ob=touristplace.objects.get(id=request.session['locid'])
    ob.latitude=lat
    ob.longitude=lon
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location="/viewtouristplace"</script>''')

def edittp(request,id):
    request.session['tpid'] = id
    tp_obj = touristplace.objects.get(id = id)
    return render(request,'admin/edit_tourist place.html',{'tp':tp_obj})

def edittp_post(request):
    place = request.POST['textfield']
    image = request.FILES['file']
    fs = FileSystemStorage()
    fp = fs.save(image.name, image)
    description = request.POST['textfield2']
    iob = touristplace.objects.get(id = request.session['tpid'])
    iob.place = place
    iob.image = fp
    iob.description = description
    iob.latitude = '0'
    iob.longitude = '0'
    iob.save()
    request.session['locid'] = iob.id
    return HttpResponse('''<script>alert("updated");window.location="/map_tp"</script>''')

def deletetp(request,id):
    ob = touristplace.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location="/viewtouristplace"</script>''')


def complaint(request):
    ob=complaints.objects.all()
    return render(request,"admin/manage complaints.html",{'val':ob})

def replysend(request):
    replys=request.POST['textfield']
    ob=complaints.objects.get(id=request.session['compid'])
    ob.reply=replys
    ob.save()
    return HttpResponse('''<script>alert("replied");window.location='/complaint'</script>''')


def reply(request,id):
    request.session['compid']=id
    return render(request,"admin/reply.html")

def viewuser(request):
    ob=userregistration.objects.all()
    return render(request,"admin/view user.html",{'val':ob})

def feedbacks(request):
    ob=feedback.objects.all()
    return render(request,"admin/feedback.html",{'val':ob})





# --------------------------------------------------------------------------------------------------------------------------------------------------------------

#restaurant

def restaurantdashboard(request):
    return render(request,"restaurant/dashboardrestaurant.html")

def restaurant_home(request):
    return render(request,"restaurant/home.html")


def restaurantregister(request):
    return render(request,"restaurant/restaurant registration.html")

def addrestaurant(request):
    type=request.POST['select2']
    name=request.POST['textfield']
    pin = request.POST['textfield3']
    district=request.POST['select']
    email = request.POST['textfield4']
    phone_number = request.POST['textfield5']
    license_number = request.POST['textfield6']
    password = request.POST['textfield7']
    place = request.POST['textfield2']
    image = request.FILES['file']
    fs=FileSystemStorage()
    fp=fs.save(image.name,image)
    if type=="Restaurant":
        ob=Login()
        ob.username=email
        ob.password=password
        ob.type='pending'
        ob.save()
        iob=restaurant()
        iob.name=name
        iob.place=place
        iob.pin =pin
        iob.district=district
        iob.email=email
        iob.image=fp
        iob.phonenumber=phone_number
        iob.license=license_number
        iob.password=password
        iob.lattitude="0"
        iob.longitude="0"
        iob.lid=ob
        iob.save()
        request.session['locid']=iob.id
        return HttpResponse('''<script>alert("added");window.location='/map'</script>''')
    else:
        ob = Login()
        ob.username = email
        ob.password = password
        ob.type = 'pending'
        ob.save()
        iob = resorts()
        iob.name = name
        iob.place = place
        iob.pin = pin
        iob.district = district
        iob.email = email
        iob.image = fp
        iob.phonenumber = phone_number
        iob.license = license_number
        iob.password = password
        iob.lattitude = "0"
        iob.longitude = "0"
        iob.lid = ob
        iob.save()
        request.session['locid'] = iob.id
        return HttpResponse('''<script>alert("added");window.location='/mapresort'</script>''')





def map(request):
    return render(request,"restaurant/map.html")

def map1(request):
    lat=request.POST['lat']
    lon=request.POST['lon']
    ob=restaurant.objects.get(id=request.session['locid'])
    ob.lattitude=lat
    ob.longitude=lon
    ob.save()
    return HttpResponse('''<script>alert("registration completed");window.location="/"</script>''')

def mapresort(request):
    return render(request,"resort/maprsrt.html")

def map2(request):
    lat=request.POST['lat']
    lon=request.POST['lon']
    ob=resorts.objects.get(id=request.session['locid'])
    ob.lattitude=lat
    ob.longitude=lon
    ob.save()
    return HttpResponse('''<script>alert("registration completed");window.location="/"</script>''')

def viewmenu(request):
    ob=fooditem.objects.filter(restaurantid__lid__id=request.session['lid'])
    return render(request,"restaurant/view menu.html",{'val':ob})

def addmenu(request):
    return render(request, "restaurant/add menu.html")

def menuadd(request):
    foodcategorys=request.POST['textfield']
    foodname=request.POST['textfield2']
    image= request.FILES['file']
    fn=FileSystemStorage()
    fs=fn.save(image.name,image)
    price = request.POST['textfield3']
    description = request.POST['textfield4']
    iob=fooditem()
    iob.foodname=foodname
    iob.image=fs
    iob.price=price
    iob.description=description
    iob.restaurantid=restaurant.objects.get(lid__id=request.session['lid'])
    iob.category=foodcategorys
    iob.save()

    return HttpResponse('''<script>alert("added");window.location='/viewmenu'</script>''')

def editmenu(request,id):
    ob=fooditem.objects.get(id=id)
    request.session['fdid']=id
    return render(request, "restaurant/edit_menu.html",{'val':ob})




def edit(request):
    try:
        foodcategorys = request.POST['textfield']
        foodname = request.POST['textfield2']
        image = request.FILES['file']
        fn = FileSystemStorage()
        fs = fn.save(image.name, image)
        price = request.POST['textfield3']
        description = request.POST['textfield4']

        iob = fooditem.objects.get(id=request.session['fdid'])
        iob.foodname = foodname
        iob.image = fs
        iob.price = price
        iob.description = description
        iob.restaurantid = restaurant.objects.get(lid__id=request.session['lid'])
        iob.category = foodcategorys
        iob.save()
        return HttpResponse('''<script>alert("Details edited successfully");window.location="/viewmenu"</script>''')
    except:
        foodcategorys = request.POST['textfield']
        foodname = request.POST['textfield2']
        price = request.POST['textfield3']
        description = request.POST['textfield4']
        iob = fooditem.objects.get(id=request.session['fdid'])
        iob.foodname = foodname
        iob.price = price
        iob.description = description
        iob.restaurantid = restaurant.objects.get(lid__id=request.session['lid'])
        iob.category = foodcategorys
        iob.save()
        return HttpResponse('''<script>alert("Details edited successfully");window.location="/viewmenu"</script>''')

def deletemenu(request,id):
    ob = fooditem.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Details edited successfully");window.location="/viewmenu"</script>''')


def viewfacility(request):
    ob = restaurantfacility.objects.filter(restaurantid__lid__id=request.session['lid'])
    return render(request,"restaurant/view_restaurant_facility.html",{'val':ob})

def addfacility(request):
    return render(request,"restaurant/add facility.html")

def facilityadd(request):
    facilitys=request.POST['textfield']
    image=request.FILES['file']
    fn=FileSystemStorage()
    fs=fn.save(image.name,image)
    description=request.POST['textfield2']

    iob=restaurantfacility()
    iob.facility=facilitys
    iob.image=fs
    iob.description=description
    iob.restaurantid=restaurant.objects.get(lid__id=request.session['lid'])
    iob.save()

    return HttpResponse('''<script>alert("facility added");window.location="/viewfacility"</script>''')

def editfacility(request,id):
    ob = restaurantfacility.objects.get(id=id)
    request.session['rtfid'] = id
    return render(request, "restaurant/edit facility.html", {'val': ob})

def facilityedit(request):
    try:
        facilitys = request.POST['textfield']
        image = request.FILES['file']
        fn = FileSystemStorage()
        fs = fn.save(image.name, image)
        description = request.POST['textfield2']
        iob = restaurantfacility.objects.get(id=request.session['rtfid'])
        iob.facility = facilitys
        iob.image = fs
        iob.description = description
        iob.restaurantid = restaurant.objects.get(lid__id=request.session['lid'])
        iob.save()
        return HttpResponse('''<script>alert("Details edited successfully");window.location="/viewfacility"</script>''')
    except:
        facilitys = request.POST['textfield']
        description = request.POST['textfield2']
        iob = restaurantfacility.objects.get(id=request.session['rtfid'])
        iob.facility = facilitys
        iob.description = description
        iob.restaurantid = restaurant.objects.get(lid__id=request.session['lid'])
        iob.save()
        return HttpResponse('''<script>alert("Details edited successfully");window.location="/viewfacility"</script>''')

def deleterestaurantfacility(request,id):
    ob = restaurantfacility.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Details deleted successfully");window.location="/viewfacility"</script>''')


def viewrating(request):
    ob=restaurantreviewrating.objects.filter(restaurantid__lid__id=request.session['lid'])
    return render(request,"restaurant/view rating.html",{'val':ob})



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------


#resort



def resortdashboard(request):
    return render(request,"resort/dashboardresort.html")

def resort_home(request):
    return render(request,"resort/homeresort.html")


def manageroom(request):
    ob=resortroom.objects.filter(resortid__lid__id=request.session['lid'])
    return render(request,"resort/manage room.html",{'val':ob})

def addroom(request):
    return render(request,"resort/add room.html")

def roomadd(request):
    roomnumber=request.POST['textfield']
    Image=request.FILES['file']
    fn=FileSystemStorage()
    fs=fn.save(Image.name,Image)
    Type=request.POST['textfield2']
    Amount=request.POST['textfield3']

    iob=resortroom()
    iob.roomno=roomnumber
    iob.type=Type
    iob.amount=Amount
    iob.image=fs
    iob.resortid = resorts.objects.get(lid=request.session['lid'])
    iob.save()

    return HttpResponse('''<script>alert("room added");window.location="/manageroom"</script>''')


def editroom(request,id):
    ob=resortroom.objects.get(id=id)
    request.session['rmid']=id
    return render(request, "resort/edit room.html",{'val':ob})

def roomedit(request):
    try:
        roomnumber=request.POST['textfield']
        Image=request.FILES['file']
        fn=FileSystemStorage()
        fs=fn.save(Image.name,Image)
        Type=request.POST['textfield2']
        Amount=request.POST['textfield3']
        iob=resortroom.objects.get(id=request.session['rmid'])
        iob.roomno=roomnumber
        iob.type=Type
        iob.amount=Amount
        iob.image=fs
        iob.resortid = resorts.objects.get(lid=request.session['lid'])
        iob.save()
        return HttpResponse('''<script>alert("edited successfully");window.location="/manageroom"</script>''')
    except:
        roomnumber = request.POST['textfield']
        Type = request.POST['textfield2']
        Amount = request.POST['textfield3']
        iob = resortroom.objects.get(id=request.session['rmid'])
        iob.roomno = roomnumber
        iob.type = Type
        iob.amount = Amount
        iob.resortid = resorts.objects.get(lid=request.session['lid'])
        iob.save()
        return HttpResponse('''<script>alert("edited successfully");window.location="/manageroom"</script>''')

def deleteroom(request, id):
    ob = resortroom.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Details deleted successfully");window.location="/manageroom"</script>''')



def viewresortfacility(request):
    ob=resortfacility.objects.filter(resortid__lid__id=request.session['lid'])
    return render(request, "resort/view facility.html",{'val':ob})

def addresortfacility(request):
    return render(request,"resort/add resortfacility.html")

def resortfacilityadd(request):
    resortfacilitys=request.POST['textfield']
    image=request.FILES['file']
    fn=FileSystemStorage()
    fs=fn.save(image.name,image)
    descriptions=request.POST['textfield2']

    iob=resortfacility()
    iob.facility=resortfacilitys
    iob.image=fs
    iob.description=descriptions
    iob.resortid=resorts.objects.get(lid__id=request.session['lid'])
    iob.save()

    return HttpResponse('''<script>alert("facility added");window.location="/viewresortfacility"</script>''')

def editresortfacility(request,id):
    ob=resortfacility.objects.get(id=id)
    request.session['rsfid']=id
    return render(request, "resort/edit resort facility.html", {'val': ob})


def resortfacilityedit(request):
    print(request.FILES)
    print(request.POST)
    try:
        fclity = request.POST['textfield']
        image = request.FILES['file']
        fn = FileSystemStorage()
        fs = fn.save(image.name, image)
        descriptions = request.POST['textfield2']
        iob=resortfacility.objects.get(id=request.session['rsfid'])
        iob.facility = fclity
        iob.image = fs
        iob.description = descriptions
        iob.resortid = resorts.objects.get(lid__id=request.session['lid'])
        iob.save()
        return HttpResponse('''<script>alert("facility edited");window.location="/viewresortfacility"</script>''')
    except Exception as e:
        print(e)
        facility = request.POST['textfield']
        descriptions = request.POST['textfield2']
        iob = resortfacility.objects.get(id=request.session['rsfid'])
        iob.facility = facility
        iob.description = descriptions
        iob.resortid = resorts.objects.get(lid__id=request.session['lid'])
        iob.save()
        return HttpResponse('''<script>alert("facility edited");window.location="/viewresortfacility"</script>''')

def deleteresortfacility(request,id):
    ob=resortfacility.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("details deleted successfully");window.location="/viewresortfacility"</script>''')



def viewresortrating(request):
    ob=resortreviewrating.objects.filter(resortid__lid__id=request.session['lid'])
    return render(request,"resort/view resort rating .html",{'val':ob})
























































































###############################################android-webservice###########################################################



def logins(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        ob= Login.objects.get(username=username, password=password)
        if ob is None:
            data={'task':'invalid'}
            r = json.dumps(data)
            return HttpResponse(r)
        else:
            data={'task':'success','id':ob.id}
            r = json.dumps(data)
            return HttpResponse(r)




    except:
        data={'task': 'invalid'}
        r = json.dumps(data)
        return HttpResponse(r)


def userregister(request):
    fullname = request.POST['fullname']
    email = request.POST['email']
    phone_number = request.POST['phonenumber']
    print(phone_number)
    address = request.POST['address']
    gender = request.POST['gender']
    password = request.POST['password']
    ob=Login()
    ob.username=email
    ob.password=password
    ob.type='user'
    ob.save()

    ob1=userregistration()
    ob1.fullname=fullname
    ob1.email=email
    ob1.phonenumber=phone_number
    ob1.address=address
    ob1.lid=ob
    ob1.gender=gender
    ob1.save()

    data={'task':'success'}
    r = json.dumps(data)
    return HttpResponse(r)

def viewrest_android(request):
    ob=restaurant.objects.all()
    data=[]
    for i in ob:
        row={'name':i.name,'image':str(i.image),'location':i.place,'rid':i.id}
        data.append(row)
    r=json.dumps(data)
    print(r,"===============================")
    return HttpResponse(r)

def viewmore_restaurant(request):
    id=request.POST['rid']
    obb=restaurant.objects.filter(id=id)
    data=[]
    for ob in obb:
        row={'email':ob.email,'phonenumber':str(ob.phonenumber),'address':ob.place+","+str(ob.pin)+","+ob.district,'lattitude':ob.lattitude,'longitude':ob.longitude}
        data.append(row)
    r=json.dumps(data)
    print(r,"=========================")
    return HttpResponse(r)

def menurestaurant_android(request):
    id=request.POST['rid']
    ob=fooditem.objects.filter(restaurantid__id=id)
    data=[]
    for i in ob:
        row={'category':i.category,'name':i.foodname,'image':str(i.image),'description':i.description,'price':i.price,'fid':i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)

def resfacility_android(request):
    id=request.POST['rid']
    ob=restaurantfacility.objects.filter(restaurantid__id=id)
    data=[]
    for i in ob:
        row={'name':i.facility,'image':str(i.image),'description':i.description,'fcid':i.id}
        data.append(row)
    r = json.dumps(data)
    print(r,"=======================")
    return HttpResponse(r)

def restaurantrating_android(request):
    rid=request.POST['rid']
    uid=request.POST['uid']
    print(uid,"================================")
    rating=request.POST['rating']
    review=request.POST['review']
    ob=restaurantreviewrating()
    ob.uid=userregistration.objects.get(lid__id=uid)
    ob.restaurantid=restaurant.objects.get(id=rid)
    ob.rating=rating
    ob.review=review
    ob.date=datetime.today()
    ob.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)





def viewresort_android(request):
    ob=resorts.objects.all()
    data=[]
    for i in ob:
        row={'name':i.name,'image':str(i.image),'location':i.place,'rid':i.id}
        data.append(row)
    r=json.dumps(data)
    print(r,"===============================")
    return HttpResponse(r)


def viewmore_resort(request):
    id=request.POST['rid']
    obb=resorts.objects.filter(id=id)
    data=[]
    for ob in obb:
        row={'email':ob.email,'phonenumber':str(ob.phonenumber),'address':ob.place+","+str(ob.pin)+","+ob.district,'lattitude':ob.lattitude,'longitude':ob.longitude}
        data.append(row)
    r=json.dumps(data)
    print(r,"=========================")
    return HttpResponse(r)


def roomresort_android(request):
    id=request.POST['rid']
    ob=resortroom.objects.filter(resortid__id=id)
    data=[]
    for i in ob:
        row={'roomno':i.roomno,'type':i.type,'image':str(i.image),'amount':i.amount,'rmid':i.id}
        data.append(row)
    r = json.dumps(data)
    return HttpResponse(r)
def view_reply(request):
    id=request.POST['lid']
    ob=complaints.objects.filter(userid__lid__id=id)
    data=[]
    for i in ob:
        row={'complaint':i.complaint,'date':str(i.date),'reply':i.reply}
        data.append(row)
    r = json.dumps(data)
    print(r,"=======================")
    return HttpResponse(r)

def resortfacility_android(request):
    id=request.POST['rid']
    ob=resortfacility.objects.filter(resortid__id=id)
    data=[]
    for i in ob:
        row={'name':i.facility,'image':str(i.image),'description':i.description,'fcid':i.id}
        data.append(row)
    r = json.dumps(data)
    print(r,"=======================")
    return HttpResponse(r)


def resortrating_android(request):
    rid=request.POST['rid']
    uid=request.POST['uid']
    rating=request.POST['rating']
    review=request.POST['review']
    ob=resortreviewrating()
    ob.uid=userregistration.objects.get(lid__id=uid)
    ob.resortid=resorts.objects.get(id=rid)
    ob.rating=rating
    ob.review=review
    ob.date=datetime.today()
    ob.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)

def touristplace_android(request):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT `travel_planning_touristplace`.*,AVG(`travel_planning_touristplacereviewrating`.`rating`) AS rating FROM `travel_planning_touristplace` LEFT JOIN `travel_planning_touristplacereviewrating` ON travel_planning_touristplace.id=travel_planning_touristplacereviewrating.`tpid_id` GROUP BY `travel_planning_touristplace`.`id`")
    res = cursor.fetchall()
    ob=touristplace.objects.all()
    data = []
    for i in res:
        if i[6] is None:
            rating=0
        else:
            rating=i[6]
        row = {'place': i[1], 'image': str(i[2]), 'description': i[5],'latitude': i[3],'longitude': i[4],'tid':i[0],'rating':rating}
        data.append(row)
    r = json.dumps(data)
    print(r, "=======================")
    return HttpResponse(r)

def touristrating_android(request):
    tpid=request.POST['tpid']
    uid=request.POST['uid']
    rating=request.POST['rating']
    review=request.POST['review']
    print(uid,rating,review,"************************")
    ob=touristplacereviewrating()
    ob.uid=userregistration.objects.get(lid__id=uid)
    ob.tpid=touristplace.objects.get(id=tpid)
    ob.rating=rating
    ob.review=review
    ob.date=datetime.today()
    ob.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)

def sendcomplaint(request):
    uid=request.POST['lid']
    comp=request.POST['comp']
    ob=complaints()
    ob.userid=userregistration.objects.get(lid__id=uid)
    ob.comp=comp

    ob.date=datetime.today()
    ob.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)





def sendfeedback(request):
    uid=request.POST['lid']
    comp=request.POST['feed']
    ob=feedback()
    ob.uid=userregistration.objects.get(lid__id=uid)
    ob.comp=comp
    ob.date=datetime.today()
    ob.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)

def view_resort_rating(request):
    from django.db.models import Avg
    rid=request.POST['rid']
    ob=resortreviewrating.objects.filter(resortid__id=rid).aggregate(Avg=Avg('rating'))
    print(ob['Avg'],"====================*****")
    if ob['Avg'] == 'None':
        rating=0
    else:
        rating=ob['Avg']
    data = {'task':rating}
    r = json.dumps(data)
    return HttpResponse(r)

def view_restaurant_rating(request):
    from django.db.models import Avg
    rid = request.POST['rid']
    ob = restaurantreviewrating.objects.filter(restaurantid__id=rid).aggregate(Avg=Avg('rating'))
    print(ob['Avg'], "====================*****")
    if ob['Avg'] == 'None':
        rating = 0
    else:
        rating = ob['Avg']
    data = {'task': rating}
    r = json.dumps(data)
    return HttpResponse(r)

def viewrcmdrest_android(request):
    from django.db import connection
    cursor = connection.cursor()
    lati = request.POST['lati']
    longi = request.POST['longi']
    lid=request.POST['lid']
    print(lati,longi,"=========================")
    ob=userregistration.objects.get(lid__id=lid)
    res1=recommendor(ob.lid.id)
    print("SELECT * FROM `travel_planning_restaurant` WHERE `id` IN(SELECT `restaurantid_id` FROM `travel_planning_restaurantreviewrating` WHERE `uid_id` IN(" + res1 + ") ) AND id NOT IN(SELECT `restaurantid_id` FROM `travel_planning_restaurantreviewrating` WHERE `uid_id`='"+str(ob.id)+"')")
    cursor.execute("SELECT *,(3959 * ACOS ( COS ( RADIANS('"+lati+"') ) * COS( RADIANS(`travel_planning_restaurant`.`lattitude`) ) * COS( RADIANS(`travel_planning_restaurant`.`longitude`) - RADIANS('"+longi+"') ) + SIN ( RADIANS('"+lati+"') ) * SIN( RADIANS( `travel_planning_restaurant`.`lattitude` ) ))) AS user_distance FROM `travel_planning_restaurant` WHERE `id` IN(SELECT `restaurantid_id` FROM `travel_planning_restaurantreviewrating` WHERE `uid_id` IN(" + res1 + ") ) AND id NOT IN(SELECT `restaurantid_id` FROM `travel_planning_restaurantreviewrating` WHERE `uid_id`='"+str(ob.id)+"') HAVING user_distance < 31.068")
    res=cursor.fetchall()
    data = []
    for i in res:
        row = {'name': i[1], 'image': str(i[5]), 'location': i[4], 'rid': i[0]}
        data.append(row)
    r = json.dumps(data)
    print(r, "===============================")
    return HttpResponse(r)

def viewrcmdresort_android(request):
    from django.db import connection
    cursor = connection.cursor()
    lati=request.POST['lati']
    longi=request.POST['longi']
    lid = request.POST['lid']
    print(lati,longi,"88888888888888")
    ob = userregistration.objects.get(lid__id=lid)
    res1 = recommendor(ob.lid.id)
    # cursor.execute("SELECT * FROM `travel_planning_resorts` WHERE `id` IN(SELECT `resortid_id` FROM `travel_planning_resortreviewrating` WHERE `uid_id` IN("+res1+")) AND id NOT IN(SELECT `resortid_id` FROM `travel_planning_resortreviewrating` WHERE `uid_id`='"+str(ob.id)+"')")
    cursor.execute("SELECT *, (3959 * ACOS ( COS ( RADIANS('"+lati+"') ) * COS( RADIANS(`travel_planning_resorts`.`lattitude`) ) * COS( RADIANS(`travel_planning_resorts`.`longitude`) - RADIANS('"+longi+"') ) + SIN ( RADIANS('"+lati+"') ) * SIN( RADIANS( `travel_planning_resorts`.`lattitude` ) ))) AS user_distance FROM `travel_planning_resorts` WHERE `id` IN(SELECT `resortid_id` FROM `travel_planning_resortreviewrating` WHERE `uid_id` IN("+res1+")) AND id NOT IN(SELECT `resortid_id` FROM `travel_planning_resortreviewrating` WHERE `uid_id`='"+str(ob.id)+"') HAVING user_distance < 31.068")
    res = cursor.fetchall()
    data = []
    for i in res:
        row = {'name': i[1], 'image': str(i[5]), 'location': i[4], 'rid': i[0]}
        data.append(row)
    r = json.dumps(data)
    print(r, "===============================")
    return HttpResponse(r)

def viewrcmdtourist_android(request):
    from django.db import connection
    cursor = connection.cursor()
    lati = request.POST['lati']
    longi = request.POST['longi']
    lid = request.POST['lid']
    ob = userregistration.objects.get(lid__id=lid)
    res1 = recommendor(ob.lid.id)
    cursor.execute("SELECT *,(3959 * ACOS ( COS ( RADIANS('" + lati + "') ) * COS( RADIANS(`travel_planning_touristplace`.`latitude`) ) * COS( RADIANS(`travel_planning_touristplace`.`longitude`) - RADIANS('" + longi + "') ) + SIN ( RADIANS('" + lati + "') ) * SIN( RADIANS( `travel_planning_touristplace`.`latitude` ) ))) AS user_distance FROM `travel_planning_touristplace` WHERE `id` IN(SELECT `tpid_id` FROM `travel_planning_touristplacereviewrating` WHERE `uid_id` IN(" + res1 + ")) AND id NOT IN(SELECT `tpid_id` FROM `travel_planning_touristplacereviewrating` WHERE `uid_id`='" + str( ob.id) + "') HAVING user_distance < 31.068")
    # cursor.execute("SELECT *, (3959 * ACOS ( COS ( RADIANS('" + lati + "') ) * COS( RADIANS(`travel_planning_touristplace`.`latitude`) ) * COS( RADIANS(`travel_planning_touristplace`.`longitude`) - RADIANS('" + longi + "') ) + SIN ( RADIANS('" + lati + "') ) * SIN( RADIANS( `travel_planning_touristplace`.`latitude` ) ))) AS user_distance FROM `travel_planning_touristplace` WHERE `id` IN(SELECT `resortid_id` FROM `travel_planning_touristplacereviewrating` WHERE `uid_id` IN(" + res1 + ")) AND id NOT IN(SELECT `resortid_id` FROM `travel_planning_touristplacereviewrating` WHERE `uid_id`='" + str(ob.id) + "') HAVING user_distance < 31.068")
    res = cursor.fetchall()
    data = []
    for i in res:
        # if i[6] is None:
        rating = 0
        # else:
        #     rating = i[6]
        row = {'place': i[1], 'image': str(i[2]), 'description': i[5], 'latitude': i[3], 'longitude': i[4], 'tid': i[0],
               'rating': rating}
        data.append(row)
    r = json.dumps(data)
    print(r, "=======================")
    return HttpResponse(r)

def identifyuser_android(request):
    lid=request.POST['lid']
    ob=userregistration.objects.get(lid__id=lid)
    data = {'nm':ob.fullname}
    r = json.dumps(data)
    return HttpResponse(r)
