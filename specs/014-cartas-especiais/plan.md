# Plano: Cartas especiais

*Spec:* SPEC/2026-11-24-cartas-especiais.md
*Data:* 2026-11-24

## Visão geral

Fazer as cartas Isolante, Ponte e Curto funcionarem na partida. As regras ficam em Python puro na camada domain, a tela na camada web. Nenhuma mudança no cálculo de energia, nos pontos ou no rating.

## Onde mexer

- src/circuitcrash/domain/tabuleiro.py: regras da partida (estado, colocar peça, circuito, pontos).
- src/circuitcrash/web/: telas e rotas da partida (mostrar cartas, casas bloqueadas e receber o uso da carta).
- tests/: testes novos das cartas, ao lado dos testes atuais do tabuleiro.
- src/circuitcrash/mcps/: só se o servidor MCP precisar reconhecer a ação; senão, fica registrado como fora do escopo.

## Decisões de projeto

1. *Cartas no jogador:* cada jogador na partida guarda quais cartas ainda tem (Isolante, Ponte, Curto). Todas começam disponíveis.
2. *Casas bloqueadas:* o estado da partida guarda um conjunto de casas bloqueadas pelo Isolante. A função que coloca peças recusa essas casas.
3. *Uma função por carta:* usar_isolante, usar_ponte e usar_curto, no mesmo estilo das funções atuais. Cada uma valida a jogada, recusa com mensagem clara se for inválida e, se der certo, marca a carta como usada e passa a vez.
4. *Ponte:* guarda uma ligação extra entre duas casas do mesmo jogador, e o cálculo do circuito passa a considerar essa ligação junto das peças.
5. *Curto:* remove a peça, esvazia a casa e chama o recálculo existente (recalcular). Os pontos já ganhos ficam com quem capturou.
6. *Sem mudança de banco nesta etapa:* as cartas valem durante a partida em andamento. Guardar cartas nas partidas gravadas fica para uma spec futura.

## Riscos

- O cálculo do circuito é o coração do jogo. A Ponte mexe nele, então precisa de testes antes de qualquer mudança.
- Partidas gravadas existentes não devem quebrar: os campos novos têm valor padrão.

## Ordem de trabalho

1. Testes das regras (Isolante, Curto, Ponte).
2. Regras no tabuleiro.py.
3. Tela e rotas.
4. Conferir pytest, ruff e mypy.
5. Atualizar o README e publicar no Render.