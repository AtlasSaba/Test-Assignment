# Simple Blog API
Django application that serves as a basic API for a blog.

## Prerequisites
- Python 3.x
## Getting Started

Follow these steps to run the project on your local machine:
- Clone the repo:
```
git clone https://github.com/AtlasSaba/Test-Assignment
```
- Move to the directory:
```
cd Test-Assignment
```
- Install requirements:
```
pip install -r requirements.txt
```
- Run the Development Server:
```
python manage.py runserver
```
- Access the Application:
```
http://127.0.0.1:8000/
```

### Api Endpoints
#### 1. Get All Blog Posts
- **URL**: `/api/all-posts/`
- **Method**: GET
- **Description**: Retrieve a list of all blog posts.
- **Example Response**: 
```
[{
        "id": 4,
        "title": "test #4",
        "content": "test #44 content",
        "publication_date": "2023-09-14T19:11:25Z"
    }]
```
#### 2. Get a Single Blog Post

- **URL**: `/api/blog-post/<post_id>/`
- **Method**: GET
- **Description**: Retrieve details of a single blog post by its ID.
- **Example Response**: /api/blog-post/6/
```
{
    "id": 6,
    "title": "test#6",
    "content": "content##6 test",
    "publication_date": "2023-09-14T19:35:18.132006Z"
}
```
#### 3. Create a New Blog Post

- **URL**: `/api/all-posts/`
- **Method**: POST
- **Description**: Create a new blog post.
- **Example Response**: Request body : *{"title":"test#7","content":"content##77 test"}*
```
{
    "id": 7,
    "title": "test#7",
    "content": "content##77 test",
    "publication_date": "2023-09-14T20:42:39.269197Z"
}
```
#### 4. Update a Blog Post

- **URL**: `/api/blog-post/<post_id>/`
- **Method**: PUT
- **Description**: Update an existing blog post by its ID.
- **Example Response**: /api/blog-post/6/
Request body : *{"title":"test#6 updated","content":"content##6 test upodated"}*
```
{
    "id": 6,
    "title": "test#6 updated",
    "content": "content##6 test updated",
    "publication_date": "2023-09-14T19:35:18.132006Z"
}
```
#### 5. Delete a Blog Post

- **URL**: `/api/blog-post/<post_id>/`
- **Method**: DELETE
- **Description**: Delete an existing blog post by its ID.
- - **Example Response**: /api/blog-post/6/
```
{
    "message": "successfully deleted blog post"
}
```