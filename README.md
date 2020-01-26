# Example GraphQL with Django

This application has queries, mutations and file uploads.

## Steps required to start the application

1.  It is recommended to use **Python 3.4** or higher
2.  Install the packages contained in **requirements.txt** using the command installation of `pip install -r requirements.txt`
3.  Execute the run.py file with `python manage.py makemigrations`
4.  Execute the run.py file with `python manage.py migrate`
5.  Execute the run.py file with `python manage.py runserver`
6.  Open the browser and go to the address <http://localhost:8000/> or <http://127.0.0.1:8000/>

---

## Queries

```
query {
  allCategories {
    totalCount
    edges {
      node {
        id
        name
        ingredients {
          totalCount
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}
```

---

## Mutations
### Create category
```
mutation {
  createCategory(input: {name: "category"}) {
    category {
      id
      name
    }
  }
}
```

### Update category
```
mutation {
  updateCategory(input: {id: "identifier", name: "update category"}) {
    category {
      id
      name
      ingredients {
        totalCount
        edges {
          node {
            id
            name
          }
        }
      }
    }
  }
}
```

### Delete category
```
mutation d {
  deleteCategory(input: "identifier") {
    category {
      id
      name
    }
  }
}
```

---

## Steps required to upload image

### Single file

#### Operations

    {
      query:
        mutation($folder_id: ID!, $image: Upload!) {
          uploadImage(folderId: $folder_id, image: $image) {
            message
          }
        }
      ,
      variables: {
        dir: directory
        image: example.png
      }
    }

#### cURL request

    curl localhost:8000/graphql/ \
    -F operations='{ "query": "mutation ($image: Upload!, $folder_id: ID!) { uploadImage(folderId: $folder_id, image: $image) { message } }", "variables": { "image": null, "folder_id": 1 } }'
    -F map='{ "0": ["variables.image"] }' \
    -F 0=@example.jpg
