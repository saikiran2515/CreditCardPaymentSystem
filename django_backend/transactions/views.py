from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer

# module5
# daily payment summary view
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()

        status = self.request.GET.get('status')
        amount = self.request.GET.get('amount')
        date = self.request.GET.get('date')

        if status:
            queryset = queryset.filter(status=status)

        if amount:
            queryset = queryset.filter(amount=amount)

        if date:
            queryset = queryset.filter(
                created_at__date=date
            )

        return queryset

class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer



# add CSV Export functionality

import csv
from django.http import HttpResponse
from rest_framework.views import APIView


class ExportTransactionsCSV(APIView):

    def get(self, request):

        response = HttpResponse(
            content_type='text/csv'
        )

        response['Content-Disposition'] = (
            'attachment; filename="transactions.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            'User',
            'Amount',
            'Status',
            'Created At'
        ])

        transactions = Transaction.objects.all()

        for transaction in transactions:
            writer.writerow([
                transaction.user.username,
                transaction.amount,
                transaction.status,
                transaction.created_at
            ])

        return response



# module5
# daily payment summary view

class DailyPaymentSummary(APIView):

    def get(self, request):

        total_transactions = Transaction.objects.count()

        successful_payments = Transaction.objects.filter(
            status='SUCCESS'
        ).count()

        failed_payments = Transaction.objects.filter(
            status='FAILED'
        ).count()

        total_amount = Transaction.objects.aggregate(
            Sum('amount')
        )['amount__sum'] or 0

        return Response({
            "total_transactions": total_transactions,
            "successful_payments": successful_payments,
            "failed_payments": failed_payments,
            "total_amount": total_amount
        })