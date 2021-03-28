# Etágio zero é fazer a extração de dados lá no wiki

import time, os, traceback, sys;

from browser.wiki import *;
from utilitario import *;

w = Wiki();

while True:
	arquivo = Utilitario.arquivo("0");
	if arquivo != None:
		try:
			arquivo["paginas"] = w.extrair(arquivo["termo"], 3);
			Utilitario.salvar("1", arquivo, arquivo["nome"]);
			os.unlink("./arquivos/estagio0/" + arquivo["nome"]);
			continue;
		except Exception:
			traceback.print_exc();
	time.sleep(60);



