from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.registerUser,name='register'),
    path('register/validateForm1',views.validateForm1,name='val1'),
    path('register/done',views.postInfo,name='postInfo'),
    path('register/socialDone/',views.postInfoAccs,name='postInfoacc'),
    path('login/',views.loginApi,name='login'),
    path('logout/',views.logoutApi,name='logout'),
    path('getMeh/<str:username>/',views.returnUserData,name='userdata'),
    path('register/socialDone/edit/',views.editProfile,name='editprofile'),
    path('register/socialDone/edit/done/',views.postInfoAccsUp,name='editprofileDone'),
    path("forgot-password/",views.forgotpassword,name='forgot-password'),
    path("requestOtp/",views.requestOtp,name="request-otp"),
    path("verifyOtp/",views.verifyOtp,name="verify-otp"),
    path("reset-password/",views.resetpasswordPage,name="reset-pswd"),
    path("reset-password/done/",views.resetPswdDone, name="reset-pswd-done"),
]