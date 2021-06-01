from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'SANJITA29112000'
app.config['MYSQL_DB'] = 'project'

mysql = MySQL(app)



mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nayaksanjita29@gmail.com'
app.config['MAIL_PASSWORD'] = 'Ranjita@29112000'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        email = details['email']
        subject = details['subject']
        message=details['message']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUser(name,email, subject, message) VALUES (%s, %s, %s, %s)",
         (name,email, subject, message))
        mysql.connection.commit()
        cur.close()

        msg = Message(subject, sender = 'nayaksanjita29@gmail.com', recipients = [email])
        msg.body ="Dear "+ name+ "!! You will here back from us soon !!!"
        mail.send(msg)
        return render_template('submit.html')
    return render_template('index.html')





@app.route('/clubs', methods=['GET', 'POST'])
def clubs():
    return render_template("clubs.html")

@app.route('/fmem', methods=['GET', 'POST'])
def member():
   if request.method == "POST":
        details = request.form
        firstname = details['firstname']
        lastname =details['lastname']
        usn = details['usn']
        gender=details['gender']
        email=details['email']
        phone=details['phone']
        branch=details['branch']
        semester=details['semester']
        clubs=details['clubs']
        di={
            "IEEE":"sanjitavn29@gmail.com",
            "Onyx":"sanjitavn29@gmail.com",
            "ISSA":"sanjitavn29@gmail.com",
            "UCSP":"sanjitavn29@gmail.com",
            "Robotics":"sanjitavn29@gmail.com",
            "Force Ikshvaku":"sanjitavn29@gmail.com",
            "Agni Racing":"sanjitavn29@gmail.com",
            "Saeniks":"sanjitavn29@gmail.com"
        }
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO rege(firstname,lastname,usn,gender,email,phone,branch,semester,clubs) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)",
         (firstname,lastname,usn,gender,email,phone,branch,semester,clubs))
        mysql.connection.commit()
        cur.close()

        msg = Message("Club Registration", sender = 'nayaksanjita29@gmail.com', recipients = [email])
        msg.body ="Dear "+ firstname+ " !! You will here back from "+clubs+ " soon !"
        mail.send(msg)
        msg1= Message("Registration request",sender ='nayaksanjita29@gmail.com',recipients= [di[clubs]])
        msg1.body= "Name: " +firstname+" "+lastname+"\n"+"USN: "+usn+"\n"+"Gender: "+gender+"\n"+"Phone Number: "+phone+"\n"+"Branch: "+branch+"\n"+"Semester: "+semester+"\n"
        mail.send(msg1)
        return render_template('submit.html')
   return render_template('fmem.html')
    




if __name__ == '__main__':
    app.run(debug="true")