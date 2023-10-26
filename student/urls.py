from django.urls import path
from .views import list_students, create_student, detail_student, edit_student,delete_student

app_name = "student"

urlpatterns = [
    path('', list_students, name="list-student"),
    path('create-student', create_student, name="create-student"),
    path('detail-student/<int:student_id>', detail_student, name="detail-student"),
    path('edit-student/<int:student_id>', edit_student, name="edit-student"),
    path('delete_student/<int:student_id>', delete_student, name="delete-student"),
]
