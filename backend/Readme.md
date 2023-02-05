# Deploy
### Create a vercel.json
```json
{
  "builds": [
    {
      "src": "backend/wsgi.py",
      "use": "@vercel/python",
      "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
    },
    {
      "src": "build_files.sh",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "staticfiles_build"
      }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "backend/wsgi.py"
    }
  ]
}
```
___
### Add to root/wsgi.py
```python
app = application
```
___
### Replace Sqlite database 