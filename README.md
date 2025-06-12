Blog Platform with Comments
Overview
This is a blogging platform built using Django REST Framework with Simple JWT authentication. Users can register, create posts (with title and description), comment on posts, and delete their own posts. The platform includes pagination for posts and comments and ensures that only the post author can delete their posts.
Features

User Authentication: Register and authenticate users using JWT tokens.
Post Management: Create, list, and delete posts (only by the post author).
Comment System: Add and retrieve comments for specific posts.
Pagination: Paginated responses for posts (5 per page) and comments (3 per page).
Authorization: Only authenticated users can create posts, comment, or delete their own posts.

Requirements

Python 3.8+
Django 4.2+
Django REST Framework
djangorestframework-simplejwt
A PostgreSQL database (or any other supported database)

Setup Instructions
1. Clone the Repository
git clone <repository-url>
cd blog-platform

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a .env file in the project root and add the following:
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/blog_db

5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

6. Create a Superuser (Optional)
python manage.py createsuperuser

7. Run the Development Server
python manage.py runserver

The API will be available at http://localhost:8000.
API Endpoints
Authentication

Register: POST /api/register/
Payload: { "username": "string", "password": "string", "confirm_password": "string" }
Response: { "message": "successfully created" } (201)
Renders register.html for GET requests.


Obtain JWT Token: POST /api/token/
Payload: { "username": "string", "password": "string" }
Response: { "refresh": "string", "access": "string" }


Refresh JWT Token: POST /api/token/refresh/
Payload: { "refresh": "string" }
Response: { "access": "string" }



Posts

List/Create Posts: GET/POST /api/posts/
GET: Returns a paginated list of all posts (5 per page).
POST: Creates a new post (requires authentication).
Payload: { "title": "string", "description": "string" }
Response: Post data (201 on success, 400 on error).


Retrieve/Delete Post: GET/DELETE /api/posts/<post_id>/
GET: Returns post details.
DELETE: Deletes the post (only by the author, requires authentication).
Response: 201 on success, 403 if not authorized.



Comments

List/Create Comments: GET/POST /api/posts/<post_id>/comments/
GET: Returns a paginated list of comments for a post (3 per page).
POST: Adds a comment to the specified post (requires authentication).
Payload: { "content": "string" }
Response: Comment data (201 on success, 400 on error).



Project Structure

Models:
Post: Stores post title, description, author, and creation timestamp.
Comment: Stores comment content, associated post, author, and creation timestamp.


Serializers:
PostSerializer: Handles serialization for Post model.
CommentSerializer: Handles serialization for Comment model.


Views:
RegisterView: Handles user registration.
PostListCreateAPIView: Manages post creation and listing.
PostDetailAPIView: Manages post retrieval and deletion.
CommentCreateAPIView: Manages comment creation and listing.


Pagination:
PostPagination: Limits posts to 5 per page.
CommentPagination: Limits comments to 3 per page.



Configuration
Update settings.py to include the following:
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    'your_app_name',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

Add the following to urls.py:
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from your_app_name.views import RegisterView, PostListCreateAPIView, PostDetailAPIView, CommentCreateAPIView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/posts/', PostListCreateAPIView.as_view(), name='post_list_create'),
    path('api/posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('api/posts/<int:post_id>/comments/', CommentCreateAPIView.as_view(), name='comment_create'),
]

Usage

Register a user via POST /api/register/.
Obtain a JWT token using POST /api/token/.
Use the access token in the Authorization header (Bearer <token>) for authenticated requests.
Create and manage posts and comments using the respective endpoints.

Notes

Ensure the register.html template is created for the registration form.
Only authenticated users can access post and comment APIs.
The PostDetailAPIView GET response currently only returns the post data. To include comments, modify the response to include comment_serializer.data as needed.

License
This project is licensed under the MIT License.
