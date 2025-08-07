# AIAgent
AIAgent on local with vector DB

run first 
for lower pythion version 
python -m venv venv 

for python 3 + version 
python3 -m venv venv

for mac 
./venv/bin/activate

if you got error 
The error zsh: permission denied occurs because the activate script does not have the necessary execute permissions. You can fix this by granting execute permissions to the activate script.

Steps to Fix:
Run the following command to add execute permissions:
chmod +x ./venv/bin/activate

Then, activate the virtual environment:
source ./venv/bin/activate


for windows
./venv/Scripts/activate

Then install all the libs from the requirements.txt file 
pip install -r requirements.txt 

otherwise 
pip install  langchain langchain-ollama langchain-chroma pandas

Then please install the ollama models which you want to use or run on your machine refer website https://ollama.com/

after installation check ollama list which will show all models which you installed, try to use llama3.2 which we are going to use id,size and modifed will be differe
ollama list
NAME               ID              SIZE      MODIFIED       
llama3.2:latest    a8190f17acd5    2.0 GB    18 seconds ago    
mistral:latest     9007803aa9a0    4.4 GB    2 days ago        
gemma3:4b          a2af6c89eb7f    3.3 GB    2 days ago

Then install the ollama pull mxbai-embed-large model which we are going to use for embedding id,size and modifed will be differe
ollama list
NAME                        ID              SIZE      MODIFIED       
mxbai-embed-large:latest    468836162e7d    669 MB    13 seconds ago    
llama3.2:latest             a8190f17acd5    2.0 GB    2 minutes ago     
mistral:latest              9007803aa9a0    4.4 GB    2 days ago        
gemma3:4b                   a2af6c89eb7f    3.3 GB    2 days ago   





