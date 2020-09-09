from googlesearch import search, get_random_user_agent
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', dest='vuln', action='store', help='The vulnerability that you want to gather h1 reports', required=True)
parser.add_argument('-n', dest='numberOfReports', action='store', type=int, default=100, help='The number of how many reports you want to gather. DEFAULT: 100')
parser.add_argument('-p', dest='seconds', action='store', type=float, default=2.0, help='How much second/seconds do you want it to wait between HTTP Requests, I highly recommend to set this up so that we can avoid getting banned by google. DEFAULT: 2')
args = parser.parse_args()
numberOfReports = args.numberOfReports
vuln = args.vuln
seconds = args.seconds
user_agent = get_random_user_agent()
query = f"site:hackerone.com inurl:/reports/ intext:{vuln}"

def banner():
	print("""
  ____ ____  ___ _____ _   _ 
 / ___|  _ \|_ _|_   _| | | |
| |  _| |_) || |  | | | |_| |
| |_| |  _ < | |  | | |  _  |
 \____|_| \_\___| |_| |_| |_|
 	a tool created by 0xShin
		""")

def search_links(query):
	reports = []
	links = search(query, stop=numberOfReports, pause=seconds, user_agent=user_agent)
	print('[+] Currently gathering links [+]')
	for link in links:
		reports.append(link)
	return reports
def outputToFile(reports):
	f = open(f'{vuln}.txt', 'w')
	print(f'[+] Outputting the links into {vuln}.txt [+]')
	for report in reports:
		f.write(report + '\n')
	f.close()

banner()
outputToFile(search_links(query))