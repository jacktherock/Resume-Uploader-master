
# Resume Uploader

Basic Resume Uploader App created in `Django` using `Bootstrap`, `HTML`, `CSS`, `Jquery` .

This app include basic forms, modals, date fields, image upload fields, file upload fields, radio buttons and check boxes.

Run app to get basic understanding of all the fields in Django.


## Steps to run virtual environment

 - Clone the repository
```bash
  git clone https://github.com/jacktherock/Resume-Uploader-master.git
```

 - Create a virtual environment in `ResumeUploader` directory
```bash
  virtualenv venv
```

 - Now activate virtual environment
```bash
  .\venv\Scripts\activate
```

 - Now Install `requirements.txt` file
```bash
  python -m pip install -r requirements.txt
```

Know more about [Virtual Environment in Python](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

## Steps to run Django server

 - Go to main project directory where `manage.py` locates
```bash
  cd ResumeUploader
```

 - Create database
```bash
  python manage.py makemigrations
```

 - Create tables in database
```bash
  python manage.py migrate
```

 - Run Django Server
 ```bash
  python manage.py runserver
```

Now Resume Uploader app server will run properly.



## Support
All types of contributions will be accepted. 

# Thank You for Visiting !!
