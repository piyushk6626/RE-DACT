from flask import Flask, render_template, request
app = Flask(_name_)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def form():


    if request.form.get('text'):
        text = request.form['text']

    result = {"Personal_Identifiers_Remover":0, "Health_Information_Remover":0, "Financial_Information_Remover":0, "Health_Information_Remover":0,"Employment_Information_Remover":0, "Online_Account_Information_Remover":0,"Demographic_Information_Remover":0 }

    if request.form.get('Personal_Identifiers_Remover'):
        result["Personal_Identifiers_Remover"] = request.form['Personal_Identifiers_Remover']

    if request.form.get('Financial_Information_Remover'):
        result["Financial_Information_Remover"] = request.form['Financial_Information_Remover']

    if request.form.get('Health_Information_Remover'):
        result["Health_Information_Remover"] = request.form['Health_Information_Remover']
    
    if request.form.get('Employment_Information_Remover'):
        result["Employment_Information_Remover"] = request.form['Employment_Information_Remover']

    if request.form.get('Online_Account_Information_Remover'):
        result["Online_Account_Information_Remover"] = request.form['Online_Account_Information_Remover']

    if request.form.get('Demographic_Information_Remover'):
        result["Demographic_Information_Remover"] = request.form['Demographic_Information_Remover']

    print(result)
    print(text)
    

    return index()



if _name_ == '_main_':
    app.run(host='127.0.0.1', port=8000, debug=True)