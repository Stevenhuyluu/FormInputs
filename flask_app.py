
from flask import Flask, request, render_template
app = Flask(__name__)

#Vaidate name and address
#Tell them that their message has been recieved
#contact them after they have sent in credentials.
#return different messages based on what they check volunteer or recylcer














@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    address = request.form.ger('input_address','')
    dropdown = request.form.get('input_dropdown', '')
    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    if name =="":
        return render_template("main_page.html", input_data=dropdown,
                           output="where is your name")
    if address =="":
        return render_template("main_page.html", input_data=dropdown,
                           output="what is your address")
    return render_template("main_page.html", input_data=dropdown,
                           output="You're a wizard %s." % name)
