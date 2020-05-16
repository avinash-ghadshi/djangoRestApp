# djangoRestApp

This is simple application written in Python DRF ( Django Rest Framework ).

### Pre-requisite
***You need to install following packages***
- Python3
    - for debian system
    - ``` $ sudo apt-get install python3 ```
    - for centos system
    - ``` $ sudo yum install python3 ```

### Project Setup

```
$ git clone https://github.com/avinash-ghadshi/djangoRestApp.git
$ cd djangoRestApp/django_api/
$ . venv/bin/activate
$ cd django_apis/
$ python manage.py runserver > /tmp/sdac.log 2>&1
```

Hit ``` http://127.0.0.1:8000/articles ``` on browser

URL supported by this app
> http://127.0.0.1:8000/articles
http://127.0.0.1:8000/articlesapi
http://127.0.0.1:8000/articlesgen/2
http://127.0.0.1:8000/articlesgen/1
http://127.0.0.1:8000/article/1
http://127.0.0.1:8000/article/1


NOTE:
If you get below error on any page
**"detail": "Authentication credentials were not provided."**

- just do following steps
    - on terminal
        - ``` $ python manage.py createsuperuser```
            - enter name and password as you want
    - Go to postman UI and do following things
        - click on authentication option and add username and password
        - Then click on send option [ Make sure request method is POST ]

**Enjoy!!!**

*Thanks for your contribution*
