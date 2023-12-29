To create a Flask app to calculate BMI, you must follow the following steps:

### Set up a Python virtual environment

In this step, you need to create the project folder and virtual environment.
Create a folder for your Flask app.

```bash
mkdir bmi_flask_app
```

Then ensure that `virtualenv` is installed. If not, install it with the following command.

```bash
pip install virtualenv
```

Create and activate a virtual python environment.

```bash
python3 -m venv myenv
source myenv/bin/activate
```

If you are using Git for this project, ignore your newly created `myenv` directory in your `.gitignore` file.
Next install Python packages and isolate the project code away from the main Python system installation. Install Flask into your virtual environment with the following command:

```bash
pip install flask
```

Once Flask finishes installing, confirm the installation by running this command:

```bash
python -c "import flask; import importlib; print(importlib.metadata.version('flask'))"
```

The output of this command should be a version number. With this, our programming environment is set up.

### Creating a Your Flask Backend

In this step you create the Python file that houses the logic for the web app.

Create a blank Python file called `bmi_calculator.py` in the base directory for your Flask app. Open it up and paste in the following code:

```python
from flask import Flask, render_template, request

# Initialize Flask application
app = Flask(__name__)

def calculate_bmi(height, weight, system):
    # Calculates the BMI based on the given height, weight, and system (metric or imperial)
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
```

*   This code initializes a Flask application.
*   It creates a function called `calculate_bmi` which takes in the inputs `height`, `weight`, and `system` and calculates BMI based on these provided values.
*   Next, it defines a route for the root URL `'/'`. The function `index()` handles both GET and POST requests.
    *   Inside the function it initializes the variables `bmi_result`, `height`, `weight`, and `system` from the form submission, calculates the BMI using the `calculate_bmi()` function, and stores the result in `bmi_result`.
    *   Finally, it renders the HTML, passing the BMI result (`bmi_result`), input height (`input_height`), input weight (`input_weight`) and the selected measurement system (`system) to be displayed in the template `index.html\`.

### Creating a Your Flask Frontend

In this step you create the HTML file that acts as the user interface, which for us is called `index.html`.
Create a folder called "templates" in the base directory of your project.

```bash
mkdir templates
```

Inside your templates directory, add an html file called index.html. Copy and paste in the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>BMI Calculator</title>
</head>
<body>
    <h1>BMI Calculator</h1>
    <p>Input height in inches (not feet) if selecting imperial units</p>
    <p>Input height in centimeters (not meters) if selecting metric units</p>
    <form method="post">
        
        <label for="height">Height:</label>
        <input type="number" step="any" name="height" id="height" placeholder="Enter height" required><br><br>

        <label for="weight">Weight:</label>
        <input type="number" step="any" name="weight" id="weight" placeholder="Enter weight" required><br><br>

        <label for="system">Measurement System:</label>
        <select name="system" id="system">
            <option value="metric">Metric (cm, kg)</option>
            <option value="imperial">Imperial (inches, lbs)</option>
        </select><br><br>

        <button type="submit">Calculate BMI</button>
    </form>

    {% if (bmi_result) %}
    <h2>For a height of {{ input_height }} {% if system == 'imperial' %}inches{% else %}centimeters{% endif %} and weight of {{ input_weight }} {% if system == 'metric' %}kilograms{% else %}pounds{% endif %} your BMI is: {{ bmi_result }}</h2>
    {% endif %}
</body>
</html>
```

*   This code is a basic web page for your BMI calculator.
*   It adds a header with the `<h1>` tag to display "BMI Calculator" at the top of the page.
*   It creates a form that uses the HTTP POST method to submit data. Inside the form there are input fields for:
    *   Height: With the type number that requires a numerical value.
    *   Weight: Also requires a numerical value
    *   Measurement System: A dropdown `select` field that allows user to pick between metric or imperial measurements. It has a default value of `'metric'`
*   There is a button that triggers the submission of the form data for BMI calculation.
*   Then there is a section to display the BMI results. It uses a Jinja templating syntax (`{%...%}`) to conditionally display the BMI result.
    *   If `bmi_result` has a value and is not `None` it shows the calculated BMI. It also displays the user's inputted height and weight along with the measurement system selected.

### Deploy the debug version of your Flask web app.

Lastly, run the application using the `flask run` command

```bash
flask --app bmi_calculator run
```

This last command should output the following:

```text
Output
 * Serving Flask app "hello" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 813-894-335
```

You can check to see your flask app running by following the URL that comes after "Running on". Verify that the webpage displays the HTML form. Note that this Flask development server should not be used in a production deployment.
Note that height can only be inputted in centimeters in metric mode and not meters, and inches in imperial mode and not feet.
