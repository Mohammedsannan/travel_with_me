from django.urls import path
from travel_planning import views

urlpatterns=[

    path('',views.main,name="main"),
    path('index', views.index, name="index"),
    path('lgn', views.lgn, name="lgn"),
    path('admdashboard', views.admdashboard, name="admdashboard"),
    path('viewrestaurant',views.viewrestaurant,name="viewrestaurant"),
    path('acceptrestaurant/<int:id>', views.acceptrestaurant, name="acceptrestaurant"),
    path('rejectrestaurant/<int:id>', views.rejectrestaurant, name="rejectrestaurant"),
    path('viewresort', views.viewresort, name="viewresort"),
    path('acceptresort/<int:id>', views.acceptresort, name="acceptresort"),
    path('rejectresort/<int:id>', views.rejectresort, name="rejectresort"),
    path('managerestaurant', views.managerestaurant, name="managerestaurant"),
    path('manageresort', views.manageresort, name="manageresort"),
    path('viewtouristplace', views.viewtouristplace, name="viewtouristplace"),
    path('addtouristplace', views.addtouristplace, name="addtouristplace"),
    path('addtp', views.addtp, name="addtp"),
    path('map_tp', views.map_tp, name="map_tp"),
    path('map1_tp', views.map1_tp, name="map1_tp"),
    path('edittp/<int:id>', views.edittp, name="edittp"),
    path('edittp_post', views.edittp_post, name="edittp_post"),
    path('deletetp/<int:id>', views.deletetp, name="deletetp"),
    path('unblockresort/<int:id>', views.unblockresort, name="unblockresort"),
    path('blockresort/<int:id>', views.blockresort, name="blockresort"),
    path('blockrestaurant/<int:id>', views.blockrestaurant, name="blockrestaurant"),
    path('unblockrestaurant/<int:id>', views.unblockrestaurant, name="unblockrestaurant"),

    path('complaint', views.complaint, name="complaint"),
    path('replysend', views.replysend, name="replysend"),
    path('reply/<int:id>', views.reply, name="reply"),
    path('viewuser', views.viewuser, name="viewuser"),
    path('feedbacks', views.feedbacks, name="feedbacks"),

    path('restaurantdashboard', views.restaurantdashboard, name="restaurantdashboard"),
    path('restaurantregister', views.restaurantregister, name="restaurantregister"),
    path('addrestaurant', views.addrestaurant, name="addrestaurant"),
    path('viewmenu', views.viewmenu, name="viewmenu"),
    path('addmenu', views.addmenu, name="addmenu"),
    path('menuadd', views.menuadd, name="menuadd"),
    path('editmenu/<int:id>', views.editmenu, name="editmenu"),
    path('deletemenu/<int:id>', views.deletemenu, name="deletemenu"),
    path('edit', views.edit, name="edit"),
    path('viewfacility', views.viewfacility, name="viewfacility"),
    path('addfacility', views.addfacility, name="addfacility"),
    path('facilityadd', views.facilityadd, name="facilityadd"),
    path('editfacility/<int:id>', views.editfacility, name="editfacility"),
    path('facilityedit', views.facilityedit, name="facilityedit"),
    path('deleterestaurantfacility/<int:id>', views.deleterestaurantfacility, name="deleterestaurantfacility"),
    path('viewrating', views.viewrating, name="viewrating"),
    path('map', views.map, name="map"),
    path('map1', views.map1, name="map1"),


    path('resortdashboard', views.resortdashboard, name="resortdashboard"),
    path('manageroom', views.manageroom, name="manageroom"),
    path('addroom', views.addroom, name="addroom"),
    path('roomadd', views.roomadd, name="roomadd"),
    path('editroom/<int:id>', views.editroom, name="editroom"),
    path('roomedit', views.roomedit, name="roomedit"),
    path('deleteroom/<int:id>', views.deleteroom, name="deleteroom"),
    path('viewresortfacility', views.viewresortfacility, name="viewresortfacility"),
    path('addresortfacility', views.addresortfacility, name="addresortfacility"),
    path('resortfacilityadd', views.resortfacilityadd, name="resortfacilityadd"),
    path('editresortfacility/<int:id>', views.editresortfacility, name="editresortfacility"),
    path('resortfacilityedit', views.resortfacilityedit, name="resortfacilityedit"),
    path('deleteresortfacility/<int:id>', views.deleteresortfacility, name="deleteresortfacility"),
    path('mapresort', views.mapresort, name="mapresort"),
    path('map2', views.map2, name="map2"),
    path('restaurant_home', views.restaurant_home, name="restaurant_home"),
    path('viewresortrating', views.viewresortrating, name="viewresortrating"),



    path('viewrest_android',views.viewrest_android,name='viewrest_android'),
    path('viewmore_restaurant',views.viewmore_restaurant,name='viewmore_restaurant'),
    path('menurestaurant_android',views.menurestaurant_android,name='menurestaurant_android'),
    path('resfacility_android',views.resfacility_android,name='resfacility_android'),
    path('restaurantrating_android',views.restaurantrating_android,name='restaurantrating_android'),
    path('viewresort_android',views.viewresort_android,name='viewresort_android'),
    path('viewmore_resort',views.viewmore_resort,name='viewmore_resort'),
    path('roomresort_android',views.roomresort_android,name='roomresort_android'),
    path('resortfacility_android',views.resortfacility_android,name='resortfacility_android'),
    path('resortrating_android',views.resortrating_android,name='viewresortrating_android'),
    path('resort_home', views.resort_home, name="resort_home"),




   ##########################################webservice########################################
    path('userregister', views.userregister, name="userregister"),
    path('logins', views.logins, name="logins"),
    path('touristplace_android', views.touristplace_android, name="touristplace_android"),
    path('touristrating_android', views.touristrating_android, name="touristrating_android"),
    path('view_resort_rating',views.view_resort_rating,name='view_resort_rating'),
    path('view_restaurant_rating',views.view_restaurant_rating,name='view_restaurant_rating'),
    path('viewrcmdrest_android',views.viewrcmdrest_android,name='viewrcmdrest_android'),
    path('viewrcmdresort_android',views.viewrcmdresort_android,name='viewrcmdresort_android'),
    path('viewrcmdtourist_android',views.viewrcmdtourist_android,name='viewrcmdtourist_android'),
    path('sendcomplaint',views.sendcomplaint,name='sendcomplaint'),
    path('sendfeedback',views.sendfeedback,name='sendfeedback'),
    path('identifyuser_android',views.identifyuser_android,name='identifyuser_android'),
    path('view_reply',views.view_reply,name='view_reply'),
























]