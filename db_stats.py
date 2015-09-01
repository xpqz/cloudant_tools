import requests
import json

account = '' # FILL ME IN
auth = ''  # FILL ME IN:  use the form 'Basic LWRxLXJ0YW5tEWxsYXkBVlVfY2xhc3MxMQ=='
url = 'https://{0}.cloudant.com/'.format(account)

def main():
	dbs = requests.get(url + '_all_dbs', headers={'Authorization': auth}).json()
	
	output = []
	for db in dbs:
		print 'Retrieving stats for {0}...'.format(db)
		stats = requests.get(url + db, headers={'Authorization': auth}).json()
		output.append(stats['doc_count'])

	print json.dumps(output, indent=4)
	print json.dumps(sorted(output), indent=4)

if __name__ == "__main__":
	main()