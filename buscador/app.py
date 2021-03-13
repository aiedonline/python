

from google import *;
from bing import *;
from tor import *;

#t = Tor("9050");
#t.teste(); 


g = Google("9050");
b = Bing("9050");
print(  g.executeBusca("Python é fácil?") );
print(  b.executeBusca("Python é fácil?") );
