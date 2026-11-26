from circuitcrash.domain.catalogo_missoes import gerar_missoes_do_dia, CATALOGO_DIARIO


def test_gerar_missoes_do_dia():
    missoes = gerar_missoes_do_dia("2026-11-26")
    
    # Deve gerar a mesma quantidade de missões que o catálogo tem
    assert len(missoes) == len(CATALOGO_DIARIO)
    
    # A primeira missão do catálogo é "Jogue 3 partidas"
    assert missoes[0].descricao == "Jogue 3 partidas hoje"
    assert missoes[0].meta == 3
    assert missoes[0].progresso_atual == 0
