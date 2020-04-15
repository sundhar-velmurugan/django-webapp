### Visit the deployed app
https://django-trivia-blog.herokuapp.com/

### For local deployment 
- Create the following environment variables
```
SECRET_KEY='refer settings.py file'
DEBUG_VALUE='True'
EMAIL_HOST_USER='your-name@mail.com'
EMAIL_HOST_PASSWORD='your-password'
EMAIL_HOST='smtp-host-name'
EMAIL_PORT='port-number'
EMAIL_USE_TLS='True'
AWS_ACCESS_KEY_ID='aws-access-key-id'
AWS_SECRET_ACCESS_KEY='aws-secret-access-key'
AWS_STORAGE_BUCKET_NAME='bucket-name'
AWS_S3_REGION_NAME="s3-region"
AWS_S3_SIGNATURE_VERSION="s3v4"
```
- Install dependencies
`pip3 install -r requirements.txt`
- Run the server
`python manage.py runserver`