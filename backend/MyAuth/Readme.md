# MyAuth

### It's the backend authentication

It's use jwt tokens.

___
### Changed files
* admin.py:  
* models.py: 
* setting.py:
  ```python
    INSTALLED_APPS = [
  ...
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser'
  ...
  ]
  MIDDLEWARE = [
    ...
  'corsheaders.middleware.CorsMiddleware',
    ...
  ]
  CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
    'http://localhost:8081'
  ]
  
  REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': (
          'rest_framework.authentication.TokenAuthentication',
      ),
      'DEFAULT_PERMISSION_CLASSES': (
          'rest_framework.permissions.IsAuthenticated',
      )
  }
  ```
* root/urls.py:
  ```python
    urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
  ]
  ```

--- 
### Dependencies:
* django-cors-headers - headers for Cross-Origin Resource Sharing 
* djoser - Django authentication system
* djangorestframework - 

---
### Vue Project:
* main.js
  ```vue
  axios.defaults.baseURL = 'http://127.0.0.1:8001'
  ```

---
### Additional Info
To login: Post request on /token/login -d '{"username": '', "password"='}'  
To take info about you: Post request on /users/me -d '{"Authorization": "Token ${token}"}'  
To take info about users: Post request on /users -d '{"Authorization": "Token ${token}"}'
All requests must be with Token


