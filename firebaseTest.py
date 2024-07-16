import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('secrets.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://streamlit-493fd-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules



ref2=db.reference()
ref2.set({"main":"123"})

# ref3=db.reference()
# ref3.update({"main":"123", "sub":"123456"})

# ref3.update({'ex':"text"})