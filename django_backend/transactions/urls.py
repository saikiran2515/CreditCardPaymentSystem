from django.urls import path

from .views import (
    TransactionListView,
    TransactionCreateView,
    ExportTransactionsCSV,
# m5
    DailyPaymentSummary,
)

urlpatterns = [
    path('', TransactionListView.as_view()),
    path('add/', TransactionCreateView.as_view()),
    path('export/', ExportTransactionsCSV.as_view()),
    path('summary/', DailyPaymentSummary.as_view()),
]