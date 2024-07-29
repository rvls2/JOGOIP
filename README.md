# Snake python

Snake python é um jogo baseado em uma experiência 2D, que simula uma cobra que "passeia" pelo Grad5 e se "alimenta" de 3 coletáveis que remetem as questões fáceis, médias e difíceis das listas de IP, além disso, a cobra tenta fugir ao máximo do "run time error" - objeto que causa sua morte. Além do mais, o tamanho da cobra cresce à medida que mais se alimenta dos coletáveis e, ademais, a cobra também morre se tocar em si mesma e se bater nas "boradas" do jogo. Vale ressaltar também que:
- HARD: aumenta em dois a pontuação da cobra;
- MEDIUM: aumenta em três a potuação da cobra;
- EASY : aumenta em um a pontuação da cobra;

## Como rodar o jogo:
> 1º - É necessário ter uma IDE instalada, como o visual studio code ou o pycharm.
> >
> 2º - É necessário instalar o pygame e o python em sua máquina.
> >
> 3 º - Rodar o arquivo main.py

## Como jogar o jogo:
Para mover a cobrinha, é necessário usar as seguintes teclas:

   |  **Player** | &#8592; , &#8593; , &#8594; , &#8595;  |

Sendo a primeira delas para mover a cobrinha para o lado, a segunda mover para cima, a terceira mover para o outro lado e a quarta para baixo.

## Equipe:
- Aigo Alana (aacl)
- Ismael Álvaro (ials)
- Milla Rwana (mras)
- Pedro Henrique (phss)
- Rayssa Vitória (rvls)

## Divisão dos trabalhos:
- Aigo Alana: Criação de uma tela de menu e de fim de jogo, implementação de coletáveis com o adicional de uma pontuação diferente para cada coletável.
- Ismael Álvaro: Identificação e armazenamento dos coletáveis, estruturação dos diretórios, desenvolvimento da classe dos objetos coletáveis e atualização das imagens de Spritesheets.
- Milla Rwana: desenvolvimento da base do código, modularização e organização do código, implementação da lógica da movimentação da cobrinha.
- Pedro Henrique: Ajustes para garantir o bom desempenho do jogo, criação da função bomba e ajustes no código principal para integrar essa funcionalidade
- Rayssa Vitória: Aplicação dos sprites e a base do background, correção do tamanho da fonte na tela, testar o jogo para buscar possíveis erros.

## link para acessar o código:
- https://github.com/mi18242/JOGOIP

## Organização do código:
> Como usamos o conceito de modularização do código, o nosso código foi dividido em 4 módulos:

> - O módulo "functions.py" foi criado para armazenar as funções gerar_bomba, desenhar_bomba, desenhar_cobra, desenhar_pontuacao, selecionar_velocidade e fim_de_jogo:
  
    - gerar_bomba(): Gera uma posição aleatória para uma bomba que não colida com a cobra ou com a comida.
    - desenhar_bomba(): Desenha a bomba na tela na posição especificada com a cor vermelha.
    - desenhar_cobra(): Desenha a cobra na tela com base nas posições de cada pixel da cobra, usando a cor branca.
    - desenhar_pontuacao(): Desenha a pontuação na tela no canto superior esquerdo.
    - selecionar_velocidade(): Atualiza a direção da cobra com base na tecla pressionada, evitando que a cobra se mova na direção oposta imediatamente.
    - fim_de_jogo(): Exibe a tela de fim de jogo com a pontuação e capturas de cores diferentes, e permite reiniciar o jogo pressionando Enter.

> - O módulo "main.py" é a funcao principal do código e armazena as funções rodar_jogo e menu_principal:

    - rodar_jogo(): Esta função contém a lógica principal do jogo, inicializa as variáveis de estado do jogo (posição da cobra, tamanho, pontuação, capturas, etc.) e cria o grupo de sprites para gerenciar os objetos no jogo (comida e bomba). Além disso, trata eventos de saída e de pressionamento de teclas para atualizar a velocidade da cobra, atualiza a posição da cobra e verifica colisões com as bordas da tela. Vale ressaltar também que verifica colisões com a comida, atualiza o tamanho da cobra, pontuação, contagem de capturas e gera uma nova comida e bomba.
    - menu_principal(): Desenha a tela do menu e espera o jogador pressionar Enter para iniciar o jogo chamando a função rodar_jogo.

> - O módulo "Settings.py" é a funcao que inicializa o Pygame e faz as configurações principais do jogo, além disso define os caminhos para os diretórios principais, de imagens e sons e faz o carregamento de imagens e definição das cores.

> - O módulo "sprites.py" foi criado para armazenar uma classe chamada comida e a função update :

    - Class comida(): Define a classe Comida que herda de pygame.sprite.Sprite. O método __init__ inicializa a comida com base na posição atual da cobra (pixels). Além disso, define diferentes tipos de comida, cada um com uma cor e um valor de pontos, e seleciona um tipo aleatoriamente e associa a cor da comida selecionada a uma sprite_sheet correspondente, e extrai uma imagem da sprite_sheet. É importate citar também que define a imagem inicial da comida e configura sua posição e Garante que a comida não apareça sobre a cobra ao inicializar sua posição.
    - update(): Atualiza a imagem da comida e este método é chamado automaticamente em cada frame do jogo.

## Ferramentas e bibliotecas usadas:

- Pygame: Usado pra importar configurações próprias de jogo e, assim, facilitar o trabalho do grupo.
- random : Uma biblioteca nativa do Python que é responsável por facilitar as operações de aleatoriedade, como a geração das frutas e etc.
- os: Um módulo nativo do Python que fornece uma maneira de interagir com o sistema operacional, incluindo funções para manipulação de arquivos, diretórios e processos, bem como para obter informações sobre o ambiente do sistema. Foi usado no código, principalmente, na parte de settings.

## Conceitos apresentados na disciplina que foram aplicados:
  Utilizamos diversos conceitos enquanto estávamos desenvolvendo o jogo, dentre eles:

- Listas: Utilizadas na geração de bombas e na posição da cobra. No código rodar_jogo, por exemplo, a lista pixels armazena as coordenadas dos segmentos da cobra e é usada para evitar que a comida apareça em posições ocupadas pela cobra.
- Tuplas: Usadas para identificar coordenadas, como na definição da posição da comida e da bomba. No código da classe Comida, por exemplo, as tuplas são usadas para armazenar as coordenadas (comida_x, comida_y) e definir a posição da comida.
- Orientação a Objetos: Estruturação completa dos componentes do jogo. A classe Comida define objetos de comida, incluindo atributos como cor, pontos e métodos de atualização da posição e renderização.
- Condicionais: Importantes para as regras e colisões do jogo. No código rodar_jogo, as condicionais verificam se a cobra colidiu com as paredes ou consigo mesma, ou se a cobra colidiu com a comida ou com a bomba.
- Laços: O jogo ocorre dentro de um laço while not fim_jogo. Esse laço mantém o jogo em execução, atualizando a posição da cobra, desenhando os elementos na tela e verificando eventos de entrada do jogador.

## Desafios e Lições:
.....










    



    
















