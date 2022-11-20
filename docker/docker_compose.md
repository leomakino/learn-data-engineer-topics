Docker Compose é o orquestrador de containers da Docker.
Ele segue os comandos de arquivos YAML (.yml)
Arquivos YAML descrevem a infraestrutura como código e como ela vai se comportar ao ser iniciado.
podemos definir o comportamento que o Docker vai ter caso um dos containers venha a falhar
utilizando o Docker Compose, em vez de o administrador executar o docker run na mão para cada container e subir os serviços separados, linkando os containers das aplicações manualmente, temos um único arquivo que vai fazer essa orquestração e vai subir os serviços/containers de uma só vez. 
OBS: Os comandos do Docker Compose só vão funcionar passando o caminho do diretório ou estando no mesmo diretório do arquivo do docker-compose.yml
docker-compose up
Docker vai baixar as imagens que vão ser usadas nesse compose.
Podemos colocar a flag -d para termos o terminal funcional, enquanto o compose roda em segundo plano
Usado para executar o arquivo yml

docker-compose ps
Listar nomes de aplicações, status de serviço e portas de cada container.

docker-compose stop
Parar serviço

docker-compose rm -f
Remove container