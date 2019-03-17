# -GetPubli

Tutorial Criação do Ambiente virtual:

Pré-requisito: Python instalado

OBS: vá na pasta do projeto
1 - pip install virtualenv
2 - virtualenv venv
3 - cd venv
4 - cd scripts
5 - activate
6 - volta pro diretório onde está o requeriments.txt
7 - pip3 install -r requirements.txt
8 - python run.py runserver

Com o amiente criado e já utilizado, como eu entro nele a proxima vez que for utilizar o projeto?
OBS: vá na pasta do projeto
1 - cd venv
2 - cd scripts
3 - activate
4 - python run.py runserver

Esse é o projeto "Esqueleto", ele tem códigos da ac1(CRUD funcionario) e ac3(Dowload de arquivos).
Coisas importantes que TODOS devem verificar:
1 - Operações de CRUD
    No default.py
    1.1 - GET:    def get(info_get):
    1.2 - DELETE: def delete(info_del):
    1.3 - POST:   def post():
    
2 - Como receber informações de um formulário
    em forms.py
    2.1 - Criação da classe que irá receber informações nos templates
    
    em zip.html, jpg.html e pdf.html
    2.2 - Utilização da classe no HTML
    
    em default.pu
    2.3 - Como receber as informações desse HTML

