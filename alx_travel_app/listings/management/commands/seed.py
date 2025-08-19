from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from decimal import Decimal
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'
    
    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Create or get admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@alxtravel.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write('Created admin user')
        
        # Create sample hosts
        hosts = []
        for i in range(1, 4):
            host, created = User.objects.get_or_create(
                username=f'host{i}',
                defaults={
                    'email': f'host{i}@alxtravel.com',
                    'first_name': f'Host{i}',
                    'last_name': 'Smith',
                }
            )
            if created:
                host.set_password('host123')
                host.save()
            hosts.append(host)
            self.stdout.write(f'Created host: {host.username}')
        
        # Create sample guests
        guests = []
        for i in range(1, 6):
            guest, created = User.objects.get_or_create(
                username=f'guest{i}',
                defaults={
                    'email': f'guest{i}@alxtravel.com',
                    'first_name': f'Guest{i}',
                    'last_name': 'Johnson',
                }
            )
            if created:
                guest.set_password('guest123')
                guest.save()
            guests.append(guest)
            self.stdout.write(f'Created guest: {guest.username}')
        
        # Sample listings data
        sample_listings = [
            {
                'title': 'Beautiful Beach House in Miami',
                'description': 'Stunning beachfront property with panoramic ocean views. Perfect for families and groups.',
                'property_type': 'house',
                'price_per_night': 250.00,
                'max_guests': 8,
                'num_bedrooms': 4,
                'num_beds': 6,
                'num_bathrooms': 3,
                'address': '123 Ocean Drive',
                'city': 'Miami',
                'state': 'Florida',
                'country': 'USA',
                'latitude': 25.7617,
                'longitude': -80.1918,
                'amenities': ['wifi', 'pool', 'air_conditioning', 'kitchen', 'tv', 'parking']
            },
            {
                'title': 'Cozy Downtown Apartment',
                'description': 'Modern apartment in the heart of the city. Close to restaurants and attractions.',
                'property_type': 'apartment',
                'price_per_night': 120.00,
                'max_guests': 4,
                'num_bedrooms': 2,
                'num_beds': 2,
                'num_bathrooms': 1,
                'address': '456 Main Street',
                'city': 'New York',
                'state': 'New York',
                'country': 'USA',
                'latitude': 40.7128,
                'longitude': -74.0060,
                'amenities': ['wifi', 'kitchen', 'tv', 'elevator']
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin surrounded by nature. Perfect for hiking and relaxation.',
                'property_type': 'cabin',
                'price_per_night': 95.00,
                'max_guests': 6,
                'num_bedrooms': 3,
                'num_beds': 4,
                'num_bathrooms': 2,
                'address': '789 Forest Road',
                'city': 'Aspen',
                'state': 'Colorado',
                'country': 'USA',
                'latitude': 39.1911,
                'longitude': -106.8175,
                'amenities': ['wifi', 'fireplace', 'kitchen', 'hiking_trails']
            },
            {
                'title': 'Luxury Villa with Private Pool',
                'description': 'Exclusive villa with private pool and stunning garden views.',
                'property_type': 'villa',
                'price_per_night': 450.00,
                'max_guests': 10,
                'num_bedrooms': 5,
                'num_beds': 7,
                'num_bathrooms': 4,
                'address': '101 Luxury Lane',
                'city': 'Los Angeles',
                'state': 'California',
                'country': 'USA',
                'latitude': 34.0522,
                'longitude': -118.2437,
                'amenities': ['wifi', 'pool', 'air_conditioning', 'kitchen', 'tv', 'parking', 'garden']
            },
            {
                'title': 'Modern City Condo',
                'description': 'Sleek condo with city views and modern amenities.',
                'property_type': 'condo',
                'price_per_night': 180.00,
                'max_guests': 4,
                'num_bedrooms': 2,
                'num_beds': 2,
                'num_bathrooms': 2,
                'address': '222 Urban Avenue',
                'city': 'Chicago',
                'state': 'Illinois',
                'country': 'USA',
                'latitude': 41.8781,
                'longitude': -87.6298,
                'amenities': ['wifi', 'gym', 'pool', 'concierge', 'parking']
            }
        ]
        
        # Create listings
        listings = []
        for i, listing_data in enumerate(sample_listings):
            host = hosts[i % len(hosts)]  # Distribute listings among hosts
            listing = Listing.objects.create(host=host, **listing_data)
            listings.append(listing)
            self.stdout.write(f'Created listing: {listing.title}')
        
        # Create sample bookings
        bookings = []
        for i in range(10):
            listing = random.choice(listings)
            guest = random.choice(guests)
            
            # Generate random dates
            check_in = datetime.now().date() + timedelta(days=random.randint(1, 30))
            check_out = check_in + timedelta(days=random.randint(2, 7))
            
            num_guests = random.randint(1, listing.max_guests)
            nights = (check_out - check_in).days
            total_price = listing.price_per_night * nights
            
            booking = Booking.objects.create(
                listing=listing,
                guest=guest,
                check_in_date=check_in,
                check_out_date=check_out,
                num_guests=num_guests,
                total_price=total_price,
                status=random.choice(['confirmed', 'completed', 'pending']),
                special_requests='Early check-in requested' if random.choice([True, False]) else ''
            )
            bookings.append(booking)
            self.stdout.write(f'Created booking for {listing.title}')
        
        # Create sample reviews
        for booking in bookings:
            if booking.status == 'completed' and random.choice([True, False]):
                review = Review.objects.create(
                    booking=booking,
                    guest=booking.guest,
                    listing=booking.listing,
                    rating=random.randint(4, 5),
                    comment=f'Great stay at {booking.listing.title}! Would recommend.',
                    is_approved=True
                )
                self.stdout.write(f'Created review for {booking.listing.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully seeded database with sample data!')
        )
        self.stdout.write(f'Created: {User.objects.count()} users, '
                         f'{Listing.objects.count()} listings, '
                         f'{Booking.objects.count()} bookings, '
                         f'{Review.objects.count()} reviews')
