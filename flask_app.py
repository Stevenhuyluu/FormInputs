
from flask import Flask, request, render_template
app = Flask(__name__)

#Vaidate name and address
#Tell them that their message has been recieved
#contact them after they have sent in credentials.
#return different messages based on what they check volunteer or recylcer
#if they pick volunteer return drop down.














@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    address = request.form.get('input_address','')
    choice = request.form.get('role', '')
    days = request.form.get('day', '')
    questions = request.form.get('input_freeform', '')
    email = request.form.get('input_email', '')
    if name =="":
        return render_template("main_page.html",
                           output="where is your name")
    if address =="":
        return render_template("main_page.html",
                           output="what is your address")
    if choice =="":
        return render_template("main_page.html",
                           output="what are you signing up to be?")
    if choice =="Recycle":
        return render_template("main_page.html", name=name, address=address, recycle=True)
    if choice =="Volunteer":
        return render_template("main_page.html", name=name, email=email, volunteer=True)
    else:
        return render_template("main_page.html", output = choice)