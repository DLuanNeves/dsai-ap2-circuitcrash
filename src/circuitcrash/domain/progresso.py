from dataclasses import dataclass

from circuitcrash.domain.catalogo_missoes import TipoMissao
from circuitcrash.domain.missoes import Conquista, Missao


@dataclass
class ResultadoPartida:
    colocacao: int
    fagulhas_ganhas: int
    vitorias: int = 0
    baterias_capturadas: int = 0
    avatares_usados: int = 1
    ranking_anterior: int = 100
    ranking_atual: int = 100

    @property
    def posicoes_subidas(self) -> int:
        if self.ranking_anterior > self.ranking_atual:
            return self.ranking_anterior - self.ranking_atual
        return 0


class AtualizadorDeMissoes:
    def __init__(self, missoes: list[Missao], conquistas: list[Conquista]):
        self.missoes = missoes
        self.conquistas = conquistas

    def processar_partida(self, resultado: ResultadoPartida) -> None:
        """Avança o progresso das missões e conquistas com base na partida."""
        for missao in self.missoes:
            if missao.concluida:
                continue

            if missao.tipo == TipoMissao.JOGAR_PARTIDAS.value:
                missao.avancar(1)
            elif (
                missao.tipo == TipoMissao.VENCER_PARTIDAS.value
                and resultado.vitorias > 0
            ):
                missao.avancar(resultado.vitorias)
            elif missao.tipo == TipoMissao.GANHAR_FAGULHAS.value:
                missao.avancar(resultado.fagulhas_ganhas)
            elif missao.tipo == TipoMissao.USAR_AVATAR.value:
                missao.avancar(1)
            elif missao.tipo == TipoMissao.CAPTURAR_BATERIAS.value:
                missao.avancar(resultado.baterias_capturadas)
            elif missao.tipo == TipoMissao.SUBIR_RANKING.value:
                missao.avancar(resultado.posicoes_subidas)
            else:
                missao.avancar(1)

        for conquista in self.conquistas:
            if not conquista.desbloqueada and resultado.vitorias > 0:
                conquista.avancar(resultado.vitorias)
