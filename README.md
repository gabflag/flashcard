<h1>FLASHCARD</h1>

# Tecnologias utilizadas:

  - Python 3.9.7 e suas biblioteca TkInter, mysql.connector, calendar, datetime, random
  - MySQL Workbench
  - InkScape

# A respeito do programa:
  O Flashcard é um software de cartões de memorização que emprega a técnica de repetição espaçada para maximizar a retenção de informações. Através de 
  um algoritmo, o programa calcula os intervalos ideais de revisão para cada cartão. Dentro do projeto, na página principal, você encontrará o script
  necessário para criar o banco de dados com inserções de teste, caso queira, basta alterar o script.
  
# Objetivo:
  
  * Consulta, criação, atualização e exclusão de cartões no banco de dados;
  * Demonstrar como pode ser realizado a integração de um banco de dados com um programa funcional;
  * Demonstrar como pode ser criado e utilizado caixa de mensagens com o TkInter;
  * Demonstrar a criação de uma interface gráfica e navegabilidade entre telas;
  * Implementação de um algoritmo de repetição espaçada.


# Modo de uso:

  - Execute o arquivo 'main.py' que está na pasta 'view';
  - Faça login usando o usuário root:root OU admin:admin e clique no botão 'ENTRY';
  - Ao abrir a tela de cartões, o cartão da vez será mostrado. Você pode clicar no botão 'ANSWER' para mostrar a resposta', clique no botão 
  RIGTH' caso saiba a resposta ou 'WRONG' caso não saiba. Observação, aqui você tem a liberdade de apertar os botões 'RIGTH' e 'WRONG' mesmo não
  exibindo a resposta com o botão 'ANSWER', o intuito é agilizar o processo de revisão;
  - Se você não tem cartões para revisar será mostrando no campo de diálogo entre os botões 'ANSWER' e 'WRONG' a mensagem 'Doens't exist card to review';
  - Se você tem cartões para revisar será mostrando no campo de diálogo entre os botões 'ANSWER' e 'WRONG' a mensagem 'You have Y cards to review now :D';
  - Para adicionar um cartão basta preencher os campos de 'FRONT' com a parte da frente do cartão e o campo 'ANSWER' com a resposta desse cartão.
  Feito issso, clique no botão superior esquerdo 'Options' e depois clique na opção 'new', uma mensagem de sucesso será exibida;
  - Para editar o cartão, ao aparecer o cartão desejado na tela, edite os campos 'FRONT' com a parte da frente do cartão e o campo 'ANSWER' com a 
  resposta desse cartão atualizadas. Feito issso, clique no botão superior esquerdo 'Options' e depois clique na opção 'Edit', uma mensagem de sucesso 
  na ação efetuada será exibida;
  - Para excluir um cartão, ao aparecer o cartão desejado na tela, clique no botão superior esquerdo 'Options' e depois clique na opção 'Delete',
  uma mensagem de sucesso na ação efetuada será exibida
  - Para sair do programa, clique no botão superior esquerdo 'Options' e depois clique na opção 'Exit', você será redirecionado para a página de login.

# Pontos a serem melhorados:
  
  - Criar uma função de criptografia e descriptografia nos dados inseridos no banco de dados (talvez o sha256 ou AES devem ser consideradas);
  - Programa especifico para testes;

# Informações relevantes:
  
  * Artes gráficas foram criadas no Inkscape
  * Necessário instalar o MySQL Workbench e configurar o arquivo 'card_crontroller.py' com suas credenciais; 
  * Necessário instalar e importar as seguintes bibliotecas:
    
    - pip install mysql-connector-python
    - pip install tk
  
  * Caso queira fazer um executavel, recomendo trabalhar com um ambiente virtual. Para criar o executavel:
    - pip install pyinstaller
    - pyinstaller --onefile -w main.py
    
# Considerações do DEV:

  <p>A transição de telas foi um desafio a ser vencido, em um primeiro momento o que foi feito era trabalhar com dois objetos, o primeiro a tela de login
  e o segundo a tela do sistema. Com essa estrutura, a única solução que aparentava ser viável era destruir a primeira tela ao validar os dados, para assim,
  abrir a segunda tela. Era funcional, entretanto, o leg de abertura gerava um certo incomodo. A solução encontrada foi trabalhar com atualização da página,
  excluindo e editando atributos do objeto, dessa forma a transição ficou flúida.</p>
  <p>Não menos importante, deixei um script com nome "data_base_inserts" para que você atualize o banco de dados para o período que você for fazer os testes,
  neste, basta alterar os paramentos ao executar (cheque as duas ultimas linhas do arquivo - obj.generate_sql_inserts_prior_today(1, 21) : 
  obj.generate_sql_inserts_after_today(21, 101)) e atualizar seu script com os novos cartões.</p>

  
# Observações:
  
  Considero um projeto interessante para quem gostaria de fixar conceitos e checar como pode ser simples fazer uma aplicação em CRUD com Python e MySQL. O algoritmo
  de repetição espaçada aqui implementado consiste em caso a resposta seja correta se adiciona na data de criação a diferença entre a data de criação do cartão a
  data de revisão, para os casos de resposta errada, a data de criação do cartão recebe a metade da diferença entre a data de revisão e data de criação.
  Caso tenha algum erro de lógica no código, ortografia ou melhores maneiras de serem executadas as tarefas dispostas ficaria grato pela compreensão, 
  aprecio sugestões para melhorar.
   

# Imagens:

![tela_inicial](https://user-images.githubusercontent.com/95552879/219486776-f0f12e4a-d41b-4ee0-8eb5-1865ba8bd669.png)

![erro_credentials](https://user-images.githubusercontent.com/95552879/219486812-b309cb58-c410-4478-86fa-8f97a9cad545.png)

![tela_sistema](https://user-images.githubusercontent.com/95552879/219486842-7ae02a7c-556e-4a20-a19f-566d92f12c9e.png)

![edit_after](https://user-images.githubusercontent.com/95552879/219486908-5d801172-8a48-49d9-bdd9-2399a0a3ec36.png)

![erro_unfilled](https://user-images.githubusercontent.com/95552879/219486875-3a6b7469-a066-4755-84c0-8f2f7563950c.png)
