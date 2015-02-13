
from tools import transformer
from tools import translator
import os


class PyPache:

	data = []
	translator = translator.Translator()
	transformer = transformer.Transformer()

	def __init__(self, log_path):
		with open(log_path, 'rt') as log_file:
			self.log = log_file.read()

	def load_log(self):
		for line in self.log.split("\n"):
			if len(line) > 1:
				line_list = line.split("|")

				temp_list = (line_list[0]).split(" ")
				referrer = line_list[1]
				user_agent = line_list[2]

				ip = temp_list[0]
				host = self.translator.ip_to_hostname(ip)
				user = temp_list[2]
				date = temp_list[3] + " " + temp_list[4]
				method = temp_list[5]
				file = temp_list[6]
				protocol = temp_list[7]
				code = temp_list[8]
				size = temp_list[9]

				self.data.append({
					"ip": ip,
					"hostname": host,
					"user": user,
				    "date": date,
				    "method": method,
				    "file": file,
				    "protocol": protocol,
				    "code": code,
				    "size": size
				})

		for ele in self.data:
			print(ele)


		# splitted = line.split("\"")
		#
		# first = splitted[0].split(" ")
		# ip = first[0]
		# user = first[2]
		# date = first[3] + first[4]
		#
		# request = splitted[1]
		# resp_code = splitted[2]
		# ref = splitted[3]
		# agent = get_agent(splitted[5])


# 18.1.4.0 - r [13/Feb/2015:12:00:17 +0100] POST /rt/rutorrent/plugins/history/action.php HTTP/1.1 200 308 | https://.duckdns.org/rt/rutorrent/ | Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0
# 18.1.4.0 - r [13/Feb/2015:12:00:17 +0100] GET /rt/rutorrent/plugins/cpuload/action.php?_= HTTP/1.1 200 297 | https://.duckdns.org/rt/rutorrent/ | Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0
# 18.1.4.0 - r [13/Feb/2015:12:00:17 +0100] GET /rt/rutorrent/plugins/tracklabels/action.php?tracker=.net HTTP/1.1 304 130 | https://.duckdns.org/rt/rutorrent/ | Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0
# 18.1.4.0 - r [13/Feb/2015:12:00:16 +0100] POST /rt/rutorrent/plugins/check_port/action.php HTTP/1.1 200 314 | https://.duckdns.org/rt/rutorrent/ | Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0
# 18.1.4.0 - r [13/Feb/2015:12:00:17 +0100] GET /rt/rutorrent/plugins/tracklabels/action.php?tracker= HTTP/1.1 304 130 | https://.duckdns.org/rt/rutorrent/ | Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0
# 18.1.4.0 - r [13/Feb/2015:12:00:17 +0100] POST /rt/rutorrent/plugins/rss/action.php HTTP/1.1 200 319 | https://.duckdns.org/rt/rutorrent/ | Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0

def main():

	log_path = "apache.log"

	pypache = PyPache(log_path)
	pypache.load_log()

	print(os.get_terminal_size())

if __name__ == "__main__":

	main()
