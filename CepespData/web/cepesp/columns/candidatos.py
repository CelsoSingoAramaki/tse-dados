class CandidatosColumnsSelector:

    def columns(self):
        return [
            'ID_CANDIDATO',
            'DATA_GERACAO',
            'HORA_GERACAO',
            'ANO_ELEICAO',
            'NUM_TURNO',
            'DESCRICAO_ELEICAO',
            'SIGLA_UF',
            'SIGLA_UE',
            'DESCRICAO_UE',
            'CODIGO_CARGO',
            'DESCRICAO_CARGO',
            'NUMERO_PARTIDO',
            'SIGLA_PARTIDO',
            'NOME_CANDIDATO',
            'NUMERO_CANDIDATO',
            'CPF_CANDIDATO',
            'NOME_URNA_CANDIDATO',
            'COD_SITUACAO_CANDIDATURA',
            'DES_SITUACAO_CANDIDATURA',
            'NOME_PARTIDO',
            'CODIGO_LEGENDA',
            'SIGLA_LEGENDA',
            'COMPOSICAO_LEGENDA',
            'NOME_COLIGACAO',
            'CODIGO_OCUPACAO',
            'DESCRICAO_OCUPACAO',
            'DATA_NASCIMENTO',
            'NUM_TITULO_ELEITORAL_CANDIDATO',
            'IDADE_DATA_ELEICAO',
            'CODIGO_SEXO',
            'DESCRICAO_SEXO',
            'COD_GRAU_INSTRUCAO',
            'DESCRICAO_GRAU_INSTRUCAO',
            'CODIGO_ESTADO_CIVIL',
            'DESCRICAO_ESTADO_CIVIL',
            'CODIGO_COR_RACA',
            'DESCRICAO_COR_RACA',
            'CODIGO_NACIONALIDADE',
            'DESCRICAO_NACIONALIDADE',
            'SIGLA_UF_NASCIMENTO',
            'CODIGO_MUNICIPIO_NASCIMENTO',
            'NOME_MUNICIPIO_NASCIMENTO',
            'DESPESA_MAX_CAMPANHA',
            'COD_SIT_TOT_TURNO',
            'DESC_SIT_TOT_TURNO',
            'EMAIL_CANDIDATO',
        ]

    def visible_columns(self):
        return ['ANO_ELEICAO', 'NUM_TURNO', 'DESCRICAO_ELEICAO', 'SIGLA_UF', 'SIGLA_UE', 'CODIGO_CARGO',
                'NUMERO_PARTIDO', 'SIGLA_PARTIDO', 'NUMERO_CANDIDATO', 'DES_SITUACAO_CANDIDATURA',
                'DESC_SIT_TOT_TURNO']

    def order_by_columns(self):
        return ['ANO_ELEICAO', 'SIGLA_UF', 'SIGLA_UE', 'CODIGO_CARGO', 'NUMERO_CANDIDATO']
