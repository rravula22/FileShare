# Flask AWS File Sharing Application

This is a Flask application for file sharing and emailing using AWS services. The application allows users to upload files to an AWS S3 bucket, share the file link via email, and generate a pre-signed URL for file access.

## Prerequisites

Before running the application, make sure you have the following:

- Python installed on your machine.
- An AWS account with the necessary credentials and permissions set up.
- The required Python libraries installed (`Flask`, `boto3`, `mysql-connector-python`, `requests`).

## Usage

1. Clone the repository and navigate to the project folder.

2. Install the required dependencies:

```bash
pip install Flask boto3 mysql-connector-python requests
```

3. Set up your AWS credentials:

   - Create a file named `key.json` with the following structure:

     ```json
     {
       "access_key": "YOUR_AWS_ACCESS_KEY",
       "secret_key": "YOUR_AWS_SECRET_KEY",
       "bucket": "YOUR_S3_BUCKET_NAME"
     }
     ```

     Replace `YOUR_AWS_ACCESS_KEY`, `YOUR_AWS_SECRET_KEY`, and `YOUR_S3_BUCKET_NAME` with your AWS credentials and S3 bucket name.

4. Start the Flask server:

```bash
python app.py
```

5. The server will start running on http://localhost:5000.

6. Open your browser and navigate to http://localhost:5000 to access the application.

## Routes

- **GET /:** Renders the index.html template.

- **POST /submitForm:** Handles user login form submission and checks the user's credentials against the database.

- **POST /uploadFile:** Uploads a file to the specified AWS S3 bucket.

- **POST /sendemail:** Sends emails with the file link to the specified recipients.

- **GET /report:** Renders the report.html template.

## AWS Services Used

- **Amazon S3:** Used for file storage and retrieval.

- **AWS Lambda and API Gateway:** Used to trigger the email sending process via a serverless API endpoint.

## Database

The application connects to a MySQL database running on the RDS instance with the following configuration:

- Host: cloudfinaldb.cl7uutdsqhvw.us-east-1.rds.amazonaws.com
- Port: 3306
- Username: admin
- Region: us-east-1c
- Database: clouddb

Ensure that you have the necessary database set up with the required user table.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - A lightweight web framework for Python.
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK for Python.
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - MySQL driver for Python.
- [requests](https://docs.python-requests.org/en/latest/) - A library for sending HTTP requests.
