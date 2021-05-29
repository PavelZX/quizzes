from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('getquizzes', views.get_quizzes),
  path('addquiz', views.add_quiz),
  path('updatequiz/<int:quiz_id>', views.update_quiz),
  path('deletequiz/<int:quiz_id>', views.delete_quiz),
  path('getmatters', views.get_matter),
  path('addmatter', views.add_matter),
  path('updatematter/<int:matter_id>', views.update_matter),
  path('deletematter/<int:matter_id>', views.delete_matter)
]