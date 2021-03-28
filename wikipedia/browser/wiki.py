#### PASSO 1 - ACHAR LINKS
#1 - Navegar para: https://pt.wikipedia.org/w/index.php?title=Especial:Pesquisar
#2 - Input em: //input[@name="search"]
#3 - Pegar as URLS: //ul[@class="mw-search-results"]/li/div[1]/a 

#### PASSO 2 - Extrair texto
#1 - Navegar par a página
#2 - Achar o: //div[@id="mw-content-text"]
#	2.1 - extrair todos os //p
#	2.2 - extrair links com /wiki/: 
import time;

from browser.browser import *;

class Wiki (Browser):
	def __init__(self, socks5 = None):
		super().__init__(socks5=socks5);

	def extrair_pagina(self, href):
		self.driver.get(href);
		retornar = {"texto" : "", "links" : []};
		conteudo = self.driver.find_element_by_xpath('//div[@id="mw-content-text"]');
		paragrafos = conteudo.find_elements_by_xpath('//p');
		links = conteudo.find_elements_by_xpath("//a[contains(@href, '/wiki/')]");
		for i in range(len(paragrafos)):
			retornar["texto"] = retornar["texto"] + paragrafos[i].text + " ";
		for i in range(len(links)):
			retornar["links"].append({"text" : links[i].text, "href" : links[i].get_attribute("href")});
		return retornar;


	def extrair(self, termo, max_pages = 3):
		self.driver.get("https://pt.wikipedia.org/w/index.php?title=Especial:Pesquisar");
		input_b = self.driver.find_element_by_xpath("//div[@id='searchText' and  input[@name='search']]/input");
		input_b.send_keys(termo);
		input_b.send_keys(Keys.RETURN);
		time.sleep(1);
		resultados = self.driver.find_elements_by_xpath('//ul[@class="mw-search-results"]/li/div[1]/a');
		links_a_consultar = [];
		retornar = [];
		for i in range(len(resultados)):
			links_a_consultar.append(resultados[i].get_attribute("href"));
			if i == max_pages:
				break;
		for i in range(len(links_a_consultar)):
			retornar.append(self.extrair_pagina(links_a_consultar[i]));
		return retornar;


