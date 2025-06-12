 # Blog API with Comments

## Project Description
This is a Django REST Framework-based project that provides a simple blogging API with JWT authentication. Users can register, create posts, comment on others' posts, and view content with pagination. Authentication is handled using djangorestframework-simplejwt.

## Prerequisites
     Python 3.8+
     Django 5.1.5
     djangorestframework
     djangorestframework-simplejwt

 ## Setup Instructions
 1. Clone the Repository
    git clone (https://github.com/juniap321/blog-application.git)
    cd Blog


# API Endpoints
    ## Authentication (JWT)
    POST /api/token/ – Obtain JWT access and refresh tokens

    ## User Registration
    POST /register/ – Register a new user

    ## Posts
    GET /posts/ – List all posts (paginated)
    POST /posts/ – Create a new post
    GET /postdetails/<int:pk>/ – Get a post's details 
    DELETE /postdetails/<int:pk>/ – Delete a post (only by the author)

    ## Comments
    POST /commentcreate/<int:post_id>/comment/ – Add a comment to a post
    GET /commentcreate/<int:post_id>/comment/ – Get comments on a post  