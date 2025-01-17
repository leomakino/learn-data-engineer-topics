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
Pub/Sub is an asynchronous global messaging service. There are three terms in Pub/Sub that appear often: topics, publishing, and subscribing. A producer publishes messages to a topic and a consumer creates a subscription to a topic to receive messages from it.
- A topic is a shared string that allows applications to connect with one another through a common thread.
- Publishers push (or publish) a message to a Cloud Pub/Sub topic
- Subscribers make a "subscription" to a topic where they will either pull messages from the subscription or configure webhooks for push subscriptions. Every subscriber must acknowledge each message within a configurable window of time.


To use Pub/Sub, you create a topic to hold data and a subscription to access data published to the topic. 

Setting up Pub/Sub:
1. Create a topic
    - The topic must have a unique name.
1. Add a subscription
1. Publish a message to the topic

Features of the pull command:
- Using the pull command without any flags will output only one message
- Once an individual message has been outputted from a particular subscription-based pull command, you cannot access that message again with the pull command

Commands:
- create a topic: `gcloud pubsub topics create myTopic`
- List topics: `gcloud pubsub topics list`
- Delete topic: `gcloud pubsub topics delete Test1`
- create a subscription called mySubscription to topic myTopic: `gcloud pubsub subscriptions create --topic myTopic mySubscription`
- List subscription in a topic: `gcloud pubsub topics list-subscriptions myTopic`
- Delete subscription: `gcloud pubsub subscriptions delete Test1`
- publish the message "hello" to the topic: `gcloud pubsub topics publish myTopic --message "Hello"`
- pull command to get the messages from a topic: `gcloud pubsub subscriptions pull mySubscription --auto-ack`
- pull more than one message `gcloud pubsub subscriptions pull mySubscription --auto-ack --limit=3`
