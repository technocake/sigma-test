from flask import Flask, request, render_template, redirect, url_for, g
import time
import os
import Queue
app = Flask(__name__)

current_response = None

rq = Queue.Queue()
qq = Queue.Queue()

@app.route("/")
def home():
	return render_template("home.html")


@app.route("/search")
def search():
	global rq, qq
	q = request.args.get("q", None)
	if q:
		#with open('query.txt', 'w') as queryfile:
		#	queryfile.write(q)
		#	queryfile.close()

		qq.put(q)

		# Now lets wait for the response...
		for i in range(10):
			time.sleep(0.5)
			try:
				r = rq.get_nowait()
				rq.task_done()
				if r and r == "None":
					return redirect(url_for('sorry_mate'))
				else:
					return r
			except Queue.Empty:
				pass
			except Exception as e:
				return redirect(url_for('sorry_mate'))
			

	return render_template("search.html", q=q)


@app.route("/status-quo")
def status_quo():
	global qq
	try:
		#with open("query.txt", "r") as queryfile:
		#	q = queryfile.read()
		q = qq.get_nowait()
		qq.task_done()
		return q
	except:
		return ""

@app.route("/respond/<response>")
def respond(response):
	""" For controller. """
	#with open("response.txt", "w") as responsefile:
	#	responsefile.write(response)
	global rq
	rq.put(response)
	return response



@app.route("/sorry-mate")
def sorry_mate():
	return render_template("sorry-mate.html")


@app.route("/controller")
def controller():
	map_index = ['User Input.mm']
	return render_template("controller.html", map_index=map_index)


if __name__ == '__main__':
	import webbrowser
	webbrowser.open("http://localhost:5000")
	app.run(debug=True)
