from flask import Flask, request, jsonify
import subprocess
import shlex

app = Flask(__name__)


@app.route('/ps', methods=['GET'])
def get_ps_output():
    args = request.args.getlist('arg')

    cmd = ['ps'] + args

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            return f"Error executing command: {result.stderr}", 500

        formatted_output = shlex.quote(result.stdout)

        return f"<pre>{formatted_output}</pre>"

    except Exception as e:
        return f"An error occurred: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)