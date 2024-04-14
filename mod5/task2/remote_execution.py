import subprocess

from flask import Flask
from subprocess import TimeoutExpired

from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(validators=[InputRequired(), NumberRange(min=1, max=30)])

def run_python_code_in_subprocess(code: str, timeout: int):
    command = ['python', '-c', code]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        outs, errs = proc.communicate(timeout=timeout)
        return outs
    except TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()
        return "исполнение кода не уложилось в данное время"



@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        code = form.code.data
        timeout = form.timeout.data
        return run_python_code_in_subprocess(code, timeout)

    return "Ошибка ввода"

if __name__ == '__main__':
    app.run(debug=True)
