from dataclasses import dataclass
from circuitcrash.domain.missoes import Missao, Conquista


@dataclass
class ResultadoPartida:
    colocacao: int
    fagulhas_ganhas: int
    vitorias: int = 0


class AtualizadorDeMissoes:
    def __init__(self, missoes: list[Missao], conquistas: list[Conquista]):
        self.missoes = missoes
        self.conquistas = conquistas

    def processar_partida(self, resultado: ResultadoPartida) -> None:
        """Avança o progresso das missões e conquistas com base na partida."""
        for missao in self.missoes:
            if not missao.concluida:
                missao.avancar(1)

        for conquista in self.conquistas:
            if not conquista.desbloqueada:
                if resultado.vitorias > 0:
                    conquista.avancar(resultado.vitorias)
