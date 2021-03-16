import random;

from engine.browser import *;

class Bing (Browser):
	def __init__(self, socks5=None):
		super().__init__(socks5=socks5);

	def executeBusca(self, palavras):
		print("O senhor está pesquisando: ", palavras);
		paginas = ["https://www.bing.com", "https://www.bing.com/?cc=br"];
		pagina = paginas[random.randint(0, len(paginas) - 1)];
		print("Página do BING: ", pagina);
		self.driver.get(pagina);
		input_q = self.driver.find_element_by_xpath("//input[@name='q']");
		input_q.send_keys(palavras);
		input_q.send_keys(Keys.RETURN);
		buffer_quadros = self.driver.find_elements_by_xpath("//li[@class='b_algo' and div[1]/h2/a]");
		buffer_links = [];
		for i in range(len(buffer_quadros)):
			try:
				link = buffer_quadros[i].find_element_by_xpath("./div[1]/h2/a").get_attribute("href");
				buffer_links.append(link);
			except:
				print("vou ignorar");
		return buffer_links;
