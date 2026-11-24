# Tarefas: Cartas especiais

*Spec:* SPEC/2026-11-24-cartas-especiais.md
*Plano:* specs/014-cartas-especiais/plan.md

Cada tarefa vira um commit pequeno, com os trailers Agent: e Spec:.

## Fase 1: Estado das cartas

- [ ] T001 Teste: cada jogador começa com 3 cartas disponíveis (Isolante, Ponte, Curto).
- [ ] T002 Guardar as cartas do jogador e as casas bloqueadas no estado da partida (valores padrão, sem quebrar o que já existe).
- [ ] T003 Teste: usar uma carta consome o turno e ela não pode ser usada de novo.

## Fase 2: Isolante

- [ ] T004 Teste: Isolante em casa vazia bloqueia a casa; em casa ocupada é recusado.
- [ ] T005 Teste: nenhuma peça pode ser colocada em casa bloqueada.
- [ ] T006 Implementar usar_isolante e recusar casas bloqueadas ao colocar peça.

## Fase 3: Curto

- [ ] T007 Teste: Curto remove peça de adversário desprotegida e esvazia a casa.
- [ ] T008 Teste: Curto é recusado em base, fonte, peça que encosta numa base e peça própria.
- [ ] T009 Teste: depois de um Curto que corta o circuito, o objetivo volta a neutro e os pontos ficam com quem capturou.
- [ ] T010 Implementar usar_curto usando o recálculo existente.

## Fase 4: Ponte

- [ ] T011 Teste: Ponte liga o meu circuito a uma casa vazia do outro lado de uma peça adversária, sem alterá-la.
- [ ] T012 Teste: Ponte é recusada se o destino estiver ocupado, bloqueado ou fora de linha reta.
- [ ] T013 Implementar usar_ponte e considerar a ligação extra no cálculo do circuito.

## Fase 5: Tela

- [ ] T014 Mostrar as cartas (disponíveis e usadas) na tela da partida.
- [ ] T015 Marcar as casas bloqueadas no tabuleiro.
- [ ] T016 Rotas para usar cada carta, com mensagem clara quando a jogada for inválida.

## Fase 6: Fechamento

- [ ] T017 pytest, ruff check, ruff format --check e mypy sem erro.
- [ ] T018 Atualizar o README (cartas especiais prontas) e publicar no Render.