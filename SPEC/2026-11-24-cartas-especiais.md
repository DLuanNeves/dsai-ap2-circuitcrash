# Spec: Cartas especiais

*Data:* 2026-11-24
*Status:* rascunho
*Origem:* item 2 de "Próximos passos" do README (cartas especiais)

## O quê e por quê

A tela de regras já descreve três cartas especiais (Isolante, Ponte e Curto), mas na partida elas ainda não funcionam. Esta funcionalidade faz as três cartas funcionarem, para dar mais estratégia ao jogo.

## Regras gerais

- Cada jogador começa a partida com 1 carta de cada tipo (3 no total).
- Cada carta pode ser usada uma única vez por partida.
- Usar uma carta é a ação do turno: no mesmo turno o jogador não coloca peça, não gira peça e não passa a vez.
- A regra atual continua valendo: a mesma peça não pode ser girada em duas rodadas seguidas.
- Cartas já usadas aparecem marcadas como usadas na tela e não podem ser escolhidas de novo.

## Histórias de usuário

### 1. Isolante
Como jogador, quero bloquear uma casa vazia para impedir que os adversários liguem seus circuitos por ali.

- Só pode ser usada numa casa vazia.
- A casa fica bloqueada até o fim da partida, para todos os jogadores (inclusive quem usou).
- Nenhuma peça pode ser colocada numa casa bloqueada.
- A casa bloqueada aparece marcada na tela.

### 2. Ponte
Como jogador, quero passar por cima de uma peça adversária para ligar meu circuito a uma casa vazia do outro lado.

- Liga o meu circuito a uma casa vazia do outro lado de uma peça adversária, em linha reta.
- A casa de destino deve estar vazia e não bloqueada.
- A peça adversária não é alterada nem removida.
- A Ponte atravessa exatamente uma peça (decisão provisória, a confirmar com o cliente).

### 3. Curto
Como jogador, quero remover uma peça adversária para cortar o circuito dele.

- Só pode remover peça de adversário, nunca a minha.
- Não pode remover uma base, a fonte de energia nem uma peça que encosta numa base.
- Se o circuito do adversário é cortado, o objetivo volta a ficar neutro e os pontos já ganhos ficam com quem capturou.
- A casa da peça removida fica vazia e pode receber peças de novo.
- Pode ser usado numa peça girada na mesma rodada (decisão provisória, a confirmar com o cliente).

## Requisitos

- FR-001: cada jogador começa com 3 cartas, uma de cada tipo, e o estado "usada ou não" é guardado na partida.
- FR-002: usar uma carta consome o turno inteiro do jogador.
- FR-003: uma carta usada não pode ser usada de novo na mesma partida.
- FR-004: o servidor valida cada uso (casa vazia, casa não bloqueada, peça de adversário, peça que não encosta em base). Jogada inválida é recusada com mensagem clara.
- FR-005: a tela mostra as cartas disponíveis, as usadas e as casas bloqueadas.
- FR-006: o cálculo de energia, a captura de objetivos e os pontos continuam como hoje.

## Critérios de aceitação

1. Com 4 jogadores, cada um começa com 3 cartas disponíveis.
2. O Isolante numa casa vazia impede qualquer peça ali até o fim; numa casa ocupada é recusado.
3. A Ponte liga meu circuito a uma casa vazia do outro lado de uma peça adversária, sem mexer nessa peça.
4. O Curto remove uma peça adversária desprotegida; nas protegidas (base, fonte, peça que encosta numa base, minha peça) é recusado.
5. Depois de um Curto que corta o circuito, o objetivo volta a neutro e os pontos continuam com quem capturou.
6. Depois de usar uma carta, o jogador não usa a mesma de novo e não faz outra ação no turno.
7. Os testes atuais continuam passando, mais os testes novos das cartas.
8. ruff check, ruff format --check e mypy passam sem erro.

## Fora do escopo

- Novas cartas além das três.
- Partida privada e campeonatos.
- Mudar o valor dos objetivos, das Fagulhas ou do rating.
- Comprar cartas na loja.