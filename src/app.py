from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
import pyautogui
import subprocess
from subprocess import Popen, PIPE
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
    # subprocess.call(['gnome-terminal'])
    # time.sleep(3)
    run_drone = ['cd ../../dk ; python connection_template.py']
    p = Popen(run_drone, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = p.communicate()
    print(stdout)
    print(stderr)
    print(p.returncode)

    # pyautogui.hotkey('win', 'r')
    # pyautogui.typewrite('ubuntu')
    # pyautogui.press('enter')


    # once a new ubuntu termina is open, it runs the code for the SITL drone
    # result = subprocess.run('cd ../../dk/ ; python connection_template.py' , capture_output=True, shell=True)
    # output = result.stdout.decode()
    # print(output)
    return make_response(jsonify({'the output is:': 'output'}))



if __name__ == '__main__':
    app.run(port = 5560, debug = True)