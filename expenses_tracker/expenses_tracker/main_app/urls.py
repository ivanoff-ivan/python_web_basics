from django.urls import path

from expenses_tracker.main_app.views import show_home_page, show_create_expense_page, show_edit_expense_page, \
    show_delete_expense_page, show_profile_page, show_profile_edit_page, show_profile_delete_page

urlpatterns = [
    path('', show_home_page, name='home page'),
    path('create/', show_create_expense_page, name='create expense page'),
    path('edit/<int:pk>/', show_edit_expense_page, name='edit expense page'),
    path('delete/<int:pk>/', show_delete_expense_page, name='delete expense page'),
    path('profile/', show_profile_page, name='profile page'),
    path('profile/edit/', show_profile_edit_page, name='profile edit page'),
    path('profile/delete/', show_profile_delete_page, name='profile delete page'),
]
