from circuitcrash.domain.missoes import Conquista, Missao
from circuitcrash.domain.progresso import AtualizadorDeMissoes, ResultadoPartida


def test_atualizador_avanca_missoes_e_conquistas():
    missao = Missao(id=1, descricao="Jogar partidas", recompensa_fagulhas=10, meta=3)
    conquista = Conquista(id=1, titulo="Vencer", meta=1)
    atualizador = AtualizadorDeMissoes(missoes=[missao], conquistas=[conquista])

    resultado = ResultadoPartida(colocacao=1, fagulhas_ganhas=40, vitorias=1)
    atualizador.processar_partida(resultado)

    assert missao.progresso_atual == 1
    assert not missao.concluida
    assert conquista.desbloqueada
