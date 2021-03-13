import random;

from browser import *;

class Google (Browser):
	def __init__(self,socks5=None):
		super().__init__(socks5=socks5);
	def executeBusca(self, palavras):
		print("O senhor está pesquisando: ", palavras);
		paginas = ["https://www.google.com.br", "https://www.google.com", "https://www.google.com.ar", "https://www.google.com.vn", "https://www.google.com.pa",
		"https://www.google.co.uk/", "https://www.google.fr/", "https://www.google.ch/","https://www.google.de/", "https://www.google.pl/", "https://www.google.it/",
		"https://www.google.ie/webhp", "https://www.google.es/", "https://www.google.pt/", "https://www.google.at/", "https://www.google.com.au/webhp",
		"https://www.google.co.ma/", "https://www.google.cz/", "https://www.google.ca/webhp", "https://www.google.com.mx/", "https://www.google.com.co/",
		"https://www.google.com.ec/", "https://www.google.hn/", "https://www.google.no/", "https://www.google.se/", "https://www.google.nl/", "https://www.google.co.il/",
		"https://www.google.co.jp/" ];

		pagina = paginas[random.randint(0, len(paginas) - 1)];
		print("A página do google será: ", pagina);

		self.driver.get(pagina);
		input_q = self.driver.find_element_by_xpath("//input[@name='q']");
		input_q.send_keys(palavras);
		input_q.send_keys(Keys.RETURN);
		buffer_links = [];
		buffer_quadros = self.driver.find_elements_by_xpath("//div[@class='g' and div[1]/div[1]/a]");
		for i in range(len(buffer_quadros)):
			try:
				link = buffer_quadros[i].find_element_by_xpath("./div[1]/div[1]/a").get_attribute("href");
				buffer_links.append(link);
			except:
				print('vou ignorar falta de elemento dentro da div.');
		return buffer_links;
