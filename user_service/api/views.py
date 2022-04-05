from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer

# Create your views here.
class UserView(viewsets.ViewSet):

    def listUsers(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def createUser(self, request):
        serializer = AccountSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieveUser(self, request, pk=None):
        try:
            accounts = Account.objects.get(id=pk)
        except Account.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AccountSerializer(accounts)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def deleteUser(self, request, pk=None):
        try:
            accounts = Account.objects.get(id=pk)
            accounts.delete()
        except Account.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_204_NO_CONTENT)