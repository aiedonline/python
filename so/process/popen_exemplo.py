#O subprocessmódulo permite que você crie novos processos, conecte-se a seus canais de entrada / saída / erro
#   e obtenha seus códigos de retorno. Este módulo pretende substituir vários módulos e funções mais antigos:
import subprocess
from subprocess import Popen




#A criação e o gerenciamento do processo subjacente neste módulo são tratados pela Popen. 
#    Ele oferece muita flexibilidade para que os desenvolvedores sejam capazes de lidar com os casos
#    menos comuns não cobertos pelas funções de conveniência.

#Execute um programa filho em um novo processo. No POSIX, a classe usa um os.execvp()comportamento
#    semelhante ao de -para executar o programa filho. No Windows, a classe usa a CreateProcess()função Windows.

#Parametros esperados:
#    universal_newlines=True
#    shell=True
p = Popen(["ls","-l"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)


# Interaja com o processo: Envie dados para stdin. Leia os dados de stdout e stderr, até que o
#    fim do arquivo seja alcançado. Aguarde o encerramento do processo e defina o returncodeatributo.
#    communicate()retorna uma tupla . Os dados serão strings se os fluxos forem abertos no modo de texto;
#    caso contrário, bytes.(stdout_data, stderr_data)
output, errors = p.communicate();
#proc = subprocess.Popen(...)
#try:
#    outs, errs = proc.communicate(timeout=15)
#except TimeoutExpired:
#    proc.kill()   OUUUU    Popen.send_signal( sinal ) 
#    outs, errs = proc.communicate()


#Popen.returncode
#O código de retorno filho, definido por poll()e wait()(e indiretamente por communicate()).
#    Um Nonevalor indica que o processo ainda não terminou.

print(output, errors);

