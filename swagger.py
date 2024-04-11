from flask_restx import Api

api = Api(
    default="Rotas",
    default_label="Rotas disponíveis",
    title="API Vitibrasil",
    description="API de consulta na Vitibrasil",
    authorizations={
        'Bearer': {
            'description': 'No campo Value digite "Bearer <access_token>"',
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }
)