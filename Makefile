install:
	pip3 install -r requirements.txt

run-prod:
	python3 scrapping/scrapping.py
	python3 -m flask run --host=0.0.0.0