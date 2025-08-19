ALX Travel App - Airbnb Clone Backend

A Django REST Framework-based backend for an Airbnb-like travel application, built as part of the ALX portfolio project.
🚀 Features

    User Authentication: JWT-based authentication system

    Property Management: CRUD operations for property listings

    Booking System: Complete booking lifecycle management

    Reviews & Ratings: Guest review system with host responses

    Search & Filtering: Advanced property search with multiple filters

    Payment Integration: Stripe payment processing

    API Documentation: Swagger/OpenAPI documentation

    Database Seeding: Management command for sample data

🛠️ Technology Stack

    Backend Framework: Django 4.2.7

    API Framework: Django REST Framework 3.14.0

    Database: MySQL

    Authentication: JWT Tokens

    API Documentation: drf-yasg (Swagger/OpenAPI)

    Task Queue: Celery with Redis

    File Storage: AWS S3 (via django-storages)

    CORS Handling: django-cors-headers

📋 Project Structure
text

alx_travel_app/
├── alx_travel_app/          # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py             # Main URL routing
│   └── celery.py           # Celery configuration
├── listings/               # Main application
│   ├── models.py          # Database models
│   ├── serializers.py     # DRF serializers
│   ├── views.py           # API views
│   ├── urls.py           # App URL routing
│   └── management/
│       └── commands/
│           └── seed.py    # Database seeder
├── core/                  # Common utilities
├── requirements.txt       # Python dependencies
└── .env                  # Environment variables

🗄️ Database Models
Key Entities:

    User: Authentication and user profiles

    Listing: Property listings with details and amenities

    Booking: Reservation records with status tracking

    Review: Guest reviews and host responses

    Payment: Transaction records

🔌 API Endpoints
Authentication

    POST /api/auth/register - User registration

    POST /api/auth/login - User login

    POST /api/auth/refresh - Token refresh

Listings

    GET /api/listings/ - List all properties

    POST /api/listings/ - Create new listing

    GET /api/listings/{id}/ - Get listing details

    PUT /api/listings/{id}/ - Update listing

    DELETE /api/listings/{id}/ - Delete listing

Bookings

    GET /api/bookings/ - User's bookings

    POST /api/bookings/ - Create new booking

    GET /api/bookings/{id}/ - Booking details

    PUT /api/bookings/{id}/ - Update booking

    DELETE /api/bookings/{id}/ - Cancel booking

Reviews

    GET /api/listings/{id}/reviews/ - Listing reviews

    POST /api/listings/{id}/reviews/ - Create review

    PUT /api/reviews/{id}/ - Update review

🚦 Installation & Setup
Prerequisites

    Python 3.8+

    MySQL 5.7+

    Redis

    Git

1. Clone the Repository
bash

git clone <repository-url>
cd alx_travel_app

2. Set Up Virtual Environment
bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

3. Install Dependencies
bash

pip install -r requirements.txt

4. Environment Configuration

Create .env file:
bash

# Database
DB_NAME=alx_travel_db
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306

# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0

5. Database Setup
sql

CREATE DATABASE alx_travel_db;

6. Run Migrations
bash

python manage.py migrate

7. Create Superuser
bash

python manage.py createsuperuser

8. Seed Sample Data
bash

python manage.py seed

9. Start Development Server
bash

python manage.py runserver

📊 Database Seeding

The project includes a management command to populate the database with sample data:
bash

python manage.py seed

This command creates:

    Sample users (hosts and guests)

    Property listings with various amenities

    Bookings with different statuses

    Reviews and ratings

📖 API Documentation

Access interactive API documentation at:

    Swagger UI: http://localhost:8000/swagger/

    ReDoc: http://localhost:8000/redoc/

🧪 Testing

Run the test suite:
bash

python manage.py test

🚀 Deployment
Production Settings

    Set DEBUG=False

    Configure production database

    Set up proper ALLOWED_HOSTS

    Configure static files serving

    Set up SSL/HTTPS

    Configure email backend

Environment Variables for Production
bash

# Set in production environment
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=mysql://user:password@host:port/database
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

🤝 Contributing

    Fork the repository

    Create a feature branch (git checkout -b feature/amazing-feature)

    Commit changes (git commit -m 'Add amazing feature')

    Push to branch (git push origin feature/amazing-feature)

    Open a Pull Request

📝 License

This project is part of the ALX portfolio program.
🆘 Support

For support, please open an issue in the GitHub repository or contact the development team.
🔄 Version History

    v1.0.0 (Current)

        Initial release with core functionality

        User authentication and authorization

        Property management system

        Booking system

        Review and rating system

        API documentation

Note: This is a portfolio project for educational purposes. Not intended for production use without proper security auditing and testing.

