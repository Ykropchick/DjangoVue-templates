# Frontend
ordinary development
The axios request send to main url
For example:
```vue
methods:{
    async recordSmth(){
      const data = {
        "name" : this.name,
        "surname": this.surname
      };
    const response = (await this.axios.post('record-score/', data)).data;
    console.log(response)
    }
}
```
### P.S don't uncomment anything in the vue.config.js  

# Backend
to develop through the usual request functions
For example:

```python
import json


def record_smth(request):
    data = json.loads(request.body)
    name = data['name']
    surname = data['surname']
    # Data is a model
    new_data = Data(name=name, surname=surname)
    new_data.save()
    response = {
        "success": True,
    }
    return JsonResponse(response)
```

# Connecting
Uncomment all in vue.config.js 
do in frontend ``` npm build ```  
do in backend ```./manage.py collectstatic```
### Your project prepare to deploy