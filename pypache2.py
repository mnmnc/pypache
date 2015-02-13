
from tools import transformer
from tools import translator
import os
import argparse


class PyPache:

	data = []
	translator = translator.Translator()
	transformer = transformer.Transformer()
	limits = {}

	def __init__(self, log_path):
		try:
			with open(log_path, 'rt') as log_file:
				self.log = log_file.read()
		except:
			print("File not found.")
			os._exit(1)

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
				date = temp_list[3][1:7] + " " + temp_list[3][13:21]
				method = temp_list[5]
				file = temp_list[6]
				protocol = temp_list[7]
				code = temp_list[8]
				size = temp_list[9]


				self.data.append({
					"ip": ip.strip(),
					"hostname": host.strip(),
					"user": user.strip(),
				    "date": date.strip(),
				    "method": method.strip(),
				    "file": file.strip(),
				    "protocol": protocol.strip(),
				    "code": code.strip(),
				    "size": size.strip(),
				    'referrer': referrer.strip(),
				    'agent': (self.translator.get_agent(user_agent))

				})


	def set_limits(self, term_size):

		minimal = {
			'protocol': 3,
		    'method': 1,
		    'file': 10,
		    'user': 3,
		    'hostname': 10,
		    'agent': 4,
		    'referrer': 10
		}

			#- print(t_date, end=' ')
			#- print(t_code, end=' ')
			#+ print(t_method, end=' ')
			#+ print(t_protocol, end=' ')
			#+ print(t_user, end=' ')
			#+ print(t_agent, end=' ')
			#- print(t_ip, end=' ')
			# print(t_hostname, end=' ')
			# print(t_referrer, end=' ')
			# print(t_file, end=' ')
			# print()

		left = term_size - 16 - 4 - 16 - 6 - 8 - 6 - 11
		#                 date code ip  meth pro use agent

		maximal = {
			'protocol': 8,
		    'method': 6,
		    'file': int(left/3) -1,
		    'user': 5,
		    'hostname': int(left/4) -1,
		    'agent': 10,
		    'referrer': int(left/3) -1
		}

		self.limits.update({
			'minimal': minimal,
		    'maximal': maximal
		})

	def minimal(self):

		for ele in self.data:
			t_ip = self.transformer.adjust_item( ele['ip'], 15)[:15]

			t_hostname = self.transformer.adjust_item(  ele['hostname'],
														self.limits['minimal']['hostname']
													)[:self.limits['minimal']['hostname']]

			t_protocol = (ele['protocol']).split("/")[1]

			t_method = ele['method'][0]

			t_referrer = self.transformer.adjust_item(  ((ele['referrer']).split("/"))[2],
														self.limits['minimal']['referrer']
													)[:self.limits['minimal']['referrer']]

			t_agent = self.transformer.adjust_item(  ele['agent'][0],
														self.limits['minimal']['agent']
													)[:self.limits['minimal']['agent']]

			t_user = self.transformer.adjust_item(  ele['user'],
														self.limits['minimal']['user']
													)[:self.limits['minimal']['user']]

			t_file = self.transformer.adjust_item(  ele['file'],
														self.limits['minimal']['file']
													)[-self.limits['minimal']['file']:]

			t_code = ele['code']
			t_date = ele['date']
			t_size = self.transformer.adjust_item(ele['size'], 6)

			print(t_date, end=' ')
			print(t_code, end=' ')
			#print(t_size, end=' ')
			print(t_method, end=' ')
			#print(t_protocol, end=' ')
			#print(t_user, end=' ')
			print(t_agent, end=' ')
			print(ele['agent'][1], end=' ')
			print(t_ip, end=' ')
			print(t_hostname, end=' ')
			print(t_referrer, end=' ')
			print(t_file, end=' ')
			print()


	def maximal(self):
		for ele in self.data:
			t_ip = self.transformer.adjust_item( ele['ip'], 15)[:15]

			t_hostname = self.transformer.adjust_item(  ele['hostname'],
														self.limits['maximal']['hostname']
													)[:self.limits['maximal']['hostname']]

			t_protocol = ele['protocol']

			t_referrer = self.transformer.adjust_item(  ((ele['referrer']).split("/"))[2],
														self.limits['maximal']['referrer']
													)[:self.limits['maximal']['referrer']]

			t_agent = self.transformer.adjust_item(  ele['agent'][0] +' ' + ele['agent'][1],
														self.limits['maximal']['agent'] + 3
													)[:self.limits['maximal']['agent'] + 3]

			t_user = self.transformer.adjust_item(  ele['user'],
														self.limits['maximal']['user']
													)[:self.limits['maximal']['user']]

			t_method = self.transformer.adjust_item(  ele['method'],
														self.limits['maximal']['method']
													)[:self.limits['maximal']['method']]

			t_file = self.transformer.adjust_item(  ele['file'],
														self.limits['maximal']['file']
													)[-self.limits['maximal']['file']:]

			t_code = ele['code']
			t_date = ele['date']

			print(t_date, end=' ')
			print(t_code, end=' ')
			print(t_method, end=' ')
			print(t_protocol, end=' ')
			print(t_user, end=' ')
			print(t_agent, end=' ')
			print(t_ip, end=' ')
			print(t_hostname, end=' ')
			print(t_referrer, end=' ')
			print(t_file, end=' ')
			print()

	def create_list(self, size):
		result = []
		for i in range(size):
			result.append(' ')
		return result

	def string_to_string_list(self, s, length):
		first = s[0:length]
		second = s[length:length+length]
		third = s[length+length:length+length+length]

		return [first, second, third]

	def multiline(self, term_size):

		for ele in self.data:

			final_lines = [
				self.create_list(term_size-1),
			    self.create_list(term_size-1),
			    self.create_list(term_size-1)
			]

			current_line = 0
			current_offset = 0

			# DATE
			final_lines[current_line][current_offset:current_offset+len(ele['date'])] = ele['date']
			current_offset += len(ele['date']) + 1

			# CODE
			final_lines[current_line][current_offset:current_offset+len(ele['code'])] = ele['code']
			current_offset += len(ele['code']) + 1

			# USER
			t_user = self.transformer.adjust_item(  ele['user'],
														self.limits['maximal']['user']
													)[:self.limits['maximal']['user']]
			final_lines[current_line][current_offset:current_offset+len(t_user)] = t_user
			current_offset += len(t_user) + 1

			# METHOD
			t_method = self.transformer.adjust_item(  ele['method'],
														self.limits['maximal']['method']
													)[:self.limits['maximal']['method']]
			final_lines[current_line][current_offset:current_offset+len(t_method)] = t_method
			current_offset += len(t_method) + 1

			# PROTOCOL
			t_protocol = self.transformer.adjust_item(  ele['protocol'],
														self.limits['maximal']['protocol']
													)[:self.limits['maximal']['protocol']]
			final_lines[current_line][current_offset:current_offset+len(t_protocol)] = t_protocol
			current_offset += len(t_protocol) + 1

			# AGENT
			if len(ele['agent'][0]) > self.limits["maximal"]['agent']:
				divided = self.string_to_string_list(ele['agent'][0], self.limits["maximal"]['agent'])
				if len(divided[0]) > 0:
					final_lines[0][current_offset:current_offset+len(divided[0])] = divided[0]
				if len(divided[1]) > 0:
					final_lines[1][current_offset:current_offset+len(divided[1])] = divided[1]
				if len(divided[2]) > 0:
					final_lines[2][current_offset:current_offset+len(divided[2])] = divided[2]
			else:
				final_lines[0][current_offset:current_offset+self.limits["maximal"]['agent'] + 3] = self.transformer.adjust_item(ele['agent'][0] +' '+ ele['agent'][1], self.limits["maximal"]['agent']+3)

			current_offset += self.limits["maximal"]['agent'] + 1

			# IP
			t_ip = self.transformer.adjust_item( ele['ip'], 15)[:15]
			final_lines[current_line][current_offset:current_offset+len(t_ip)] = t_ip
			current_offset += len(t_ip) + 1

			# HOSTNAME
			if len(ele['hostname']) > self.limits["maximal"]['hostname']:
				divided = self.string_to_string_list(ele['hostname'], self.limits["maximal"]['hostname'])
				if len(divided[0]) > 0:
					final_lines[0][current_offset:current_offset+len(divided[0])] = divided[0]
				if len(divided[1]) > 0:
					final_lines[1][current_offset:current_offset+len(divided[1])] = divided[1]
				if len(divided[2]) > 0:
					final_lines[2][current_offset:current_offset+len(divided[2])] = divided[2]
			else:
				final_lines[0][current_offset:current_offset+self.limits["maximal"]['hostname']] = self.transformer.adjust_item(ele['hostname'], self.limits["maximal"]['hostname'])

			current_offset += self.limits["maximal"]['hostname'] + 1


			# FILE
			if len(ele['file']) > self.limits["maximal"]['file']:
				divided = self.string_to_string_list(ele['file'], self.limits["maximal"]['file'])
				if len(divided[0]) > 0:
					final_lines[0][current_offset:current_offset+len(divided[0])] = divided[0]
				if len(divided[1]) > 0:
					final_lines[1][current_offset:current_offset+len(divided[1])] = divided[1]
				if len(divided[2]) > 0:
					final_lines[2][current_offset:current_offset+len(divided[2])] = divided[2]
			else:
				final_lines[0][current_offset:current_offset+self.limits["maximal"]['file']] = self.transformer.adjust_item(ele['file'], self.limits["maximal"]['file'])

			current_offset += self.limits["maximal"]['file'] + 1

			# REFERRER
			if len(ele['referrer']) > self.limits["maximal"]['referrer']:
				divided = self.string_to_string_list(ele['referrer'], self.limits["maximal"]['referrer'])
				if len(divided[0]) > 0:
					final_lines[0][current_offset:current_offset+len(divided[0])] = divided[0]
				if len(divided[1]) > 0:
					final_lines[1][current_offset:current_offset+len(divided[1])] = divided[1]
				if len(divided[2]) > 0:
					final_lines[2][current_offset:current_offset+len(divided[2])] = divided[2]
			else:
				final_lines[0][current_offset:current_offset+self.limits["maximal"]['referrer']] = self.transformer.adjust_item(ele['referrer'], self.limits["maximal"]['referrer'])

			current_offset += self.limits["maximal"]['referrer'] + 1


			for line in final_lines:
				if line.count(' ') < term_size-1:
					for letter in line:
						print(letter, end='')
					print()

def nparse():
	"""Parses arguments"""
	usage = " pypache.py [-s | --small | -w | --wide | -m | --multiline ]"
	parser = argparse.ArgumentParser(description=usage)
	parser.add_argument('-s', "--small", action='store_true', default=True, help='Show smalles output possible.')
	parser.add_argument('-w', "--wide", action='store_true', default=False, help='Show wide output.')
	parser.add_argument('-m', "--multiline", action='store_true', default=False, help='Show multiline output. Longer values like referrer are divided into lines.')
	parser.add_argument('-p', "--path", metavar='additional_paths', default=[None], nargs='*', help='Change the log path.')
	args = parser.parse_args()
	return args

def main():

	global args
	args = nparse()

	log_path = "apache.log"
	if args.path[0] is not None:
		log_path = args.path[0]

	pypache = PyPache(log_path)
	pypache.load_log()
	pypache.set_limits(os.get_terminal_size()[0])


	if args.wide:
		pypache.maximal()
	elif args.multiline:
		pypache.multiline(os.get_terminal_size()[0])
	else:
		pypache.minimal()

	#print(os.get_terminal_size()[0])


if __name__ == "__main__":

	main()
