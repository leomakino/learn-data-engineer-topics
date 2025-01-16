# Set Up an App Dev Environment on Google Cloud
### Cloud Storage CLI/SDK
Bucket naming rules:
- Do not include sensitive information in the bucket name, because the bucket namespace is global and publicly visible.
- Bucket names must contain only lowercase letters, numbers, dashes (-), underscores (_), and dots (.). Names containing dots require verification.
- Bucket names must start and end with a number or letter.
- Bucket names must contain 3 to 63 characters. Names containing dots can contain up to 222 characters, but each dot-separated component can be no longer than 63 characters.
- Bucket names cannot be represented as an IP address in dotted-decimal notation (for example, 192.168.5.4).
- Bucket names cannot begin with the "goog" prefix.
- Bucket names cannot contain "google" or close misspellings of "google".
- Also, for DNS compliance and future compatibility, you should not use underscores (_) or have a period adjacent to another period or dash. For example, ".." or "-." or ".-" are not valid in DNS names.

1. Make your object publicly accessible: `gsutil acl ch -u AllUsers:R gs://YOUR-BUCKET-NAME/ada.jpg`
1. Remove public access: `gsutil acl ch -d AllUsers gs://YOUR-BUCKET-NAME/ada.jpg`

### Cloud Run Functions CLI/SDK
A Cloud Run function is a piece of code that runs in response to an event, such as an HTTP request, a message from a messaging service, or a file upload. Cloud events are things that happen in your cloud environment. These might be things like changes to data in a database, files added to a storage system, or a new virtual machine instance being created.

Since Cloud Run functions are event-driven, they only run when something happens. This makes them a good choice for tasks that need to be done quickly or that don't need to be running all the time.

For example:
- automatically generate thumbnails for images that are uploaded to Cloud Storage.
- send a notification to a user's phone when a new message is received in Pub/Sub.
- process data from a Cloud Firestore database and generate a report.

Cloud Run functions are event driven, meaning a trigger type must be specified. When deploying a new function, `--trigger-topic`, `--trigger-bucket`, or `--trigger-http` are common trigger events. When deploying an update to an existing function, the function keeps the existing trigger unless otherwise specified. 

Commands:
- set the default region `gcloud config set run/region REGION`
- Create a directory for the function code: `mkdir gcf_hello_world && cd $_`
- Invoke the PubSub with some data. `gcloud pubsub topics publish cf-demo --message="Cloud Function Gen2"`
- Check the logs:
```bash
gcloud functions logs read nodejs-pubsub-function \
  --region=REGION 
```

### Setting up Pub/Sub
To use Pub/Sub, you create a topic to hold data and a subscription to access data published to the topic. 

Setting up Pub/Sub:
1. Create a topic
    - The topic must have a unique name.
1. Add a subscription
1. Publish a message to the topic
