from flask import Flask, render_template, request, session
import uuid
import os
import schedule

app = Flask(__name__)
app.secret_key="SecretKey"

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/design')
def design():
    return render_template("design.html") 


@app.route('/form/<string:design>', methods=["GET","POST"])
def form(design):
    
    session["design_sess"] = design
    return render_template("form.html")


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    design_upload = session.get("design_sess")
    if design_upload == 'design1':
        design_name = "design1.html"
            
    elif design_upload == 'design2':
        design_name = "design2.html"

    elif design_upload == "design3":
        design_name = "design3.html"

    elif design_upload == "design4":
        design_name = "design4.html"

    if request.method == "POST":
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        school = request.form.get('school')
        college = request.form.get('college')
        phone = request.form.get('phone')
        email = request.form.get('email')
        about = request.form.get('about')
        skill1 = request.form.get('skill1')
        skill2 = request.form.get('skill2')
        skill3 = request.form.get('skill3')
        skill4 = request.form.get('skill4')
        skill5 = request.form.get('skill5')
        job = request.form.get('job')
        github = request.form.get('github')
        linkdeln = request.form.get('linkdeln')
        instagram = request.form.get('instagram')
        facebook = request.form.get('facebook')

        #Including Image
        img = request.files['pic']
        img.save(f"static\img\{img.filename}")
        key = uuid.uuid1()
        img_new_name = f"{key}{img.filename}"
        os.rename(f"static\img\{img.filename}", f"static\img\{img_new_name}")
    
    return render_template(design_name,
                           dname=firstName,
                           dlname=lastName,
                           dschool=school,
                           dcollege=college,
                           dphone=phone,
                           demail=email,
                           dsk1=skill1,
                           dsk2=skill2,
                           dsk3=skill3,
                           dsk4=skill4,
                           dsk5=skill5,
                           dgithub=github,
                           dinstagram=instagram,
                           dfacebook=facebook,
                           dlinkdeln=linkdeln,
                           dabout=about,
                           dp=img_new_name,
                           djob=job)

def delete(): 
    files = os.listdir("static/img/")
    for f in files:
        print(f)
        os.remove(f"static/img/{f}")

if __name__ == "__main__":
    schedule.every().day.at("23:59").do(delete)
    app.run(debug=True)
