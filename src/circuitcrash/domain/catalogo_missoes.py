from dataclasses import dataclass
from enum import Enum
from circuitcrash.domain.missoes import Missao


class TipoMissao(Enum):
    JOGAR_PARTIDAS = "jogar_partidas"
    VENCER_PARTIDAS = "vencer_partidas"
    GANHAR_FAGULHAS = "ganhar_fagulhas"
    USAR_AVATAR = "usar_avatar"
    CAPTURAR_BATERIAS = "capturar_baterias"


@dataclass
class TemplateMissao:
    tipo: TipoMissao
    descricao: str
    meta: int
    recompensa: int


CATALOGO_DIARIO = [
    TemplateMissao(TipoMissao.JOGAR_PARTIDAS, "Jogue 3 partidas hoje", 3, 50),
    TemplateMissao(TipoMissao.VENCER_PARTIDAS, "Vença 1 partida hoje", 1, 100),
    TemplateMissao(TipoMissao.GANHAR_FAGULHAS, "Ganhe 150 Fagulhas hoje", 150, 50),
    TemplateMissao(TipoMissao.USAR_AVATAR, "Jogue com 2 avatares diferentes", 2, 75),
    TemplateMissao(TipoMissao.CAPTURAR_BATERIAS, "Capture 5 baterias", 5, 50),
]


def gerar_missoes_do_dia(data_str: str) -> list[Missao]:
    """Gera as missões diárias baseadas no catálogo."""
    missoes_geradas = []
    for i, template in enumerate(CATALOGO_DIARIO):
        missao = Missao(
            id=i + 1,
            descricao=template.descricao,
            recompensa_fagulhas=template.recompensa,
            meta=template.meta,
            progresso_atual=0,
            tipo=template.tipo
        )
        missoes_geradas.append(missao)
    return missoes_geradas
