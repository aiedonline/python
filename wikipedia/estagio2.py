import time, os, traceback, sys, spacy;


from utilitario import *;

sp = spacy.load("pt_core_news_sm");

while True:
	arquivo = Utilitario.arquivo("2");
	if arquivo != None:
		for i in range(len(arquivo["paginas"])):
			arquivo["paginas"][i]['ideias'] = [];
			for j in range(len(arquivo["paginas"][i]["frases"])):
				sentence = sp(arquivo["paginas"][i]["frases"][j]);
				for x in range(len(sentence.ents)):
					if x < len(sentence.ents) - 1:
						pos_inicio = arquivo['paginas'][i]['frases'][j].find(sentence.ents[x].text) + len(sentence.ents[x].text);
						pos_fim = arquivo['paginas'][i]['frases'][j].find(sentence.ents[x + 1].text);
						print("\033[1;33m", sentence.ents[x].text, "\033[0;0m", 
							arquivo['paginas'][i]['frases'][j][  pos_inicio :  pos_fim  ],
							"\033[1;33m", sentence.ents[x + 1].text, "\033[0;0m");
						
						sentence2 = sp( arquivo['paginas'][i]['frases'][j][ pos_inicio - len(sentence.ents[x].text)  : pos_fim + len(sentence.ents[x + 1].text)     ]   );
						buffer_verbos = [];
						for word in sentence2:
							if word.pos_ == "VERB" or word.pos_ == "AUX":
								buffer_verbos.append( word.text );
						ideia = {"conceitoa" : sentence.ents[x].text, "conceitob" : sentence.ents[x + 1].text,
									"ligacao" : arquivo['paginas'][i]['frases'][j][  pos_inicio :  pos_fim  ],
									"verbos" : buffer_verbos};
						arquivo["paginas"][i]['ideias'].append(ideia);
				print("\n\n");
		Utilitario.salvar("3", arquivo, arquivo['nome']);
		os.unlink("./arquivos/estagio2/" + arquivo['nome']);
	time.sleep(60);


