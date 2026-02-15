from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from .models import Fundraiser, Pledge, Favourite, Enquiry
from .permissions import IsOwnerOrReadOnly
from .serializers import FundraiserSerializer, PledgeSerializer, FundraiserDetailSerializer, FavouriteSerializer, EnquirySerializer

class FundraiserList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request):
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class FundraiserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request,pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        serializer = FundraiserDetailSerializer(fundraiser)
        return Response(serializer.data)
    
    def put(self, request, pk) :
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        if not request.user.is_staff:
            return Response(
                {"detail": "Only admin users can update fundraisers."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = FundraiserDetailSerializer(
            instance=fundraiser,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        if not request.user.is_staff:
            return Response(
                {"detail": "Only admin users can delete fundraisers."},
                status=status.HTTP_403_FORBIDDEN
            )
        fundraiser.delete()
        return Response(status=status.HTTP_200_OK)
                
class PledgeList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    
    def get(self, request):
        pledges = Pledge.objects.filter(supporter=request.user)
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user) #can
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class FavouriteCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        # Check if already favourited
        if Favourite.objects.filter(user=request.user, fundraiser=fundraiser).exists():
            return Response(
                {"detail": "You have already favourited this puppy."},
                status=status.HTTP_400_BAD_REQUEST
            )
        favourite = Favourite.objects.create(user=request.user, fundraiser=fundraiser)
        serializer = FavouriteSerializer(favourite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class FavouriteList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        favourites = Favourite.objects.filter(user=request.user)
        serializer = FavouriteSerializer(favourites, many=True)
        return Response(serializer.data)

class EnquiryCreate(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, fundraiser=fundraiser)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FundraiserPledgeList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        fundraiser = get_object_or_404(Fundraiser, pk=pk)
        pledges = Pledge.objects.filter(fundraiser=fundraiser)
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)