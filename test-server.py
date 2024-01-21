# Description: This file is used to test the server.py file. It is not used in the final product.
# Three endpoints are created to test the server.py file. The first endpoint is used to test the app.py 

from flask import Flask, request

import subprocess

app = Flask(__name__)

@app.route('/')
def init():
    return "Hello World!"

@app.route("/test", methods=["POST"])
def test():
    payload = request.json
    ref = payload.get('ref', '')

    # Check if the push is to the desired branch, e.g., 'refs/heads/testing'
    if ref == 'refs/heads/stage':
        # this hook is coming from a push done to the "testing" branch
        # run test.bash script to test the app.py file

        output = subprocess.run(["bash", "test.bash"])

        if output.returncode == 0:
            return "test passed"
        else:
            return {"return code: ": output.returncode, "output: ": output.stdout}
    
    else:
        return "not pushed to stage branch"

@app.route("/deployment", methods=["POST"])
def deployment():
    payload = request.json
    ref = payload.get('ref', '')

    # Check if the push is to the desired branch, e.g., 'refs/heads/testing'
    if ref == 'refs/heads/main':
        # this hook is coming from a push done to the "testing" branch
        # Add your code logic here

        command = ["bash", "deployment.bash"]
    
        output = subprocess.run(command, close_fds=True)

        if output.returncode == 0:
            return "deployment passed"
        else:
            return {"return code: ": output.returncode, "output: ": output.stdout}
    
    else:
        return "not pushed to main branch"


if __name__ == '__main__':
    app.run(debug=True, port=5001)