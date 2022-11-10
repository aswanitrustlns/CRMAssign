from django.urls import URLPattern, path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from .views import *
urlpatterns=[
     path('login/',login,name="login"),
     path('LoginCheck',login_check,name="LoginCheck"),
     path('LogOut',logout,name="Logout"),
     path('dashboard/',dashboard,name="Dashboard"),
     path('viewTask',view_tasks,name='viewTask'),
     path('CRFDetails',detailed_page,name="CRFDetails"),
     path('display',viewall_users,name="display"),
     path('StatusUpdate',status_update,name="StatusUpdate"),
     path('ReassignTask',reassign_task,name="ReassignTask"),
     path('ViewDoc',view_document,name="ViewDoc"),
     path('CaseDetailUpdate',detail_status_update,name="CaseDetailUpdate")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


app_name='CRFAPP'