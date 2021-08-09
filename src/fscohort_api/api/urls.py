from django.urls import path
from .views import student_list_crate_api, student_get_update_delete


urlpatterns = [
    path("list/", student_list_crate_api, name="list"),
    path("list/<int:id>", student_get_update_delete, name="detail"),

]