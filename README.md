# Titanic Challenge
Sprint Final da Pós-Graduação em Engenharia de Software da PUC Rio.

## Descrição
O dataset escolhido faz parte do Titanic Challenge, do kaggle.com.
O dataset foi escolhido devido a suas características, que permitem ações de engenharia de features e conhecimento do negócio.
Foi desenvolvido um backend extremamente simples que recebe dados de um passageiro imáginário
e retorna se esse paciente morreria ou não no Titanic.
O front end também foi o mais simples possível, utilizando apenas as tecnologias da primeira sprint.

## Como executar
O notebook pode ser executado dentro do Google Colab, mas recomenda-se que a execução
se dê no vscode, para uso de mais nucleos.
No repositório, acesse  /ml/notebooks/model_v2.ipynb

## API
Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```
Este comando instala as dependências/bibliotecas, descritas no arquivo 
`requirements.txt`. Caso o sistema apresente problemas, recomenda-se a remoção das versões no 
arquivo.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
## Front End
Basta executar o arquivo index.html na pasta frontend, preencher dados imaginários e enviar o formulário.

## Link para o vídeo
https://youtu.be/kMPBTPpI0Jc

