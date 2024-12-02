# Essential Google Cloud Infrastructure: Foundation
This course introduces platform services provided by Google Cloud with a focus on Compute Engine.

The Cloud Mobile App is another way to interact with Google Cloud.
- start, stop, and SSH into Compute Engine instances and see logs from each instance
- set up customizable graphs showing key metrics such as CPU usage, network usage, requests per second, and server errors.
- The app even offers alerts and incident management and allows you to get up-to-date billing information for your projects and get billing alerts for projects that are going over budget.
- Manage VMs and database instances
- Manage apps in the App Engine
- Manage billinghttps://accounts.google.com/AddSession/signinchooser?service=accountsettings&sarp=1&continue=https%3A%2F%2Fconsole.cloud.google.com%2Fhome%2Fdashboard%3Fproject%3Dqwiklabs-gcp-04-42f7ccba5be1&ddm=1&flowName=GlifWebSignIn&flowEntry=AddSession#Email=student-04-7158ad184798@qwiklabs.net


The Google Cloud interface consists of two parts: the Cloud Console and Cloud Shell.
The Console:
- Provides a fast way to perform tasks.
- Presents options to you, instead of requiring you to know them.
- Performs behind-the-scenes validation before submitting the commands.

Cloud Shell provides:
- Detailed control
- A complete range of options and features
- A path to automation through scripting

## Commands
gcloud storage cp [MY_FILE] gs://[BUCKET_NAME]

gcloud compute regions list

### Create a persistent state in Cloud Shell
Create a subdirectory for materials used in this lab:
```mkdir infraclass```

Create a file called config in the infraclass directory:
```touch infraclass/config```

Create an environment variable
```INFRACLASS_REGION=southamerica-east1```

Append the value of your Region environment variable to the config file:
```echo INFRACLASS_REGION=$INFRACLASS_REGION >> ~/infraclass/config```

Edit the shell profile
```nano .profile```

Add the following line to the end of the file
```source infraclass/config```

Press Ctrl+O, ENTER to save the file, and then press Ctrl+X to exit nano.

Use the echo command to verify that the variable is still set
```echo $INFRACLASS_REGION```