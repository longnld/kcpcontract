from django.urls import path,include
from . import views
app_name='KCTool'
urlpatterns = [
    path('',views.kcToolPage,name="kcToolPage" ),
    path("vb-cho-xac-nhan/",views.newCreatedDocs,name="newCreatedDocs"),
    path("vb-da-xac-nhan/",views.confirmedDocs,name="confirmedDocs"),
    path("StaffManage/",views.staffManager,name="staffManager"),
    path("vb-da-ky/",views.signedDocs,name="signedDocs"),
    path("create-pdf", views.create_pdf, name="create_pdf"),
    path("getListAccount", views.getListAccount, name="getListAccount"),
    path("confirm_pdf", views.confirm_pdf, name="confirm_pdf"),
    path("sign_and_send_pdf",views.sign_and_send_pdf, name="sign_and_send_pdf"),
    path("send_pdf",views.send_pdf, name="send_pdf"),
    path("download_pdf",views.downloadFiles, name="download_pdf"),
    path("delete_file",views.deleteFile, name="delete_file"),
    path("RestoreFiles",views.restoreFile, name="restoreFiles"),
    path("delete_excel_file",views.deleteExcelFile, name="delete_file_excel"),
    path('update-profile', views.update_profile, name="update_profile"),
    path("vb-chua-duoc-quan-ly/",views.untrackedDocs,name="untrackedDocs"),
    path("updateProfile",views.updateProfile,name="updateProfile"),
    path("delete_profile/",views.delete_profile,name="delete_profile"),
    path("NewProfile/",views.addNewProfile,name="addNewProfile"),
    path("RecycleBin/",views.deletedDocs,name="deletedDocs"),
    path('get_info',views.get_info,name='get_info'),

    path("thong-tin-ho-tro",views.info_page,name="info_page")
]
