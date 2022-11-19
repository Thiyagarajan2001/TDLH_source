import pyrebase

def submit(name,email_id,phone_number,message):
   firebaseconfig={
    'apiKey': "",
  'authDomain': "",
    "databaseURL":"",
  'projectId': "",
  'storageBucket': "",
  'messagingSenderId': "",
  'appId': "",
  'measurementId': "",
  "serviceAccount": "Key/key.json"
    }
   firebase=pyrebase.initialize_app(firebaseconfig)
   #auth=firebase.auth()
   db=firebase.database()
   feedback={'Name': name,'Phone Number': phone_number,'Email Id':email_id,'Feedback': message}
   db.push(feedback)

