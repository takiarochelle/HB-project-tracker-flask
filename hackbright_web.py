"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)

@app.route("/student-add", methods=['POST', 'GET'])
def student_add():
	"""Add a student."""
	first_name = request.form.get('first')
	last_name = request.form.get('last')
	github = request.form.get('github')
	hackbright.make_new_student(first_name, last_name, github)
	return render_template("student_add.html")
	# return redirect("/student")
	
@app.route("/student-search")
def get_student_form():
	"""Show form for searching for a student."""
	return render_template("student_search.html")

@app.route("/student")
def get_student():
	"""Show information about a student."""
	github = request.args.get('github')

	first, last, github = hackbright.get_student_by_github(github)

	html = render_template("student_info.html",
						   first=first,
						   last=last,
						   github=github)

	return html
	# github = "jhacks"

	# first, last, github = hackbright.get_student_by_github(github)

	# return "{} is the GitHub account for {} {}".format(github, first, last)

if __name__ == "__main__":
	hackbright.connect_to_db(app)
	app.run(debug=True)
