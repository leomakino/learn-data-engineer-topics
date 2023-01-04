# Introduction to AWS Boto in Python
## Course Description
What if you were no longer constrained by the capabilities of your laptop? What if you could get an SMS when a city garbage truck camera spots a missing a cat? This is all possible with cloud technology. This course will teach you how to integrate Amazon Web Services (AWS) into your data workflow. You’ll learn how to upload data to S3, AWS cloud storage. You’ll use triggers from your analysis to send text messages with AWS SNS. You will use Rekognition to detect objects in an image. And you will use Comprehend to decide if a piece of feedback is negative. By the time you’re done, you will learn how to build a pipeline, subscribe people to it, and send them text messages when an image contains a cat!

## Putting Files in the Cloud
Embark on the world of cloud technology! From learning how AWS works to creating S3 buckets and uploading files to them. You will master the basics of setting up AWS and uploading files to the cloud!

### AWS and Boto3 Introduction
What is Amazon Web Services?
It is a cloud computing platform provided by Amazon that includes over than 200 services.

What is Boto3?
- It is the name of the Python SDK for AWS.
- It allows you to directly create, update, and delete AWS resources from your Python scripts.


What is the AWS Console?
The AWS Management Console is a web application that comprises and refers to a broad collection of service consoles for managing AWS resources

IAM keys
    Identity and Access Management (IAM): It specifies who or what can access services and resources in AWS
    Access Key ID: It is like a username to an AWS account
    Secret Access Key: It is like a password to an AWS account

Connect to S3 Using Boto
**boto3.client** Create a low-level service client by name using the default session.
```PYTHON
import boto3
s3_client = boto3.client('s3',
    region_name='us-east-1',
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET)
```


### Diving into buckets
S3 lets us put any file in the cloud and make it accessible anywhere through a URL
Managing cloud storage is a key component of data pipelines
 

The main components of S3 are Buckets and Objects:
- Buckets are like folders on our computers
- Objects are like files wiithin those folders
- Buckets have their own permissions policies
- Buckets can generate logs about their own activity and write them to a different bucket


Creating a bucket
```PYTHON
# Create boto3 client
import boto3
s3 = boto3.client('s3', region_name='us-east-1',
                    aws_access_key_id=AWS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET)

# Create Bucket
bucket = s3.create_bucket(Bucket='bucket_name')
```

Listing buckets
```PYTHON
bucket_response = s3.list_buckets()
# Get buckets dictionary
buckets = bucket_response['Buckets']
print(buckets)
```

Delete Buckets
```PYTHON
response = s3.delete_bucket('bucket_name')
```

There are more operations that we can read about in the [boto3 documentation S3 session](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)


### Uploading and retrieving files
Bucket rules:
- A bucket has a name
- Name is a string
- Unique name in all of S3
- Contains many objects

Object rules
- An object has a key
- An object key is the full path from bucket root
- Can only be in one parent bucket
- The object key (or key name) uniquely identifies the object in an Amazon S3 bucket.
- Object key naming guidelines

Upload file
```PYTHON
s3.upload_file(
Filename='sample.csv',
Bucket='bucket_name',
Key='sample.csv')
```

List objects
```PYTHON
response = s3.list_objects(
Bucket='bucket_name',
MaxKeys=2,
Prefix='sample' # optional)
```

Head objects
```PYTHON
response = s3.head_object(
    Bucket='bucket_name',
    Key='sample.csv')
```

Download file
```PYTHON
s3.download_file(
    Filename='sample.csv',
    Bucket='bucket_name',
    Key='sample.csv')
```

Delete Object
```PYTHON
s3.delete_object(
    Bucket='bucket_name',
    Key='sample.csv')
```

---

## Sharing Files Securely
Continue your journey in mastering AWS by learning how to upload and share files securely. You will learn how set files to be public or private, and cap off what you learned by generating web-based reports! 

### Keeping objects secure
Often we work with private data or data we want only certain users to see.
This is where AWS permission system comes in.

There is four ways we can control permissions in S3.
- **Identity and access management** (IAM) is a framework of policies and technologies to ensure that the right users have the appropriate access to technology resources.
- A **Bucket Policy** is a resource-based policy that is used to grant access permissions to the bucket and the objects in it.
- The **Access Control List** (ACL) enables the admin to manage access to buckets and objects. It makes a specific object she's trying to share public to the world!
- A **Presigned URL** is a URL that you can provide to your users to grant temporary access to a specific S3 object.
*Note: AWS defaults to denying permission*

Set ACL
```PYTHON
s3.put_object_acl(
Bucket='bucket_name', Key='sample.csv', ACL='public-read')
```

Setting ACLs on upload
```PYTHON
s3.upload_file(
Bucket='bucket_name',
Filename='sample.csv',
Key='sample.csv',
ExtraArgs={'ACL':'public-read'})

```
The Public Object URL format is 'https://{bucket}.s3.amazonaws.com/{key}'


### Accessing private objects in S3
Use '.get_object()' to acess private files
```PYTHON
obj = s3.get_object(Bucket='bucket_name', Key='sample.csv')
```

**Pre-signed URLs**
The pre-signed URLS expires after a certain timeframe and it is grat for temporary access
Generating presigned URL
```PYTHON
share_url = s3.generate_presigned_url(
        ClientMethod='get_object',
        ExpiresIn=3600,
        Params={'Bucket': 'bucket-requests','Key': 'potholes.csv'}
)
```

### Sharing files through a website
S3 is able to serve HTML pages.
It can be useful when we want to share the results of an analyses and update the results via a pipeline.

The objective of this section is to share our analyses publicly.

The pandas [dataframe.to_html()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_html.html) method is a great to generate an html table and following uploading it. 


Upload a file to an S3 object with the [upload_file](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.upload_file) method
```
s3.upload_file(
   Filename='The path to the file to upload',
   Bucket='BUCKET_NAME',
   Key='The name of the key to upload to',
    ExtraArgs={'Metadata': {'mykey': 'myvalue'}}
)
```
Note: In the ExtraArgs parameters, the ContentType follows the template name of the [Internet Assigned Numbers Authority (IANA) Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml)

Example:

| Name | Template         | Reference                |
|------|------------------|--------------------------|
| csv  | text/csv         | [RFC4180][RFC7111]       |
| png  | image/png        | [W3C][PNG_Working_Group] |
| pdf  | application/pdf  | [RFC8118]                |
| json | application/json | [RFC8259]                |

Uploading an HTML page to S3
```PYTHON
s3.upload_file(
    Filename='home_page.html',
    Bucket='BUCKET_NAME',
    Key='home_page.html',
    ExtraArgs = {
        'ContentType': 'text/html',
        'ACL': 'public-read'} # Share the URL publicly
)
```

Accessing the HTML file/page

https://{bucket}.s3.amazonaws.com/{key}

### Case Study: Generating a report Repository

Steps:
1. Prepare the Data
    1. Download the files for the month from the raw data bucket
    2. Concatenate them into one csv
    3. Create an aggregated DataFrame
2. Create the report
    1. Write the DataFrame to CSV and HTML
    2. Generate a Bokeh plot, save as HTML
3. Upload the report to shareable website
    1. Create a bucket
    2. Upload all the files for the month to S3
    3. Generate an home_page.html file that lists all the files
    4. Get the website URL

1.1 Read raw data files

```PYTHON
# Create list to hold our DataFrames
df_list = []

# Request the list of csv's from S3 with prefix; Get contents
response = s3.list_objects(
    Bucket='bucket_name',
    Prefix='2019_jan')

# Get response contents
request_files = response['Contents']

# Iterate over each object
for file in request_files:
    obj = s3.get_object(Bucket='bucket_name', Key=file['Key'])

# Read it as DataFrame
obj_df = pd.read_csv(obj['Body'])

# Append DataFrame to list
df_list.append(obj_df)
```

1.2 Concatenate them into one csv
```PYTHON
# Concatenate all the DataFrames in the list
df = pd.concat(df_list)
```

1.3 Create an aggregated Dataframe
```PYTHON
# No code yet
```


2.1 Write the DataFrame to CSV and HTML
```PYTHON
# Perform some aggregation
df.to_csv('jan_final_report.csv')
df.to_html('jan_final_report.html')
```

3.1 Create the report-bucket
```PYTHON
bucket = s3.create_bucket(Bucket='bucket-reports')
```

3.2 Upload all the files for the month to S3
```PYTHON
# Upload Aggregated CSV to S3
s3.upload_file(Filename='./jan_final_report.csv',
    Key='2019/jan/final_report.csv',
    Bucket='bucket-reports',
    ExtraArgs = {'ACL': 'public-read'})

# Upload HTML table to S3
s3.upload_file(Filename='./jan_final_report.html',
    Key='2019/jan/final_report.html',
    Bucket='bucket-reports',
    ExtraArgs = {
        'ContentType': 'text/html',
        'ACL': 'public-read'})
```

2.2 Generate a Bokeh plot, save as HTML
```PYTHON
# Assume that the Bokeh plot was generated
# Upload Aggregated Chart to S3
s3.upload_file(Filename='./jan_final_chart.html',
    Key='2019/jan/final_chart.html',
    Bucket='bucket-reports',
    ExtraArgs = {
        'ContentType': 'text/html',
        'ACL': 'public-read'})
```

Create home_page.html

```PYTHON
# List the bucket-reports bucket objects starting with 2019/
r = s3.list_objects(Bucket='bucket-reports', Prefix='2019/')

# Convert the response contents to DataFrame
objects_df = pd.DataFrame(r['Contents'])

# Create a column "Link" that contains website url + key
base_url = "https://bucket-reports."
objects_df['Link'] = base_url + objects_df['Key']

# Write DataFrame to html
objects_df.to_html('report_listing.html',
    columns=['Link', 'LastModified', 'Size'],
    render_links=True)

# Upload the file to bucket-reports bucket root.
s3.upload_file(
    Filename='./report_listing.html',
    Key='index.html',
    Bucket='bucket-reports',
    ExtraArgs = {
        'ContentType': 'text/html',
        'ACL': 'public-read'
})
```

---

## Reporting and Notifying!
Alerting humans and machines to take action is a key component in data engineering.
Let's learn how to automate sharing your findings with the world by building notification triggers for your analysis.

### SNS Topics

Amazon Simple Notification Service (SNS) is a notification service that 
    - provides a low-cost infrastructure for mass delivery of messages, predominantly to mobile users.
    - allows messaging between decoupled microservices applications or directly to users with SMS texts, push notifications, and email.

**Publishers** post messages to **topics** and **subscribers** receive them. The SNS components are:
    1. **Publishers** send messages from distributed systems, microservices, and other AWS services;
    2. **Topics** decouple message publishers from subscribers;
    3. **Subscribers** can include mobile apps, mobile phone numbers, and email address

Amazon Resource Names (ARNs) uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS, such as in IAM policies, Amazon Relational Database Service (Amazon RDS) tags, and sns topics

```PYTHON
# Create SNS Client
sns = boto3.client('sns',
    region_name='us-east-1',
    aws_access_key_id=AWS_KEY_ID,
    aws_secret_access_key=AWS_SECRET)

# Create a topic
response = sns.create_topic(Name='Topic_name')
topic_arn = response['TopicArn']

# Listing topics
response = sns.list_topics()


# Delete topic
sns.delete_topic(TopicArn='arn:aws:sns:us-east-1:320333787981:city_alerts')
```

### SNS Subscriptions
After created SNS topics, it's time to manage subscriptions to those topics. 
Managing subscriptions means how we choose who gets the notifications and how they get them.
Every subscription has a unique ID, an end point, a protocol and a status.
- ID: Unique ID
- Endpoint: the endpoint that you want to receive notifications, varying by protocol. 
- Status: Confirmed or pending confirmation status.
- Protocol: The protol that you want to use. Examples:
    - http and https
    - email and sms
    - application, lambda, and firehose.
```PYTHON
# Create a SMS subscription
response = sns.subscribe(
    TopicArn = 'arn:aws:sns:us-east-1:320333787981:city_alerts',
    Protocol = 'SMS',
    Endpoint = '+554899999999')

# Create an email subscription
response = sns.subscribe(
    TopicArn = 'arn:aws:sns:us-east-1:320333787981:city_alerts',
    Protocol='email',
    Endpoint='email@address.com')

# List subscriptions
sns.list_subscriptions()['Subscriptions']

# Delete subscription
sns.unsubscribe(
    SubscriptionArn='arn:aws:sns:us-east-1:320333787921:subscription_example:0f2dad1d-8844-4fe8
)

# Delete Multiple subscriptions
# First, get list of subscriptions
response = sns.list_subscriptions_by_topic(
    TopicArn='arn:aws:sns:us-east-1:320333787921:subscription_example') 
subs = response['Subscriptions']

# Then, unsubscribe SMS subscriptions
for sub in subs:
    if sub['Protocol'] == 'sms':
        sns.unsubscribe(sub['SubscriptionArn'])
```

### Send Messages
Publishers send a message to an Amazon SNS topic, a text message (SMS message) directly to a phone number, or a message to a mobile platform endpoint 

To publish to a topic, call the publish method with TpicArn, message, and subject as arguments.

```PYTHON
# Publish to a topic
response = sns.publish(
    TopicArn = 'arn:aws:sns:us-east-1:320333787981:subscription_example',
    Message = 'Body text of SMS or e-mail',
    Subject = 'Subject Line for Email'
)

# Send a single SMS
response = sns.publish(
    PhoneNumber = '+554899999999',
    Message = 'Body text of SMS or e-mail'
)
```
There are two ways to send a message. 
1. Publish a message to a topic
2. Send a one-off SMS

Publish to topic vs Single SMS

| Publish to a topic            | Send a single SMS                      |
|-------------------------------|----------------------------------------|
| Need a topic created          | Don't need a topic                     |
| Need to have subscribers      | Don't need subscriptions               |
| Better for multiple receivers | Just sends a message to a phone number |
| Easier list management        | Email option not available             |


## Pattern Rekognition

### Comprehending text

```PYTHON
# Initialize client
translate = boto3.client('translate',
    region_name='us-east-1',
    aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)

# Translate text
response = translate.translate_text(
    Text='Olá, tudo bem?',
    SourceLanguageCode='auto',
    TargetLanguageCode='es')

# Detect dominant language
response = comprehend.detect_dominant_language(
    Text="Hoy es un buen dia para tener un gran dia.")
```
