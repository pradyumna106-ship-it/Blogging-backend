# Blogging Backend API

A Django REST API for a blogging platform that allows users to create, read, update, and delete blog posts with categories and tags.

**Reference:** [Blogging Platform API - Roadmap.sh](https://roadmap.sh/projects/blogging-platform-api)

---

## Features

✨ **Core Features:**
- ✅ Create, Read, Update, and Delete (CRUD) blog posts
- ✅ Categorize posts (Technology, Lifestyle, Education, Travel)
- ✅ Tag-based organization for posts
- ✅ RESTful API endpoints
- ✅ Timestamp tracking (created_at, updated_at)
- ✅ Full error handling with appropriate HTTP status codes

---

## Tech Stack

- **Framework:** Django 5.2.3
- **API:** Django REST Framework
- **Database:** SQLite3
- **Language:** Python

---

## Project Structure

```
Blogging-backend/
├── bloging/                    # Main project settings
│   ├── settings.py            # Django configuration
│   ├── urls.py                # Project URL routing
│   ├── asgi.py                # ASGI configuration
│   ├── wsgi.py                # WSGI configuration
│   └── __init__.py
│
├── personal/                  # Main Django app
│   ├── migrations/            # Database migrations
│   ├── models.py              # Post and Tag models
│   ├── views.py               # API view handlers
│   ├── serializers.py         # DRF serializers
│   ├── urls.py                # App URL routing
│   ├── admin.py               # Django admin configuration
│   ├── apps.py                # App configuration
│   └── tests.py               # Unit tests
│
├── manage.py                  # Django management script
├── db.sqlite3                 # SQLite database
└── README.md                  # This file
```

---

## Database Models

### Post Model
```python
- title: CharField (max 200 characters)
- content: TextField
- category: CharField (predefined choices)
- tags: ManyToManyField (related to Tag model)
- created_at: DateTimeField (auto-set on creation)
- updated_at: DateTimeField (auto-updated)
```

### Tag Model
```python
- name: CharField (max 50 characters, unique)
```

### Category Choices
- Technology
- Lifestyle
- Education
- Travel

---

## API Endpoints

### 1. Get All Posts
```
GET /api/posts/
```
**Description:** Retrieves all blog posts  
**Response:**
```json
[
  {
    "id": 1,
    "title": "Sample Post",
    "content": "Post content here",
    "category": "Technology",
    "tags": [1, 2],
    "created_at": "2026-01-20T06:24:53Z",
    "updated_at": "2026-01-20T06:24:53Z"
  }
]
```

### 2. Get Single Post
```
GET /api/posts/<id>/
```
**Description:** Retrieves a specific post by ID  
**Response:** Single post object (see above)  
**Error Response (404):**
```json
{
  "error": "Post not found"
}
```

### 3. Create Post
```
POST /api/posts/add/
```
**Description:** Creates a new blog post  
**Request Body:**
```json
{
  "title": "New Post",
  "content": "Post content",
  "category": "Technology",
  "tags": [1, 2]
}
```
**Response:** Created post object with ID

### 4. Update Post
```
PUT /api/posts/update/<id>/
PATCH /api/posts/update/<id>/
```
**Description:** Updates an existing post (supports partial updates with PATCH)  
**Request Body:** Same structure as create (all fields optional for PATCH)  
**Response:** Updated post object  
**Error Responses:**
```json
// 404 Not Found
{ "error": "Post not found" }

// 400 Bad Request
{ "field": ["error message"] }
```

### 5. Delete Post
```
DELETE /api/posts/delete/<id>/
```
**Description:** Deletes a blog post  
**Response (204 No Content):**
```json
{ "message": "Post deleted successfully" }
```
**Error Response (404):**
```json
{ "error": "Post not found" }
```

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/pradyumna106-ship-it/Blogging-backend.git
cd Blogging-backend
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install django djangorestframework
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create a superuser (optional, for admin panel)**
```bash
python manage.py createsuperuser
```

6. **Start the development server**
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

---

## Usage Examples

### Using cURL

**Get all posts:**
```bash
curl http://localhost:8000/api/posts/
```

**Create a post:**
```bash
curl -X POST http://localhost:8000/api/posts/add/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My First Post",
    "content": "This is my first blog post.",
    "category": "Technology",
    "tags": [1]
  }'
```

**Update a post:**
```bash
curl -X PUT http://localhost:8000/api/posts/update/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title"
  }'
```

**Delete a post:**
```bash
curl -X DELETE http://localhost:8000/api/posts/delete/1/
```

### Using Python Requests

```python
import requests

BASE_URL = "http://localhost:8000/api/posts"

# Get all posts
response = requests.get(f"{BASE_URL}/")
posts = response.json()

# Create a post
new_post = {
    "title": "Python API Testing",
    "content": "Testing Django REST API",
    "category": "Technology",
    "tags": [1, 2]
}
response = requests.post(f"{BASE_URL}/add/", json=new_post)
created_post = response.json()

# Update a post
updated_data = {"title": "Updated Title"}
response = requests.patch(f"{BASE_URL}/update/1/", json=updated_data)

# Delete a post
response = requests.delete(f"{BASE_URL}/delete/1/")
```

---

## Admin Panel

Access Django Admin at `http://localhost:8000/admin/`

- Manage posts directly
- Create/edit tags
- View timestamps and audit history

---

## Error Handling

The API returns appropriate HTTP status codes:
- **200 OK:** Successful GET/PUT request
- **201 Created:** Successful POST request (when implemented)
- **204 No Content:** Successful DELETE request
- **400 Bad Request:** Invalid request data (validation errors)
- **404 Not Found:** Resource not found
- **500 Internal Server Error:** Server-side error

---

## Testing

Run tests with:
```bash
python manage.py test
```

---

## Configuration

Key settings in `bloging/settings.py`:
- `DEBUG = True` (set to False in production)
- Database: SQLite3 (can be changed to PostgreSQL/MySQL)
- `INSTALLED_APPS`: Includes `personal` and `rest_framework`

---

## Future Enhancements

- 🔐 User authentication & authorization
- 📧 Email notifications
- 💬 Comments on posts
- ⭐ Post ratings/likes
- 🔍 Full-text search
- 🏷️ Advanced filtering and pagination
- 🌐 API documentation (Swagger/OpenAPI)
- 📱 File uploads/media support

---

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

---

## License

This project is open source and available under the MIT License.

---

## Author

**Pradyumna** - [@pradyumna106-ship-it](https://github.com/pradyumna106-ship-it)

---

## Support

For issues, questions, or suggestions, please open an issue on GitHub.
