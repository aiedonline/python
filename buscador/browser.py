import random;

from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

class Browser:
	def __init__(self):
		chrome_otions = webdriver.ChromeOptions();
		agentes = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" ,
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		];
		agente = agentes[random.randint(0, len(agentes) - 1)];
		chrome_otions.add_argument("user-agent=" + agente);
		chrome_otions.add_argument("--headless");
		chrome_otions.add_argument("--no-sandbox");
		chrome_otions.add_argument("--mute-audio");
		self.driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_otions);
	def executeBusca(self, palavras):
		print("... Metodo nao implementado....");
	
	def __del__(self):
		self.driver.close();



