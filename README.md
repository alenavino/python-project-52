### Hexlet tests and linter status:
[![Actions Status](https://github.com/alenavino/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alenavino/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/303e542000f5c6b19a4f/maintainability)](https://codeclimate.com/github/alenavino/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/303e542000f5c6b19a4f/test_coverage)](https://codeclimate.com/github/alenavino/python-project-52/test_coverage)
# Task manager
[Task manager](https://task-manager-evr6.onrender.com/) is a task management system. It allows you to set tasks, assign performers and change their statuses.
## Registration and authentication are required to work with the system
### Registration:
![Registration](https://github.com/user-attachments/assets/172fd9f5-dbea-4fce-977c-f52c86e2f34f)
### Login:
![Login](https://github.com/user-attachments/assets/cc385dfc-bff2-4a5a-b1ab-96e411de4832)
## After logging in, we have access to tasks, their statuses and labels
### Home page:
![Home](https://github.com/user-attachments/assets/55966f64-b35e-44e0-863b-4fc10eb60f88)
### List of tasks:
![Tasks](https://github.com/user-attachments/assets/8435a3a0-30c7-4941-9e78-e50a27253c53)

## Dependencies

- python = "^3.10"
- poetry = "^1.8.3"

# Install & start

```
git clone git@github.com:alenavino/python-project-52.git
cd python-project-52/
```

Create a file .env in the root of the project and add the variables SECRET_KEY, DEBUG, ACCESS_TOKEN and DATABASE_URL to it

```
# install poetry
make install
# start server locally
make start
```




