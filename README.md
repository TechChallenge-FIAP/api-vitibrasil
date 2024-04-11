# vitibrasil_api
Projeto para o Tech Challenge da FIAP que consiste na criação de uma API publica de consulta nos dados de vitivinicultura do site da Embrapa

# Dockerfile

Para rodar este projeto no docker é necessário rodar os seguintes comandos

```
docker build -t vitibrasil_api .
```

Com esse comando, a imagem do Dockerfile será criada.

Após isso, você pode rodar um desses 2 comandos sendo

```
docker run -it --network="host" vitibrasil_api
```

Esse comando irá mostrar os logs da API, caso queira sair basta aperta o Ctrl + C

```
docker run -d --network="host" vitibrasil_api
```

Esse comando somente roda o container sem precisar acessar o container para ver algum log.