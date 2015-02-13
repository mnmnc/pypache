import socket

class Translator:

	previous_ip = ""
	previous_host = ""

	def ip_to_hostname(self, ip):

		if self.previous_ip == ip:
			return self.previous_host
		else:
			try:
				new_host = socket.gethostbyaddr(ip)
				self.previous_ip = ip
				self.previous_host = new_host[0]
				return new_host[0]
			except Exception:
				new_host = ip
				self.previous_ip = ip
				self.previous_host = ip
				return new_host

	def get_agent(self, agent_string):
		if "Firefox/" in agent_string:
			return ("Firefox", agent_string[agent_string.find("Firefox/")+8:agent_string.find("Firefox/")+10])
		elif "MSIE" in agent_string:
			return ("IE", agent_string[agent_string.find("MSIE")+5:agent_string.find("Firefox/")+7])
		elif "Seamonkey/" in agent_string:
			return ("Seamonkey", agent_string[agent_string.find("Seamonkey/")+10:agent_string.find("Seamonkey/")+12])
		elif "Chrome/" in agent_string and "Chromium" not in agent_string:
			return ("Chrome", agent_string[agent_string.find("Chrome/")+7:agent_string.find("Chrome/")+9])
		elif "Chromium/" in agent_string:
			return ("Chromium", agent_string[agent_string.find("Chromium/")+9:agent_string.find("Chromium/")+11])
		elif "Safari/" in agent_string and "Chrome" not in agent_string and "Chromium" not in agent_string:
			return ("Safari", agent_string[agent_string.find("Safari/")+7:agent_string.find("Safari/")+9])
		elif "OPR/" in agent_string or "Opera/" in agent_string:
			return ("Opera", 0)
		else:
			return agent_string