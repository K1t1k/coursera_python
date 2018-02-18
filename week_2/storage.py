
import json, os, tempfile, sys
from argparse import ArgumentParser
from collections import OrderedDict

def write_json(data, path):
	with open(path, 'w') as f:
		json.dump(data, f)

def main():
	storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
	parser = ArgumentParser()
	parser.add_argument("--key")
	parser.add_argument("--value")
	args = parser.parse_args()

	if os.path.exists(storage_path):
		with open(storage_path) as f:
			data = f.read()
		if data:
			with open(storage_path) as f:
				json_data = json.load(f)
			if args.key and args.value:
				if args.key in json_data:
					json_data[args.key] = json_data[args.key] + ', ' + args.value
					write_json(json_data, storage_path)
					print(json_data[args.key])
					return json_data[args.key]
				else:
					json_data[args.key] = args.value
					write_json(json_data, storage_path)
					print(json_data[args.key])
					return json_data[args.key]
			elif args.key and not args.value:
				if args.key in json_data:
					print(json_data[args.key])
					return json_data[args.key]
				else:
					print(None)
					return None
			else:
				print(None)
				return None
		else:
			json_data = dict()
			if args.key and args.value:
				json_data[args.key] = args.value
				write_json(json_data, storage_path)
				print(json_data[args.key])
				return json_data[args.key]
			else:
				print(None)
				return None
	else:
		with open(storage_path, 'w') as f:
			f.write("")
		return None
	return 0

if __name__=="__main__":
	main()
