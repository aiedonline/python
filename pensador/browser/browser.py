import random, os, inspect, time;
import subprocess;
import sys;

from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())));

class Browser:
	def __init__(self, socks5=None, terminal=True, chromedriver=None, path_directory_browser=None):
		chrome_otions = webdriver.ChromeOptions();
		if socks5 != None:
			chrome_otions.add_argument("--proxy-server=socks5://127.0.0.1:" + socks5);

		agentes = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" ,
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		];

		agente = agentes[random.randint(0, len(agentes) - 1)];
		chrome_otions.add_argument("user-agent=" + agente);
		
		if terminal:
			chrome_otions.add_argument("--headless");
			chrome_otions.add_argument("--no-sandbox");
			chrome_otions.add_argument("--mute-audio");
				
		if chromedriver == None:
			chromedriver = CURRENTDIR + "/tmp/chromedriver";

		if path_directory_browser != None:
			if os.path.exists(path_directory_browser) == False:
				os.makedirs(path_directory_browser); 
			chrome_otions.add_argument("--profile-directory=Default")
			chrome_otions.add_argument('--user-data-dir=' + path_directory_browser);

		print("Chromedriver PATH: ", chromedriver);
		self.driver = webdriver.Chrome(chromedriver, chrome_options=chrome_otions);
		self.historico = {"urls" : []};
		self.eventos = [];

	def alertLeave(self):
		self.driver.Keyboard.PressKey(Keys.Space);
	def clicar(self, xpath, numero=1, wait=0):
		elementos = self.elementos(xpath, wait);
		if elementos != None:
			for i in range(numero):
				try:
					elementos[i].click();
				except Exception as e:
					self.driver.execute_script("arguments[0].click();", elementos[i]);
		else:
			return False;
		return True;

	def elemento(self, xpath, wait=0):
		for i in range(wait + 1):
			buffer = self.driver.find_element_by_xpath(xpath);
			if buffer != None or wait == 0:
				return buffer;
			time.sleep(1);
		return None;

	def elementos(self, xpath, wait=0):
		for i in range(wait + 1):
			buffer = self.driver.find_elements_by_xpath(xpath);
			if len(buffer) > 0 or wait == 0:
				return buffer;
			time.sleep(1);
		return None;
	
	def enter(self, xpath, wait=0, enter=False):
		elemento = self.elemento(xpath, wait);
		if elemento == None:
			return False;
		else:
			elemento.send_keys(Keys.ENTER);
			return True;

	def escrever(self, xpath, texto, wait=0, enter=False, latencia=0):
		elemento = self.elemento(xpath, wait);
		if elemento == None:
			return False;
		else:
			elemento.clear();
			if latencia == 0:
				elemento.send_keys(texto);
			else:
				for caracter in texto:
					elemento.send_keys(caracter);
					time.sleep(latencia);

			if enter == True:
				elemento.send_keys(Keys.ENTER);
			return True;
	def escrever_html(self, texto, xpath="//*[@class='wysiwyg']/div[2]/iframe"):
		frame = self.elemento(xpath);
		self.driver.switch_to.frame(frame)
		body = self.driver.find_element_by_xpath("//body");
		body.send_keys(texto)
		self.driver.switch_to.default_content()

	def estrair_para_texto(self, variable, row, fields, execute=None):
		fontes = [self.driver];
		saida = [];
		if row != None and row != "":
			fontes = self.elementos(row, wait=50);
		if fontes != None:
			for i in range(len(fontes)):
				buffer_linha = [];
				for j in range(len(fields)):
					try:
						if fields[j]["control"][0:1] == ".":
							buffer_elemento = fontes[i].find_element_by_xpath(fields[j]["control"]);
						else:
							buffer_elemento = self.driver.find_element_by_xpath(fields[j]["control"]);

						if buffer_elemento != None:
							if 'innerHTML' == fields[j]["attribute"]:
								buffer_linha.append(   buffer_elemento.text);
							else:
								buffer_linha.append(   buffer_elemento.get_attribute(fields[j]["attribute"]));
					except Exception as e:
						if fields[j]["control"][0:1] == ".":
							print("De ROW: ");
							print(fontes[i].get_attribute("innerHTML"));
						else:
							print("De Browser: ");
						print(e);
						buffer_linha.append("");
				saida.append(buffer_linha);
		else:
			print("ATENCAO: Fontes invalidas em: ", row);
		return saida;

	def existe_elemento(self, xpath):
		try:
			return self.driver.find_element_by_xpath(xpath) != None;
		except:
			return False;
						
	def extrair_para_variavel(self, control, propertys, max=9999 ):
		elementos = self.elementos(control);
		saida = [];
		for i in range(len(elementos)):
			buffer_array = [];
			for j in range(len(propertys)):
				buffer_array.append(elementos[i].get_attribute(propertys[j]));
			saida.append(buffer_array);
		return saida;

	def navegar(self, url, forcar=False, lista=None):
		if lista != None and url in self.historico["urls"][lista]:
			return False; #nao navegou, nao continua
		if forcar == False and url == self.driver.current_url:
			return True; # já tá na URL
		self.driver.get(url);
		self.historico["urls"].append(url);
		for i in range(len(self.eventos)):
			if tipo == "url":
				if self.eventos[i]['valor'] == url:
					self.eventos[i]['callback'](self.eventos[i]);
			elif tipo == "control":
				if self.elemento( self.eventos[i]['valor'], wait=0) != None:
					self.eventos[i]['callback'](self.eventos[i]);

	

	def registrar_evento(valor, script, tipo, callback):
		self.eventos.append({"valor" : valor, "script" :  script, "tipo" : tipo, "callback" : callback});

	def scroll(self, interacoes =1, wait=1):
		for i in range(interacoes):
			try:
				height = self.driver.execute_script("return document.body.scrollHeight")
				self.driver.find_element_by_tag_name('body').send_keys(Keys.END);			
			except Exception as e:
				self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				traceback.print_exc();
			time.sleep(wait);
		return True;


	def submit(self, xpath):
		try:
			self.elemento(xpath).submit();
			return True
		except Exception as e:
			traceback.print_exc();
			return False;
	def upload(self, xpath, filepath):
		file_input = self.elemento(xpath);
		self.driver.execute_script('arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";', file_input)
		file_input.send_keys(filepath);

	def validar(self):
		self.navegar("http://www.crawlerweb.com.br/crawler/validadores/mywebbot.php");
		elemento = self.elemento('//*[@id="trexposto"]');
		return elemento.text.lower() != "sim";

	def __del__(self):
		self.driver.close();

