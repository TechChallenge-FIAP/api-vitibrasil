install:
	\ 
	python3.8 -m pip install virtualenv; \
	python3.8 -m venv venv; \
	source venv/bin/activate; \
	pip install -r requirements.txt; \


run-prod:
	\
	source venv/bin/activate; \
	mkdir tmp; \
	python3 scrapping/scrapping.py; \
	flask --app rest_api/app.py db init; \
	python3 crud/Comercio.py; \
	python3 crud/Exportacao.py; \
	python3 crud/Importacao.py; \
	python3 crud/Processamento.py; \
	python3 crud/Producao.py; \
	flask --app rest_api/app.py run --host=0.0.0.0; \