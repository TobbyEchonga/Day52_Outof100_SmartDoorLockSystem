from flask import Flask, render_template, request, redirect, url_for
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# GPIO setup
GPIO.setmode(GPIO.BCM)
lock_pin = 18
GPIO.setup(lock_pin, GPIO.OUT)

def unlock_door():
    GPIO.output(lock_pin, GPIO.HIGH)
    time.sleep(5)  # Keep the door unlocked for 5 seconds
    GPIO.output(lock_pin, GPIO.LOW)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unlock', methods=['POST'])
def unlock():
    # In a real-world scenario, you would perform user authentication here
    # For simplicity, let's assume any request to /unlock is valid
    unlock_door()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
