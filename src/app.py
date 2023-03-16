from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
import pyautogui
import subprocess
import time

app = Flask(__name__)
CORS(app)

# just a test to see if react and flask are connected
@app.route("/")
def test():
    return make_response(render_template('test.html'))

#  this function activates the SITL drone
@app.route("/command")
def command():
    # this opens a new ubuntu terminal
    subprocess.call(['gnome-terminal'])
    pyautogui.hotkey('win', 'r')
    time.sleep(4)
    # pyautogui.typewrite('ubuntu')
    # pyautogui.press('enter')
    # once a new ubuntu termina is open, it runs the code for the SITL drone
    result = subprocess.run('cd ../../dk/ ; python connection_template.py' , capture_output=True, shell=True)
    output = result.stdout.decode()
    print(output)
    return make_response(jsonify({'the output is:': output}))



if __name__ == '__main__':
    app.run(port = 5560, debug = True)