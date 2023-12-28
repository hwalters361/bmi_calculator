from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(height, weight, system):
    if system == 'metric':
        bmi = weight / ((height / 100) ** 2)  # BMI formula for metric units (height in meters)
    else:
        bmi = (weight / (height ** 2)) * 703  # BMI formula for imperial units (height in inches)
    return round(bmi, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi_result = None
    height = None
    weight = None
    system='metric'
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        system = request.form['system']
        bmi_result = calculate_bmi(height, weight, system)
 
    return render_template('index.html', bmi_result=bmi_result, input_height=height, input_weight=weight, system=system)

if __name__ == '__main__':
    app.run(debug=True)
