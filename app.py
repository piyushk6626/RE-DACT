from flask import Flask, render_template, request
from LocalLLM import Sensitive_Personal_Information_Remover

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST','GET'])
def form():
    result = {
        "Personal_Identifiers_Remover": 0, 
        "Health_Information_Remover": 0, 
        "Financial_Information_Remover": 0, 
        "Employment_Information_Remover": 0, 
        "Online_Account_Information_Remover": 0,
        "Demographic_Information_Remover": 0
    }

    text = ""
    
    if request.form.get('text'):
        text = request.form['text']

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
    
    # Call the Sensitive_Personal_Information_Remover with the corrected parameters
    output = Sensitive_Personal_Information_Remover(
        Text=text,
        Personal_Identity_status=bool(result["Personal_Identifiers_Remover"]),
        Financial_Information_status=bool(result["Financial_Information_Remover"]),
        Health_Information_status=bool(result["Health_Information_Remover"]),
        Employment_Information_status=bool(result["Employment_Information_Remover"]),
        Online_Account_Information_status=bool(result["Online_Account_Information_Remover"]),
        Demographic_Information_status=bool(result["Demographic_Information_Remover"])
    )

    return render_template('index.html', output=output)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
