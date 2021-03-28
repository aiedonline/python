
import time, os, traceback, sys;

from utilitario import *;
from nltk import tokenize;

while True:
	arquivo = Utilitario.arquivo("1");
	if arquivo != None:
		try:
			for i in range(len(arquivo["paginas"])):
				arquivo["paginas"][i]["frases"] = tokenize.sent_tokenize(arquivo["paginas"][i]["texto"]);
			Utilitario.salvar("2", arquivo, arquivo["nome"]);
			os.unlink("./arquivos/estagio1/" + arquivo["nome"]);
			continue;
		except Excpetion:
			traceback.print_exc();
	time.sleep(60);


