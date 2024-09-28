from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from schemas import *
from model import *
from logger import logger
from flask_cors import CORS

from schemas.passageiro_schema import PassageiroViewSchema

# Instanciando o objeto OpenAPI
info = Info(title="Titanic", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Passageiro", description="Predição de sobrevivência de passageiro ")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')




# Rota de adição de paciente
@app.post('/passageiro', tags=[paciente_tag],
          responses={"200": PassageiroViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: PassageiroSchema):

    """Determina se com as informações fornecidas o passageiro sobreviveria ou não ao desastre do Titanic
    
    Args:
        name (str): nome do paciente
        p_class (int): a classe que o passageiro viajará
        sex (str): sexo do passageiro
        age (int): idade do passageiro
        sibsp (int): quantidade de parentes horizontalmente relacionados
        parch (int): quantidade de parentes verticalmente relacionados
        fixed_fare (float): valor do ingresso que o passageiro pretende pagar
        pronome (float): pronome de tratamento do passageiro
        cod_embarque (int): nome do porto em que pretende embarcar
    Returns:
        dict: representação do passageiro
    """
    # TODO: Instanciar classes

    # Recuperando os dados do formulário
    name = form.name
    p_class = form.pclass
    sex = form.sex
    age = form.age
    sibsp = form.sibsp
    parch = form.parch
    fixed_fare = form.fare
    pronome = form.pronome
    age = form.age
        
    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    # Carregando modelo
    model_path = 'ml/pipelines/rf_titanic_pipeline.pkl'
    # modelo = Model.carrega_modelo(ml_path)
    modelo = Pipeline.carrega_pipeline(model_path)
    # Realizando a predição
    outcome = int(Model.preditor(modelo, X_input)[0])

    return {"predict": outcome}
    
if __name__ == '__main__':
    app.run(debug=True)