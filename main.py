from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True


hello_form = """
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
         form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
      
      <form method="post">
      <label>Rotate by:
          <input type="text" name="rot" value="0"/>
      </label>
          <textarea name="text">{0}</textarea>

          <input type="submit" value="Submit"/>
          </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot_var=int(request.form["rot"])
    text_var=request.form["text"]

    x = rotate_string(text_var, rot_var)

    return hello_form.format(x)


    

@app.route("/")
def index():
    return hello_form.format(" ")

app.run()
