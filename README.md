# Python3-Flask-Google App Engine-Bootsrtap
Instructions:
1. clone the repository and navigate to the directory
2. Create a virtual environment `$ python3 -m venv venv && source venv/bin/activate`
3. Install the dependencies `$ pip install -r requirements.txt`
4. Setup Google App Engine https://cloud.google.com/appengine/docs/standard/python3/quickstart
    - create/select project
    - enable billing, Cloud Build API
    - install Google Cloud CLI
5. Use your Google Cloud user credentials to authenticate with the Cloud SDK and enable local testing with Datastore: `gcloud auth application-default login`
6. Start the server `$ python main.py`
7. Go to [http://localhost:8080](http://localhost:8080) 

Website made with:
- python3
- flask
- Google App Engine
- Google datastore
- Bootstrap 

Functionality:
- View list of posts.
- Add/Edit/Delete posts.




