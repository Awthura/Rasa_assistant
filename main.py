import subprocess, threading

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	def run_subprocess(command):
		subprocess.run(command, shell=True)

	cmd1, cmd2 = "rasa run --cors '*' --enable-api", "rasa run actions"

	t1 = threading.Thread(target=run_subprocess, args=(cmd1,))
	t2 = threading.Thread(target=run_subprocess, args=(cmd2,))
	t1.start()
	t2.start()

	app.run(host='0.0.0.0', port=5000)