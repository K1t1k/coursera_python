import json
import functools

def to_json(func):
	@functools.wraps(func)
	def wrapped(*args, **kwargs):
		return json.dumps(*args, **kwargs)
	return wrapped

#def main():
#	@to_json
#	def get_data():
#  		return {'data': 42}
#
#	a = get_data()
#	return a

#if __name__ == '__main__':
#	main()