import os, json;

class Utilitario:
	@staticmethod
	def arquivo(estagio):
		arr = os.listdir("./arquivos/estagio" + estagio);
		if len(arr) > 0:
			buffer = json.loads(open("./arquivos/estagio" + estagio + "/" + arr[0], "r").read());
			buffer['nome'] = arr[0];
			return buffer;
		return None;
	@staticmethod
	def salvar(estagio, js, nome):
		f = open("./arquivos/estagio" + estagio + "/" + nome, "w");
		f.write(json.dumps(js));
		f.close();
		return True;