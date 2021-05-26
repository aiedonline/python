#!/usr/bin/python3
import json

from browser.browser import *;

buscas = json.loads(open("./data/busca.json").read());

b = Browser(terminal=False, path_directory_browser="/tmp/pensador/");

def raspar(b, lista_frases):
	time.sleep(5);
	elementos = b.elementos('//*[@class="frase fr"]');
	for elemento in elementos:
		lista_frases.append(elemento.text.encode().decode("utf-8"));

for busca in buscas:
	lista_frases = [];
	for frase in busca['frases']:
		b.navegar("https://www.pensador.com");
		time.sleep(5);
		b.escrever('//*[@name="q"]', frase, enter=True);
		raspar(b, lista_frases)
		while True:
			b.clicar('//*[text()="Próxima >"]');
			raspar(b, lista_frases);
			if not b.existe_elemento('//*[text()="Próxima >"]'):
				break;
	f = open("./tmp/" + busca['id'] + ".json", "w");
	f.write(json.dumps(lista_frases,  ensure_ascii=False) );
	f.close();





