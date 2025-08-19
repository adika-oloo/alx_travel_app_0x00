from rest_framework import serializers
from .models import Listing, Booking, Review
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class ListingSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    average_rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)
    review_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'property_type', 'price_per_night',
            'max_guests', 'num_bedrooms', 'num_beds', 'num_bathrooms',
            'address', 'city', 'state', 'country', 'latitude', 'longitude',
            'amenities', 'is_active', 'created_at', 'updated_at', 'host',
            'average_rating', 'review_count'
        ]
        read_only_fields = ['created_at', 'updated_at', 'host']

class BookingSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)
    listing = ListingSerializer(read_only=True)
    total_nights = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'guest', 'check_in_date', 'check_out_date',
            'num_guests', 'total_price', 'status', 'special_requests',
            'created_at', 'updated_at', 'total_nights'
        ]
        read_only_fields = ['created_at', 'updated_at', 'total_price']

class ReviewSerializer(serializers.ModelSerializer):
    guest = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id', 'booking', 'guest', 'listing', 'rating', 'comment',
            'host_response', 'is_approved', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'guest', 'listing']

class CreateListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'title', 'description', 'property_type', 'price_per_night',
            'max_guests', 'num_bedrooms', 'num_beds', 'num_bathrooms',
            'address', 'city', 'state', 'country', 'latitude', 'longitude',
            'amenities'
        ]

class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'listing', 'check_in_date', 'check_out_date', 'num_guests',
            'special_requests'
        ]
