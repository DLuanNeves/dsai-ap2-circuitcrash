import datetime
import random
from dataclasses import dataclass
from enum import Enum

from circuitcrash.domain.missoes import Missao


class TipoMissao(Enum):
    JOGAR_PARTIDAS = "jogar_partidas"
    VENCER_PARTIDAS = "vencer_partidas"
    GANHAR_FAGULHAS = "ganhar_fagulhas"
    USAR_AVATAR = "usar_avatar"
    CAPTURAR_BATERIAS = "capturar_baterias"
    SUBIR_RANKING = "subir_ranking"


@dataclass
class TemplateMissao:
    tipo: TipoMissao
    descricao: str
    meta: int
    recompensa: int


CATALOGO_DIARIO: list[TemplateMissao] = [
    TemplateMissao(TipoMissao.JOGAR_PARTIDAS, "Jogue 1 partida hoje", 1, 20),
    TemplateMissao(TipoMissao.JOGAR_PARTIDAS, "Jogue 3 partidas hoje", 3, 50),
    TemplateMissao(TipoMissao.JOGAR_PARTIDAS, "Jogue 5 partidas hoje", 5, 80),
    TemplateMissao(TipoMissao.JOGAR_PARTIDAS, "Jogue 10 partidas (Maratona)", 10, 150),
    TemplateMissao(TipoMissao.VENCER_PARTIDAS, "Vença 1 partida", 1, 100),
    TemplateMissao(TipoMissao.VENCER_PARTIDAS, "Vença 2 partidas", 2, 200),
    TemplateMissao(TipoMissao.VENCER_PARTIDAS, "Seja o campeão 3 vezes", 3, 300),
    TemplateMissao(TipoMissao.GANHAR_FAGULHAS, "Ganhe 50 Fagulhas", 50, 20),
    TemplateMissao(TipoMissao.GANHAR_FAGULHAS, "Ganhe 150 Fagulhas", 150, 50),
    TemplateMissao(TipoMissao.GANHAR_FAGULHAS, "Ganhe 300 Fagulhas", 300, 100),
    TemplateMissao(TipoMissao.USAR_AVATAR, "Jogue com 2 avatares diferentes", 2, 75),
    TemplateMissao(TipoMissao.USAR_AVATAR, "Jogue com 3 avatares diferentes", 3, 120),
    TemplateMissao(TipoMissao.CAPTURAR_BATERIAS, "Capture 3 baterias", 3, 30),
    TemplateMissao(TipoMissao.CAPTURAR_BATERIAS, "Capture 10 baterias", 10, 100),
    TemplateMissao(TipoMissao.CAPTURAR_BATERIAS, "Capture 20 baterias", 20, 200),
    TemplateMissao(TipoMissao.SUBIR_RANKING, "Suba 2 posições no ranking", 2, 80),
    TemplateMissao(TipoMissao.SUBIR_RANKING, "Suba 5 posições no ranking", 5, 200),
]


def gerar_missoes_do_dia(data_str: str) -> list[Missao]:
    """Sorteia 3 missões baseadas na data (para não mudar a cada refresh)."""
    dt = datetime.datetime.strptime(data_str, "%Y-%m-%d")
    seed = int(dt.timestamp())
    gerador = random.Random(seed)

    templates_sorteados = gerador.sample(CATALOGO_DIARIO, 3)

    missoes_geradas: list[Missao] = []
    for i, template in enumerate(templates_sorteados):
        missao = Missao(
            id=i + 1,
            descricao=template.descricao,
            recompensa_fagulhas=template.recompensa,
            meta=template.meta,
            progresso_atual=0,
            tipo=template.tipo.value,
        )
        missoes_geradas.append(missao)
    return missoes_geradas
