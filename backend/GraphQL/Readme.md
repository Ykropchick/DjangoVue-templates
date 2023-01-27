# GraphQl

### It's the example how to setting GraphQl in django and vue




___
### Changed files 
* settings.py:
  ```python
  from django.views.decorators.csrf import csrf_exempt
  from graphene_django.views import GraphQLView
    INSTALLED_APPS = [
  ...
    'graphene_django'
  ...
  ]
  GRAPHENE = {
  "SCHEMA": "GraphQL.schema.schema",
    }
  ```
* root/urls.py:
  ```python
    urlpatterns = [
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
  ]
  ```

--- 
### Dependencies:
* Django
    * graphene_django 
* Vue
* npm install --save @apollo/client @vue/apollo-composable @vue/apollo-util graphql graphql-tag
  


---
### Vue Project:
* main.js
  ```vue
  const cache = new InMemoryCache()
  const httpLink = createHttpLink({
      uri: 'http://127.0.0.1:8001/graphql/'
      }
  )
  
  const apolloClient = new ApolloClient({
      link: httpLink,
      cache
  })
  
  const app = createApp({
      setup(){
          provide(DefaultApolloClient, apolloClient)
      },
      render: () => h(App)
  })
  ```
* Example:
  ```vue
    async created(){
      const ALL_USERS_QUERY = gql`
        query {
          users{
            id
            admin
           }
        }
      `
      const { result } = useQuery(ALL_USERS_QUERY)
      const users = computed( () => result.value?.users ?? [] )
      watchEffect(() => {
        console.log(users.value)
      })
  ```
---
### Additional Info
Auth via GraphQl: https://django-graphql-auth.readthedocs.io/en/latest/quickstart/
The Vue setting: https://www.apollographql.com/blog/frontend/getting-started-with-vue-apollo/



