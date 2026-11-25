# Spec: Missões e Conquistas com Progresso Real

**Data:** 2026-11-25
**Status:** Aprovada

## O que é e por quê
Atualmente, as missões e conquistas mostram apenas dados de exemplo na tela. Esta funcionalidade tem como objetivo implementar o progresso real no banco de dados, fazendo com que as ações do jogador (como jogar partidas) avancem nas missões e concedam Fagulhas reais.

## Critérios de Aceitação
- [ ] As missões do dia devem avançar com base nas partidas jogadas e gravadas.
- [ ] As conquistas devem ser desbloqueadas ao atingir marcos específicos.
- [ ] As missões devem renovar automaticamente a cada dia.
- [ ] A recompensa em Fagulhas deve ser creditada no perfil do jogador ao concluir uma missão.
- [ ] O sistema deve respeitar o limite diário de Fagulhas por jogador.

## Fora do Escopo
- Criação de novas telas de administração para gerenciar as missões (isso será feito na funcionalidade #5).
- Notificações em tempo real (websockets) no momento em que a missão é concluída.
