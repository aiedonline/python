import time;

from browser import *;

class Tor (Browser):
	def __init__(self, socks5=None):
		super().__init__(socks5=socks5);
	def teste(self):
		self.driver.get("https://check.torproject.org/");
		time.sleep(20);
