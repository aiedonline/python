#!/usr/bin/python3
# Faz download do chromedrive e ofusca para a versào corrente do GOOGLE CHROME

import subprocess, re, os, requests, unicodedata, time;
from lxml import html

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status();
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk);
    return local_filename;

def chromedriver_download(version, PATH_TO_CHROMEDRIVE, directory):
    print("\033[92m[+]\033[0m", "Versão corrente do GOOGLE CHROME: ", version);

    # Primeiro passo é obter o link para download da versão/subversão corrente
    page = requests.get("https://chromedriver.chromium.org/downloads");
    page.encoding = "utf-8";
    tree = html.fromstring(unicodedata.normalize(u'NFKD', page.text).encode('ascii', 'ignore').decode('utf8'));
    links = tree.xpath("//a[contains(@href, 'path="+ version +".')]");
    VERSAO_CROMEDRIVE_SITE = re.findall("[0-9.]+", links[0].attrib.get("href") );

    # montando a URL para download do Chromedrive do GNU/Linux 64bits
    link_download =  "https://chromedriver.storage.googleapis.com/" + VERSAO_CROMEDRIVE_SITE[-1] + "/chromedriver_linux64.zip";
    download_file(link_download, os.path.join(directory, "download.zip"));

    # Agora que o DOWNLOAD está feito, vamos descompactar e movimentar o arquivo resultante
    subprocess.run(["unzip", os.path.join(directory, "download.zip"), "-d", "/tmp/" ]);
    subprocess.run(["perl", "-pi", "-e", "'s/cdc_/abc_/g'", "/tmp/chromedriver"]); # OFUSCANDO.....
    os.rename("/tmp/chromedriver", PATH_TO_CHROMEDRIVE);

def vaidar_chromedrive(directory):
    p = subprocess.Popen(["google-chrome", "--version"], stdout=subprocess.PIPE);
    saida = p.communicate()[0];
    version = re.search("[0-9]{1,3}", str(saida))[0];
    PATH_TO_CHROMEDRIVE = os.path.join(directory, "chromedrive_" + version);
    if not os.path.exists(PATH_TO_CHROMEDRIVE):
        chromedriver_download(version, PATH_TO_CHROMEDRIVE, directory);
    
    # aqui você poderia chamar o Selenium.....

vaidar_chromedrive("/tmp");
