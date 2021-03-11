
## assignment Overview

Objective of this assignment, operationalize a Machine Learning Microservice API. 

You are given a pre-trained, `sklearn` model that has been trained to predict housing prices in Boston according to several features, such as average rooms in a home and data about highway access, teacher-to-pupil ratios, and so on. You can read more about the data, which was initially taken from Kaggle, on [the data source site](https://www.kaggle.com/c/boston-housing). This assignment tests your ability to operationalize flask app—in a provided file, `app.py`—that serves out predictions (inference) about housing prices through API calls. This assignment could be extended to any pre-trained machine learning model.
Just remember during the launch of container it requires `python app.py` from CMD.

### assignment Tasks

Your assignment goal is to operationalize this working, machine learning microservice using [kubernetes](https://kubernetes.io/),assignment you will:
* Complete a Dockerfile to containerize this application
* Deploy your containerized application using Docker and make a prediction.
* Improve the log statements in the source code for this application.
* Configure Kubernetes and create a Kubernetes cluster
* Deploy a container using Kubernetes and make a prediction(make_prediction.sh already included for the reference on sending request), add deployment and a service for handling heavy payload.
* add additional command in makefile if require.

**The final implementation of the assignment will showcase your abilities to operationalize production microservices.**
**Payload will be in the form of Json file and expected sample output from docker and kubernetes have been included inside samp_output_txt.**

---

## Setup the Environment

* Install python3 and virtualenv.
* Create a virtualenv and activate it
* Run `make install` to install the necessary dependencies

### Running `app.py`

#### Standalone:
`app.py` contains the web app built using flask framework.

`python app.py`

#### Include Dockerfile, Run in Docker

#### Run in Kubernetes: 

### Verify that application is running

### Upload to Docker Hub

### Kubernetes Steps

* Setup and Configure Docker locally
* Setup and Configure Kubernetes locally
* Create Flask app in Container
* Include POD profiling
* Add applicable service type for load balancing
* Run via kubectl
* Include documentation during submission
* Add additional packages inside requirements.txt if there are any
### Kubernetes Clean Up
### Git commit
