# Chat

### It's the example how to make chat

___
### Changed files 
* settings.py:
  ```python
  from django.views.decorators.csrf import csrf_exempt
  from graphene_django.views import GraphQLView
    INSTALLED_APPS = [
    'daphne' # necessarily on top
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
    * (with daphne{ the server application that help to run websocket}) python -m pip install -U channels["daphne")
    * (without daphne) pip install channels 
 
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
Docs: https://channels.readthedocs.io/en/stable/tutorial/part_2.html



