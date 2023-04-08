# Cloud vs on premise
Cloud computing Advantages:
- flexibility/Elasticity;
- Save time and money;
- Improve agility and scalability
- Deploy globally in minutes.
- Serveless: Sem infraestrutura para configurar ou gerir. Geralmente, paga-se apenas por consumo.

On-premises applications Advantage:
- reliable;
- secure;
- allow enterprises to maintain close control.

# S3
Simple Service Storage (S3) is an object storage service offering scalability, data availability, security, and performance.

Customers of all sizes can store and protect any amount of data for virtually any use case, such as data lakes, archive data at the lowest cost, and run cloud-native applications.

Nesse serviço, dados são armazenados como objetos em recursos chamados buckets

AWS S3 offers 3 storaged classes designed for different use cases.
-S3 Standard for general-purpose storage of frequently accessed data
-S3 Standard-Infrequent Access (S3 Standard-IA), for long-lived, but less frequently accessed data
-Amazon Glacier, for low-cost archival data

A configuração de ciclo de vida (S3 Lifecycle) permite economizar nos custos de armazenamento. Ele é um conjunto de regras que define as ações aplicadas pelo S3 a um grupo de objetos. Regras, tais como: (i) Ações de transição e (ii) Ações de expiração.

S3 Transfer Acceleration possibilita transferências rápidas em longas distâncias entre um cliente e um bucket do S3.
Como esse serviço garante essa agilidade? Os dados passam por pontos de presenças que podem ou não ser roteados para caminhos otimizados. Este serviço envolve custos adicionais.

# Redshift
AWS Redshift é um serviço de armazenamento de dados em escala de petabytes totalmente gerenciado na nuvem.

Um AWS Redshift Data Warehouse é um conjunto de recursos informáticos chamados nodes, que compõem um grupo chamado de cluster. Cada cluster executa um Redshift engine e contém uma ou mais bases de dados.

Ele visa rápida consulta de dados em Big Data

# IAM
É um serviço de segurança e controle de acesso.

IAM para controlar autenticação (login) e permissões (acesso liberado) de recursos.

IAM Role é uma identidade com permissões específicas que determinam o que a identidade pode e não pode fazer na AWS

IAM Policy: Gestão de acesso através de políticas. Cria-se políticas e anexa-se às identidades do IAM (users, groups, ou roles) ou recursos da AWS.

# SQS
SQS é um serviço de fila de mensagens usado por app distribuídos para trocar mensagens através de um modelo de sondagem.

SQS fornece flexibilidade para que componentes distribuídos de aplicativos enviem e recebam mensagens sem a necessidade de que cada componente esteja simultaneamente disponível.

Simple Queue Service (SQS) oferece filas seguras, duráveis e disponíveis. Este serviço permite integrar e associar sistemas de softwares e componentes distribuídos.

Ele oferece constructos, tais como dead letter queues e tags. Além disso, oferece uma API compatível com o SDK da AWS.

SQS oferece suporte a filas padrão e FIFO.

**Benefícios do serviço**:

-   **Security:** send/receive messages control. SSE allows transmitting sensitive data by protecting the contents of messages in queues using keys managed in AWS Key Management Service (AWS KMS).

-   **Durability:** It ensures the safety of messages storing them on multiple servers. Standard queues support at-least-once message delivery. FIFO queues support exactly-once message processing

-   **Availability:** It uses redundant infrastructure to provide message production/consumption and access to these messages.

-   **Scalability:** It processes buffered requests independently. It can be any load or spikes and it won't require any provisioning instructions.

-   **Reliability:** AWS SQS locks messages during processing.

- **Customization:** Set default delay on queue; Store contents of messages larger than 256KB. Split large messages into smaller messages.

Um padrão comum é usar o Simple Notification Service (SNS) para publicar mensagens nas filas do SQS a fim de enviar mensagens de forma confiável e assíncrona para um ou mais componentes do sistema.

# Cloud Watch
AWS Cloud Watch monitora recursos/serviços da AWS e os aplicativos executados na AWS em tempo real.

Este serviço pode ser utilizado para coletar e monitorar métricas, que são as variáveis que é possível medir para avaliar seus recursos e aplicativos.

Caso de uso: Criação de alarmes que observem métricas e com a possibilidade ou não de envio de notificação e/ou alterações automáticas.

Ex: Monitorar uso de CPU e disco de um EC2 e usar essas métricas para para iniciar instâncias adicionais para lidar com o aumento de carga.

# EMR
É uma plataforma de cluster gerenciada que simplifica a execução de estruturas open-source de Big Data (Apache Hadoop, Apache Spark) para processar e analisar grandes quantidades de dados.

# Athena
É um serviço de query (consultas interativas) no S3 usando SQL padrão.
Exemplo: Usar o Athena no AWS S3 para executar consultas ad-hoc e receber resultados.

Athena é serverless, portanto, não há qualquer infraestrutura para configurar ou gerir, apenas paga-se as queries executadas.

# Glue
Glue is a fully managed ETL service that makes it simple and cost-effective to categorize your data, clean it, enrich it, and move it reliably between various data stores and data streams.

AWS Glue consists of a central metadata repository known as the AWS Glue Data Catalog, an ETL engine that automatically generates Python or Scala code, and a flexible scheduler that handles dependency resolution, job monitoring, and retries.

When should I use AWS Glue? 
> When it’s necessary to organize, cleanse, validate, and format data for storage in a data warehouse or data lake.

# Dynamo
É um serviço de banco de dados NoSQL gerenciado. Ele fornece desempenho rápido, é previsível com escalabilidade contínua. Sem se preocupar com provisionamento, nem com escalabilidade de cluster.

DynamoDB oferece criptografia em repouso, que elimina a carga operacional e a complexidade na proteção de dados confidenciais.

# EC2
Elastic Compute Cloud (EC2) oferece capacidade de computação dimensionável na nuvem da AWS.

Ele também elimina a necessidade de investir em hardware inicialmente

Aplicações: Executar servidores virtuais, configurar a segurança, rede e o gerenciamento de armazenamento.

EC2 permite a expansão ou a redução para gerenciar as alterações de requisitos ou picos de popularidade, reduzindo assim, a necessidade de prever o tráfego do servidor.

# Cognito
Cognito fornece autenticação, autorização e gerenciamento de usuários para aplicativos móveis e web.

- User pools: grupos de usuários que são diretórios de usuários que fornecem opções de cadastro e login para os usuário de um aplicativo.
- Identity pools: grupos de identidade que permite a concessão de acessos aos usuários a outros serviços de AWS.
