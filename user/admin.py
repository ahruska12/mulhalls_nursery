from django.contrib import admin
from .models import Customer, Department, Employee, QuestionsAsked, SearchHistory

admin.site.register(Customer)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(QuestionsAsked)
admin.site.register(SearchHistory)
