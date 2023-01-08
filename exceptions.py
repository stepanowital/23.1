from flask import Flask, jsonify, request


app = Flask(__name__)


class ApiError(Exception):
	pass


def division(a, b):
	try:
		a = int(a)
		b = int(b)
	except (ValueError, TypeError):
		raise ApiError('a or b are not integers')

	try:
		return a / b
	except ZeroDivisionError:
		raise ApiError('b is zero')


@app.route('/')
def main_page():
	a = request.args.get('a')
	b = request.args.get('b')

	try:
		res = division(a, b)
		return jsonify({"result": res})
	except ApiError as e:
		return jsonify({"Error": str(e)})


if __name__ == '__main__':
	app.run()
