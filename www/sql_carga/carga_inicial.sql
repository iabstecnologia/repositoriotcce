INSERT INTO
    repositorio_projeto (id, nome, ativo)
VALUES (1, 'TCCE 1/2018', TRUE),
    (3, 'TCCE 2/2020', TRUE),
    (4, 'TCCE 1/2022', TRUE),
    (5, 'TCCE 3/2026', TRUE)
ON CONFLICT (id) DO NOTHING;

INSERT INTO
    repositorio_subprojeto (nome, ativo, projeto_id)
VALUES (
        'Estudos Espeleológicos (Caráter Especial - Execução por Contrato)',
        TRUE,
        1
    ),
    (
        'Filogeografia de invertebrados troglóbios em formações ferríferas e carbonáticas',
        TRUE,
        1
    ),
    (
        'Bat caves em cavernas ferríferas da Floresta Nacional de Carajás: aspectos físicos, biológicos e cronológicos',
        TRUE,
        1
    ),
    (
        'Edital de Pesquisas Ecossistemica da Flona Carajás',
        TRUE,
        1
    ),
    (
        'Monitoramento térmico de bat caves em Florestas Nacional de Carajás',
        TRUE,
        1
    ),
    (
        'Associação de morcegos (Mammalia, Chiroptera) a cavidades ferríferas através de levantamentos simples - a importância das Aicom''s e Sicom''s',
        TRUE,
        1
    ),
    (
        'Geoquímica e Isótopos aplicados ao estudo geoecológico das cavernas da região de Carajás',
        TRUE,
        1
    ),
    (
        'Morcegos de cavernas: conhecer para preservar. Diversidade genética, banco de células e de tecidos',
        TRUE,
        1
    ),
    (
        'Diversidade de Arthropoda em cavidades da Floresta Nacional de Carajás e Parque Nacional dos Campos Ferruginosos - o habitat subterrâneo, a conectividade entre suas populações e a influência do entorno',
        TRUE,
        1
    ),
    (
        'Restauração Ambiental',
        TRUE,
        1
    ),
    (
        'Susceptibilidade, hidrologia e geomorfologia cárstica aplicadas à conservação do patrimônio espelológico da Área de Proteção Ambiental das nascentes do Rio Vermelho',
        TRUE,
        1
    ),
    (
        'Espeleometria e Gestão do Projeto',
        TRUE,
        1
    ),
    (
        'Apoio à gestão da APA',
        TRUE,
        1
    ),
    (
        'Estudo para criação de unidade de conservação federal de proteção integral na região da Serra do Ramalho, Bahia (Cooperação Técnica)',
        TRUE,
        1
    ),
    (
        'Correção, modernização e atualização do Cadastro Nacional de Informações Espeleológicas - CANIE',
        TRUE,
        1
    ),
    (
        'Aprimoramentos metodológicos para o Levantamento de Atributos Espeleométricos no Rito do Licenciamento Ambiental',
        TRUE,
        1
    ),
    (
        'Construção do Centro de Referência em Espeleologia e da sede do Cecav/ICMBio',
        TRUE,
        1
    ),
    (
        '5ª Edição curso Espeleologia (40 pessoas - 40 Horas) - Curso de Espeleologia e Licenciamento Ambiental do Instituto Chico Mendes',
        TRUE,
        1
    ),
    (
        'Livro Cavernas ferríferas do Brasil',
        TRUE,
        1
    ),
    (
        'Ecologia de Vertebrados Associados a Cavernas do Espinhaço Meridional',
        TRUE,
        1
    ),
    (
        'Dispersão versus confinamento: análise composicional e de estrutura de habitat como subsídio à compreensão de mecanismos responsáveis pela identidade faunística subterrânea',
        TRUE,
        1
    ),
    (
        'Revelando a biodiversidade subterrânea em um oásis na Caatinga',
        TRUE,
        1
    ),
    (
        'Prêmio Michel Le Bret de Espeleologia',
        TRUE,
        1
    ),
    (
        'Divulgação Científica e Educomunicação junto às comunidades locais no Parque Nacional Cavernas do Peruaçu, MG',
        TRUE,
        1
    ),
    (
        'Edital de Chamamento Público para seleção de Projetos sobre o Patrimônio Espeleológico em Rochas Ferruginosas',
        TRUE,
        1
    ),
    (
        'Diversidade taxonômica e funcional de insetos aquáticos neotropicais em igarapés das áreas ferruginosas do Brasil',
        TRUE,
        1
    ),
    (
        'DIVERSIDADE METABARCODING E FUNCIONAL DE COMUNIDADES MICROBIANAS DO SOLO DE CAVERNAS FERRÍFERAS DO PARQUE NACIONAL DOS CAMPOS FERRUGINOSOS - PA',
        TRUE,
        1
    ),
    (
        'Estudos da paisagem, da geodiversidade e propostas de geoconservação do Geossistema Ferruginoso Carajás, PA',
        TRUE,
        1
    ),
    (
        'Registros paleoambientais de depósitos de guano em cavernas ferríferas da Floresta Nacional de Carajás',
        TRUE,
        1
    ),
    (
        'Passado, presente e futuro para a conservação das áreas cavernícolas e dos serviços ecossistêmicos prestados por morcegos',
        TRUE,
        1
    ),
    (
        'Diversidade de organismos do solo, em cavernas em formação ferrífera no Quadrilatero Ferrifero, Minas Gerais, Brasil, com uso de DNA metabarcoding',
        TRUE,
        1
    ),
    (
        'Microbiota de cavernas da FLONA Carajás/PA: inventário e subsídios para o manejo espeleoturístico',
        TRUE,
        1
    ),
    (
        'TAXONOMIA E FILOGENIA MOLECULAR DE FUNGOS EM CAVERNAS FERRÍFERAS ENTRE AS REGIÕES DE CONCEIÇÃO DO MATO DENTRO E SERRO, MINAS GERAIS',
        TRUE,
        1
    ),
    (
        '37º Congresso Brasileiro de Espeleologia',
        TRUE,
        4
    ),
    (
        '39º Congresso Brasileiro de Espeleologia',
        TRUE,
        4
    ),
    (
        '19º Congresso Internacional de Espeleologia - CIE',
        TRUE,
        4
    ),
    (
        'CAVE TOOLS - Caderno de Campo Digital do CECAV - app para dispositivo móvel',
        TRUE,
        4
    ),
    (
        'Recifes de Coral - as cavernas submarinas do Nordeste do Brasil',
        TRUE,
        4
    ),
    (
        'Paisagem Sonora de Cavernas e dos Ecossistemas em seu entorno no Parque Nacional da Serra do Cipó',
        TRUE,
        4
    ),
    (
        'GAP - Gestão Administrativa dos Projetos e Ações necessários para viabilização e implementação das compensações espeleológicas',
        TRUE,
        4
    ),
    (
        'Geoespeleologia do Carste Siliciclático da Formação Tombador: Subsídios à Conservação do Patrimônio Espeleológico na Chapada Diamantina',
        TRUE,
        4
    ),
    (
        'Projeto Luzes na Escuridão',
        TRUE,
        4
    ),
    (
        'Aplicação de Traçadores corantes para caracterização da dinâmica atual de fluxo d''água subterrânea no Carste de São Desidério - Bahia',
        TRUE,
        4
    ),
    (
        'Prêmio Michel Le Bret de Espeleologia',
        TRUE,
        4
    ),
    (
        'As Cavernas de Ibitipoca',
        TRUE,
        4
    ),
    (
        'O Carste em rochas carbonáticas pré-cambrianas dos grupos Ceará e Frecheirinha',
        TRUE,
        4
    ),
    (
        'Vivências 3D: Uma imersão em realidade virtual no Parque Nacional Cavernas do Peruaçu e Furna Feia',
        TRUE,
        4
    ),
    (
        'Livro "O Carste Potiguar"',
        TRUE,
        4
    ),
    (
        'Segurança, Prevenção de Acidentes e Primeiros Socorros em Cavidades Naturais Subterrâneas e Áreas Remotas',
        TRUE,
        4
    ),
    (
        'Mapeamento de Feições cársticas hidrofuncionais na APA Nascente do Rio Vermelho',
        TRUE,
        4
    ),
    (
        'Edital de Conservação do Patrimônio Espeleológico em Unidades de Conservação',
        TRUE,
        4
    ),
    (
        'Investigando o Patrimônio Espeleológico no Mosáico do Espinhaço',
        TRUE,
        4
    ),
    (
        'Manejando o Patrimônio Espeleológico do Parque Estadual de Ibitipoca',
        TRUE,
        4
    ),
    (
        'Avaliação do potencial espeleoturístico das principais cavidades do Parque Estadual do Itacolomi (PEIT)',
        TRUE,
        4
    ),
    (
        'Cavidades ferríferas de Carajás: Plano de Manejo Espeleológico como instrumento de conservação e valorização dos seus patrimônios',
        TRUE,
        4
    ),
    (
        'Desvendando uma potencial nova espécie de morcego nectarívoro (Lonchophyllinae) das cavernas de Carajás: um estudo sobre história natural, genética, filogenia e distribuição',
        TRUE,
        4
    ),
    (
        'Identificação e mapeamento topográfico de cavidades presentes no Parque Estadual do Itacolomi (PEIT)',
        TRUE,
        4
    ),
    (
        'Diagnóstico Ambiental Espeleológico Monumento Natural Estadual Gruta Rei do Mato',
        TRUE,
        4
    ),
    (
        'Avaliação de contaminação das águas por agroquímicos e metais e sua relação com a proteção do Patrimônio Espeleológico na APA das Nascentes do Rio Vermelho',
        TRUE,
        4
    ),
    (
        'Planejamento e Desenvolvimento de Ações para valorização do Patrimônio Natural e Cultural da Unidade de Conservação Municipal Monumento Natural Cárstico de Brejo do Amparo/Januária - Minas Gerais',
        TRUE,
        4
    ),
    (
        'Patrimônio Espeleológico da APA Carste de Lagoa Santa',
        TRUE,
        4
    ),
    (
        'Inventário e Diagnóstico do Patrimônio Espeleológico do Refúgio de Vida Silvestre Libélulas da Serra de José e Área de Proteção Ambiental São José',
        TRUE,
        4
    ),
    (
        'Fortalecimento da gestão e da utilização sustentável do patrimônio espeleológico do Parque Nacional da Furna Feia',
        TRUE,
        4
    ),
    (
        'Ações de Conservação do Patrimônio Espeleológico na UC Parque Nacional de Ubajara',
        TRUE,
        4
    ),
    (
        'Ordenamento turístico para conservação do patrimônio espeleológico em UC Federais dos Estados de Sergipe, Bahia e Alagoas',
        TRUE,
        4
    ),
    (
        'Inventário de Fungos em cavernas de UCs de biomas brasileiros: diversidade e subsídios para manejo espeleológico',
        TRUE,
        4
    ),
    (
        'Revitalização da estrutura de apoio à visitação do Lajedo de Soledade, Apodi/RN',
        TRUE,
        4
    ),
    (
        'Publicação e Divulgação da obra Aves do Parque Nacional da Furna Feia',
        TRUE,
        4
    ),
    (
        'Plano de Ação Nacional Cavernas do Brasil',
        TRUE,
        4
    ),
    (
        'Fauna associada às cavernas granitoides na Mata Atlântica do Nordeste de Minas e Espírito Santo: inventário faunístico, ecologia e avaliação de impactos como subsídios à conservação destes ambientes negligenciados',
        TRUE,
        4
    ),
    (
        'Inventário e Abordagens Ecológico-Evolutivas de Peixes Subterrâneos dos Estados de Goiás e Bahia',
        TRUE,
        4
    ),
    (
        'Descobrindo o novo mundo e as dolinas de barbosilândia: Aracnídeos cavernícolas da região de APA Nascentes do Rio Vermelho e Bacia do Rio Corrente',
        TRUE,
        4
    ),
    (
        'Ecos da Escuridão: Inventário integrativo da biodiversida subterrânea',
        TRUE,
        4
    ),
    (
        'Conservação de morcegos cavernícolas no Cerrado: biodiversidade, espécies ameaçadas e ações de proteção integradas',
        TRUE,
        4
    ),
    (
        'Realizar diagnóstico sobre o tratamento do patrimônio espeleológico no âmbito dos Estados da Federação, Distrito Federal e União nos processos de licenciamento, autorização e fiscalização',
        TRUE,
        4
    ),
    (
        'Articular junto ao IPHAN a elaboração de um fluxograma para a avaliação da existência do atributo "destacada relevância histórico-cultural ou religiosa" em cavidades naturais subterrâneas',
        TRUE,
        4
    ),
    (
        'Definição de diretrizes para a prospecção espelológica em processos de licenciamento ambiental',
        TRUE,
        4
    ),
    (
        'Integração de sistemas de alerta de desmatamento em regiões de interesse espeleológico para fins de controle, monitoramento e fiscalização ambiental',
        TRUE,
        4
    ),
    (
        'Cursos sobre práticas de Conservação, Redução de Impactos e Recuperação de danos em cavernas turísticas',
        TRUE,
        4
    ),
    (
        'Articular e elaborar, em níveis estadual e federal, cursos de boas práticas de manejo de morcegos para agentes de controle agropecuário e de zoonoses',
        TRUE,
        4
    ),
    (
        'Caracterização do uso turístico das cavernas do Brasil',
        TRUE,
        4
    ),
    (
        'Analisar a efetividade das metodologias de avaliação de impacto de visitação em cavernas e divulgar os resultados obtidos',
        TRUE,
        4
    ),
    (
        'Elaboração de diretrizes para capacitação de agentes de espeleoturismo',
        TRUE,
        4
    ),
    (
        'Elaborar um manual de boas práticas de uso turístico, desportivo, educativo e cultural em cavernas com sítios arqueológicos',
        TRUE,
        4
    ),
    (
        'Realizar ações para divulgação do conhecimento sobre o patrimônio espeleológico para o público geral do PAN Cavernas do Brasil',
        TRUE,
        4
    ),
    (
        'Realizar inventário de morcegos nas áreas identificadas',
        TRUE,
        4
    ),
    (
        'Sítios de monitoramento de longo prazo em cavernas, focado em espécies alvo do PAN',
        TRUE,
        4
    ),
    (
        'Gerar e aprimorar informações essenciais para o processo de classificação das espécies cavernícolas alvo e ameaçadas de extinção (atendendo aos critérios da IUCN)',
        TRUE,
        4
    ),
    (
        'Testar a viabilidade do uso de portões (Bat gates) para cavernas no Brasil',
        TRUE,
        4
    ),
    (
        'Geoespacialização de sítios arqueológicos no contexto do patrimônio espeleológico brasileiro',
        TRUE,
        4
    ),
    (
        'Elaborar e manter listas atualizadas de cavernas com ocorrência de espécies cavernícolas ameaçadas de extinção, de troglobios raros e batcaves.',
        TRUE,
        4
    ),
    (
        'Fomentar a realização de Congressos, Simpósios ou outros eventos científicos em Espeleologia, em nível nacional ou internacional.',
        TRUE,
        4
    ),
    (
        'Grupos Regionais de Espeleologia no Multiverso Espeleológico',
        TRUE,
        4
    ),
    (
        'Projeto CLPI Peruaçu',
        TRUE,
        4
    ),
    ('III SCIVAPE', TRUE, 4),
    (
        'II Café Espeleológico: Conectividade hídrica e biológica em cavidades naturais - desafios científicos e legais',
        TRUE,
        4
    ),
    (
        'VIII Encontro Pernambucano de Micologia - Funga Nordestina em Expansão: Ciência, Cultura e Conservação',
        TRUE,
        4
    ),
    (
        'IV Seminário Científico de Pesquisas do Vale do Rio Peruaçu - SCIVAPE',
        TRUE,
        4
    ),
    (
        'XII Encontro Brasileiro de Estudo de Quirópteros (EBEQ)',
        TRUE,
        4
    ),
    (
        'Seminário APA Morro da Pedreira',
        TRUE,
        4
    ),
    (
        'Sociedade Excursionista e Espeleológica: 90 Anos de Exploração e Descobertas',
        TRUE,
        4
    ),
    (
        'Oficina do curso "Tutela Jurídica de Cavernas e Espeleologia Básica"',
        TRUE,
        4
    ),
    (
        '2ª Edição do curso de "Tutela Jurídica em Cavernas e Introdução à Espeleologia"',
        TRUE,
        4
    ),
    (
        'Realizar expedições para coleta de material genético de espécies cavernícolas no âmbito do projeto GBB (Genômica da Biodiversidade Brasileira)',
        TRUE,
        4
    ),
    (
        'Plano Integrado de melhoria do uso do solo para conservação do patrimônio espeleológico e da sociobiodiversidade em ambientes cársticos',
        TRUE,
        4
    ),
    (
        'Prospecção Espeleológica em áreas prioritárias para conservação do patrimônio Espeleológico Brasileiro',
        TRUE,
        4
    ),
    (
        'Arapongas: Uma nova fronteira de exploração no Vale do Ribeira',
        TRUE,
        4
    ),
    (
        'Dolinas de Barbosilândia - Descobrir para preservar o Patrimônio Espeleológico Goiano',
        TRUE,
        4
    ),
    (
        'Do Vale do Rio Gameleira ao Mundo Novo - Conexões Espeleológicas do Nordeste Goiano',
        TRUE,
        4
    ),
    (
        'Atualização e Adequação do Cadastro das Informações Espeleológica do Município Doutor Ulysses - PR',
        TRUE,
        4
    ),
    (
        'Levantamento Espeleológico na região do Ribeirão do Farto - Núcleo Caboclos do Parque Estadual Turístico do Alto Ribeira - SP',
        TRUE,
        4
    ),
    (
        'Projeto de Prospecção Espelológica Subaquática Iraquara/Bahia',
        TRUE,
        4
    ),
    (
        'Prospecção, exploração e mapeamento espeleológico na região compreendida entre o Parque Nacional da Serra do Cipó e Parque Natural Municipal Alto do Rio do Tanque, nos municípios de Itabira, Jaboticatubas, Itambé do Mato Dentro e Nova União, Minas Gerais',
        TRUE,
        4
    ),
    (
        'Amapá Espeleológico: Prospecção e Topografia de Cavidades Naturais nas Microrregiões do Oiapoque e Mazagão - AP',
        TRUE,
        4
    ),
    (
        'EspeleoPG: Prospecção espeleológica e educação patrimonial no município de Ponta Grossa, Paraná',
        TRUE,
        4
    ),
    (
        'Levantamento Espeleológico na Região do Lajedo - Iporanga - São Paulo',
        TRUE,
        4
    ),
    (
        'Edital de Chamamento Público para seleção de projetos de pesquisa sobre o patrimônio espeleológico (Edital)',
        TRUE,
        4
    ),
    (
        'Diversidade, distribuição e evolução de troglomorfismo em aranhas cavernícolas brasileiras (Araneae: Pholcidae, Trechaleidae)',
        TRUE,
        4
    ),
    (
        'Estado da arte dos escorpiões cavernícolas brasileiros',
        TRUE,
        4
    ),
    (
        'Da Caatinga a Mata Atlântica: diversificação e conservação dos esquizomideos do gênero Rowlandius (Schizomida: Hubardiidae) através de dados genômicos, ecológicos e morfológicos',
        TRUE,
        4
    ),
    (
        'Singularidade ecológica e biodiversidade zooplanctônica em ambientes subterrâneos do semiárido',
        TRUE,
        4
    ),
    (
        'Identidades Faunísticas em cavernas da região central do estado da Bahia: a importância de elementos da paisagem e fatores ambientais intrínsecos na definição de prioridades de conservação',
        TRUE,
        4
    ),
    (
        'Explorando as Cavernas do Rio Grande do Norte: Conservação, Pesquisa e Divulgação do Patrimônio Espeleológico no Museus Câmara Cascudo/UFRN',
        TRUE,
        4
    ),
    (
        'Reconhecimento de Sítios Arqueológicos no Vale do Rio Peruaçu',
        TRUE,
        4
    ),
    (
        'Preenchendo lacunas de conhecimento taxonômico em cavernas brasileiras: descrição de novas espécies de Isopoda, Amphipoda, Pseudoscorpiones e Orthoptera',
        TRUE,
        4
    ),
    (
        'Bioprospecção de fungos isolados em cavernas brasileiras: conhecer, explorar e preservar',
        TRUE,
        4
    ),
    (
        'Um olhar para o Passado: Oscilações Paleoclimáticas Explicam os Potenciais Berçários de Troglofauna do Brasil',
        TRUE,
        4
    ),
    (
        'Um tesouro inexplorado da Serra do Espinhaço Meridional: levantamento taxonômico e uso sustentável de fungos cavernícolas',
        TRUE,
        4
    ),
    (
        'A piaba branca Stygichthys typhlops Britta & Bohlke 1965 do Norte de Minas Gerais: ampliando o conhecimento e a divulgação de uma peixe emblemático e ameaçado de águas subterrâneas brasileiras',
        TRUE,
        4
    ),
    (
        'Diversidade escondida: Taxonomia, sistemática morfológica e molecular, história natural e conservação de vermes-de-veludo (Onychophora) da Serra da Bodoquena',
        TRUE,
        4
    ),
    (
        'Comunicação e Educação Ambiental para a conservação do patrimônio Espeleológico',
        TRUE,
        4
    ),
    (
        'Caracterização e regionalização dos terrenos cársticos, em rochas carbonáticas, no Estado da Bahia',
        TRUE,
        3
    ),
    (
        'Edição do Curso de Espeleologia e Licenciamento Ambiental do Instituto Chico Mendes',
        TRUE,
        3
    ),
    (
        'Análise de metodologias para definição de relevância e impactos sobre a fauna subterrânea',
        TRUE,
        3
    ),
    (
        'Repositório institucional de publicações técnicas e científicas do Instituto Chico Mendes',
        TRUE,
        3
    ),
    (
        'Introdução às práticas de conservação e recuperação ambiental em cavernas turísticas',
        TRUE,
        3
    ),
    (
        'Implementação dos planos de manejo espeleológicos das grutas do castelo e lapão',
        TRUE,
        3
    ),
    (
        'Articulação CANIE, SISBIO e CNC (Sprints/Aplicativo para catalogação de cavernas)',
        TRUE,
        3
    ),
    (
        'Modelagem 3D de cavidades naturais subterrâneas',
        TRUE,
        3
    ),
    (
        'Ampliação da pesquisa e conservação do patrimônio espeleológico no Nordeste brasileiro',
        TRUE,
        3
    ),
    (
        'Ampliação da Pesquisa e Conservação de Morcegos Brasileiros',
        TRUE,
        3
    ),
    (
        'Divulgação de material audiovisual sobre as cavernas e os ambientes cársticos do Brasil',
        TRUE,
        3
    ),
    (
        'Implantação do turismo espeleológico no Parque Nacional da Furna Feia/RN',
        TRUE,
        3
    ),
    ('Pró-Cavernas', TRUE, 3),
    (
        'Prospecção e topografia de cavernas na porção norte da Serra de Baldim',
        TRUE,
        3
    ),
    (
        'Atualização e adequação do cadastro das informações espeleológicas do município de Rio Branco do Sul - PR',
        TRUE,
        3
    ),
    (
        'Vale do Rio Gameleira – Redescobertas Espeleológicas no P.A. Gameleira e Entorno – Flores de Goiás/GO',
        TRUE,
        3
    ),
    (
        'CAVERNAS DA SERRA NEGRA: Prospecção, exploração, topografia, mapeamento, levantamento faunístico e avaliação arqueológica das cavidades naturais do Parque Estadual da Serra Negra da Mantiqueira, MG, e áreas do entorno',
        TRUE,
        3
    ),
    (
        'Topografia e cadastro das Grutas: Barrigudas, Urubus, Salitre e Xiranha, Localizadas no Morro das Araras – Ituaçu-Bahia',
        TRUE,
        3
    ),
    (
        'O GRANDE ROTEIRO DE PETER LUND – PART II: As cavernas não visitadas por Lund, porém reveladas pelo projeto',
        TRUE,
        3
    ),
    (
        'Prospecção e mapeamento de cavernas na Serra do Itaqueri – SP',
        TRUE,
        3
    ),
    (
        'Cursos de capacitação para guias e condutores em espeleoturismo',
        TRUE,
        3
    ),
    (
        'Além dos condutos: popularização e divulgação da ciência espeleológica',
        TRUE,
        5
    ),
    (
        'Revisão do Plano de Manejo da Área de Proteção Ambiental Carste de Lagoa Santa',
        TRUE,
        5
    ),
    (
        'Recifes de coral - as Cavernas Submarinas do Nordeste do Brasil',
        TRUE,
        5
    ),
    (
        'Gerenciamento de dados dos Planos de Ação para a Conservação das Espécies Ameaçadas de Extinção',
        TRUE,
        5
    ),
    (
        'Sistema Nacional de Anilhamento de Aves e Morcegos Silvestres',
        TRUE,
        5
    ),
    (
        'Ampliação das ações de divulgação, pesquisa e conservação do patrimônio espeleológico nos estados da Bahia e Rio Grande do Norte',
        TRUE,
        5
    ),
    (
        'Fortalecimento Operacional e Capacitação da Seção de Espeleorresgate da Sociedade Brasileira de Espeleologia',
        TRUE,
        5
    ),
    (
        'Sounds in cave: Descobrindo a ecoacústica em cavernas do Semiárido',
        TRUE,
        5
    ),
    (
        'Filogeografia de colêmbolos cavernícolas na Caatinga',
        TRUE,
        5
    ),
    (
        'GAP - Gestão Administrativa dos Projetos e ações necessários para viabilização e implementação das compensações espeleológicas',
        TRUE,
        5
    ),
    (
        'Implementação de ações do PAN Cavernas do Brasil',
        TRUE,
        5
    ),
    (
        'Conservação e gestão do patrimônio espeleológico brasileiro e a ocupação pré-colonial do planalto central a partir do sítio arqueológico GO-Ja-02, Serranópolis, Goiás',
        TRUE,
        5
    ),
    (
        'Reconstituição paleoclimática desde o Último Máximo Glacial da região Nordeste do Brasil utilizando estalagmites',
        TRUE,
        5
    ),
    (
        'Programa de Apoio ao Turismo de Base Comunitária em Unidades de Conservação federais com Cavidades Naturais Subterrâneas e Áreas Cársticas',
        TRUE,
        5
    ),
    (
        'Caixa de Pedra: Resgate e inserção da comunidade Montana na Rota Turística do Parque Naional da Furna Feia',
        TRUE,
        5
    ),
    ('Casa de Memória', TRUE, 5),
    ('Projeto Geoaves 2', TRUE, 5),
    (
        'Raízes e Trilhas: Fortalecimento do Turismo de Base Comunitária em Ubajara',
        TRUE,
        5
    ),
    (
        'Catálogo Integrado das Trilhas, Cavernas, natureza e Pontos Turísticos dos Municípios Maturéia, Mãe d’água, Teixeira, São José do Bonfim e Imaculada, integrantes do PARNA SERRA DO TEIXEIRA',
        TRUE,
        5
    ),
    (
        'Cuidar do Sagrado: Sítios arqueológicos ancestrais Kapinawá',
        TRUE,
        5
    ),
    (
        'Mapeamento Genético e Morfológico De Collembola (Hexapoda) Cavernícolas do Brasil',
        TRUE,
        5
    ),
    (
        'Fortalecimento estratégico da comunicação institucional e científica do ICMBIo',
        TRUE,
        5
    ),
    (
        'Apoio à Implantação do Centro de Referência em Espeleologia',
        TRUE,
        5
    ),
    (
        'CECAV 30 Anos – Fortalecimento Institucional e Gestão da Conservação do Patrimônio Espeleológico',
        TRUE,
        5
    )
ON CONFLICT DO NOTHING;

INSERT INTO
    repositorio_tipodocumento (id, nome, ativo)
VALUES (1, 'LIVROS', TRUE),
    (2, 'VÍDEOS', TRUE),
    (
        3,
        'RELATÓRIO TÉCNICO FINAL',
        TRUE
    ),
    (
        4,
        'DOCUMENTOS TÉCNICOS',
        TRUE
    ),
    (
        5,
        'PUBLICAÇÃO CIENTÍFICA (ARTIGOS)',
        TRUE
    ),
    (
        6,
        'PUBLICAÇÃO CIENTÍFICA (TRABALHOS ACADÊMICOS)',
        TRUE
    ),
    (
        7,
        'MATERIAL EDUCATIVO (CARTILHA)',
        TRUE
    ),
    (
        8,
        'MATERIAL EDUCATIVO (PÔSTER/FOLDER)',
        TRUE
    ),
    (
        9,
        'MATERIAL EDUCATIVO (OUTROS)',
        TRUE
    )
ON CONFLICT (id) DO NOTHING;

INSERT INTO
    repositorio_autor (id, nome, lattes_id, ativo)
VALUES (
        1,
        'ABEL PÉREZ-GONZÁLEZ',
        null,
        TRUE
    ),
    (
        2,
        'ADIVANE MORAIS NOGUEIRA',
        null,
        TRUE
    ),
    (
        3,
        'ADRIÁ BRAUN VIEIRA',
        null,
        TRUE
    ),
    (
        4,
        'ADRIANA ARIAS-AGUILAR',
        null,
        TRUE
    ),
    (
        5,
        'ADRIANA MARIA COIMBRA HORBE',
        null,
        TRUE
    ),
    (
        6,
        'AFFONSO CELSO GONÇALVES JÚNIOR',
        null,
        TRUE
    ),
    (
        7,
        'AFONSO HENRIQUE KREMPNER DE SOUSA',
        null,
        TRUE
    ),
    (
        8,
        'ALBERT DAVID DITCHFIEL',
        null,
        TRUE
    ),
    (
        9,
        'ALEJANDRO OCEGUERA FIGUEROA',
        null,
        TRUE
    ),
    (
        10,
        'ALESSANDRA A. P. BUENO',
        null,
        TRUE
    ),
    (
        11,
        'ALESSANDRO FABIANO DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        12,
        'ALEXANDRE BONESSO SAMPAIO',
        null,
        TRUE
    ),
    (
        13,
        'ALEXANDRE CUNHA RIBEIRO',
        null,
        TRUE
    ),
    (
        14,
        'ALEXANDRE LOBO',
        null,
        TRUE
    ),
    (
        15,
        'ALICIA HELENA SOUZA RODRIGUES FERREIRA',
        null,
        TRUE
    ),
    (
        16,
        'ALINE MARCELE GHILARDI',
        null,
        TRUE
    ),
    (
        17,
        'ALLAN SILAS CALUX',
        null,
        TRUE
    ),
    (
        18,
        'ALLINE SOUZA PULCINI',
        null,
        TRUE
    ),
    (
        19,
        'ALLYSSON MOURA LUZ',
        null,
        TRUE
    ),
    (
        20,
        'AMANDA CECÍLIA NEUHAUSS AGUIAR',
        null,
        TRUE
    ),
    (
        21,
        'AMANDA JANAÍNA GONSATTI FEITOSA',
        null,
        TRUE
    ),
    (
        22,
        'AMANDA MAIA DA SILVA',
        null,
        TRUE
    ),
    (
        23,
        'AMANDA MIRANDA MICELLI',
        null,
        TRUE
    ),
    (
        24,
        'AMAZONAS CHAGAS JÚNIOR',
        null,
        TRUE
    ),
    (25, 'ANA ANTUNES', null, TRUE),
    (
        26,
        'ANA BEATRIZ ALENCASTRE SANTOS',
        null,
        TRUE
    ),
    (
        27,
        'ANA CAMILA DA SILVA',
        null,
        TRUE
    ),
    (
        28,
        'ANA ELIZA MEDEIROS CÂNDIDO',
        null,
        TRUE
    ),
    (
        29,
        'ANA FLÁVIA LEÃO',
        null,
        TRUE
    ),
    (
        30,
        'ANA KAROLINA SANTOS SILVA',
        null,
        TRUE
    ),
    (
        31,
        'ANA LAURA MORAIS',
        null,
        TRUE
    ),
    (
        32,
        'ANA LEAL-ZANCHET',
        null,
        TRUE
    ),
    (
        33,
        'ANA MARIA LEAL ZANCHET',
        null,
        TRUE
    ),
    (
        34,
        'ANDRÉ CARLOS SILVA',
        null,
        TRUE
    ),
    (
        35,
        'ANDRÉ DE SOUZA AVELAR',
        null,
        TRUE
    ),
    (
        36,
        'ANDRÉ GOMIDE VASCONCELOS',
        null,
        TRUE
    ),
    (
        37,
        'ANDRÉ LUÍS BRASIL CAVALCANTE',
        null,
        TRUE
    ),
    (
        38,
        'ANDRÉ LUIZ HENRIQUES ESGUÍCERO',
        null,
        TRUE
    ),
    (
        39,
        'ANDRÉ MENEZES STRAUSS',
        null,
        TRUE
    ),
    (
        40,
        'ANDRÉ OLIVEIRA SAWAKUCHI',
        null,
        TRUE
    ),
    (
        41,
        'ANDRÉ SILVA TAVARES',
        null,
        TRUE
    ),
    (
        42,
        'ANDRÉIA DE ALMEIDA',
        null,
        TRUE
    ),
    (
        43,
        'ANGELE MARTINS',
        null,
        TRUE
    ),
    (
        44,
        'ANNA CECILIA BATISTA MAIA',
        null,
        TRUE
    ),
    (
        45,
        'ANNA SABRINA VIDAL DE SOUZA',
        null,
        TRUE
    ),
    (
        46,
        'ANTÔNIO CALAZANS REIS MIRANDA',
        null,
        TRUE
    ),
    (
        47,
        'ANTÔNIO D. BRESCOVIT',
        null,
        TRUE
    ),
    (
        48,
        'ANTÔNIO WESLEY BARROS CAÇADOR',
        null,
        TRUE
    ),
    (
        49,
        'APARECIDA CLÉBIA DA SILVA',
        null,
        TRUE
    ),
    (
        50,
        'ARIADNE F. SABBAG',
        null,
        TRUE
    ),
    (
        51,
        'ARIANE DE SOUSA BRASIL',
        null,
        TRUE
    ),
    (
        52,
        'AUGUSTO SARREIRO AULER',
        null,
        TRUE
    ),
    (
        53,
        'BÁRBARA COSTA',
        null,
        TRUE
    ),
    (
        54,
        'BEATRIZ DYBAS NATIVIDADE',
        null,
        TRUE
    ),
    (
        55,
        'BEATRIZ MARCELINO DOS SANTOS',
        null,
        TRUE
    ),
    (
        56,
        'BIANCA CLARO MAFRA OLIVEIRA',
        null,
        TRUE
    ),
    (
        57,
        'BRENDA ALMEIDA LIMA',
        null,
        TRUE
    ),
    (
        58,
        'BRENDA K. GOMES ALMEIDA',
        null,
        TRUE
    ),
    (
        59,
        'BRENO MELLADO',
        null,
        TRUE
    ),
    (
        60,
        'BRUNA C. H. LOPES',
        null,
        TRUE
    ),
    (
        61,
        'BRUNA NASCIMENTO DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        62,
        'BRUNO DA SILVA BRANDÃO GONÇALVES',
        null,
        TRUE
    ),
    (
        63,
        'BRUNO E.TÁVORA',
        null,
        TRUE
    ),
    (
        64,
        'CAIO CAVALCANTE DA SOUZA MOTA',
        null,
        TRUE
    ),
    (
        65,
        'CAMILA DE OLIVEIRA CASTRO',
        null,
        TRUE
    ),
    (
        66,
        'CAMILA ESTEFANY ALVES MOTA',
        null,
        TRUE
    ),
    (
        67,
        'CAMILA VOGT DOS SANTOS',
        null,
        TRUE
    ),
    (
        68,
        'CARLO M. CUNHA',
        null,
        TRUE
    ),
    (
        69,
        'CARLOS FREDERICO DE SOUZA LOTT',
        null,
        TRUE
    ),
    (
        70,
        'CARLOS GLEIDSON CAMPOS DA PURIFICAÇÃO',
        null,
        TRUE
    ),
    (
        71,
        'CARLOS MARIO LÓPEZ OROZCO',
        null,
        TRUE
    ),
    (
        72,
        'CARLOS TADEU CARVALHO DO NASCIMENTO',
        null,
        TRUE
    ),
    (
        73,
        'CAROLINA TEIXEIRA PUPPIN GONÇALVES',
        null,
        TRUE
    ),
    (
        74,
        'CAROLINE FERREIRA',
        null,
        TRUE
    ),
    (
        75,
        'CAROLINE FERREIRA LIMA',
        null,
        TRUE
    ),
    (
        76,
        'CECÍLIA VOLKMER RIBEIRO',
        null,
        TRUE
    ),
    (
        77,
        'CECÍLIA YUKI GOMES DE SÁ',
        null,
        TRUE
    ),
    (
        78,
        'CELIA C. C. MACHADO',
        null,
        TRUE
    ),
    (
        79,
        'CELINE CECÍLIA ALEXANDRE DA SILVA',
        null,
        TRUE
    ),
    (
        80,
        'CÉLIO MAGALHÃES',
        null,
        TRUE
    ),
    (
        81,
        'CÉSAR AUGUSTO MOREIRA',
        null,
        TRUE
    ),
    (
        82,
        'CESAR ULISSES VIEIRA VERISSIMO',
        null,
        TRUE
    ),
    (
        83,
        'CHRISSANDRO MARQUES DE ALMEIDA',
        null,
        TRUE
    ),
    (
        84,
        'CÍCERO L. SILVA',
        null,
        TRUE
    ),
    (
        85,
        'CÍNTIA FERNANDA DA COSTA',
        null,
        TRUE
    ),
    (
        86,
        'CLAUDE LUIZ AGUILAR SANTOS',
        null,
        TRUE
    ),
    (
        87,
        'CLAUDIA COSTA BONECKER',
        null,
        TRUE
    ),
    (
        88,
        'CLAUDIA REGINA SILVA',
        null,
        TRUE
    ),
    (
        89,
        'CLEUSA YOSHIKO NAGAMACHI',
        null,
        TRUE
    ),
    (
        90,
        'CRISTIANE MOURA',
        null,
        TRUE
    ),
    (
        91,
        'CRISTIANO FERNANDES FERREIRA',
        null,
        TRUE
    ),
    (
        92,
        'CRISTINA MARIA DE SOUZA MOTTA',
        null,
        TRUE
    ),
    (
        93,
        'CRISTOBAL CONDON',
        null,
        TRUE
    ),
    (
        94,
        'DAHIANA ARCILA',
        null,
        TRUE
    ),
    (
        95,
        'DAIANE F. MACIEL',
        null,
        TRUE
    ),
    (
        96,
        'DANDARA MARIA VITALINA DA SILVA CALDEIRA',
        null,
        TRUE
    ),
    (
        97,
        'DANIEL C. CAVALLARI',
        null,
        TRUE
    ),
    (
        98,
        'DANIEL DE STEFANO MENIN',
        null,
        TRUE
    ),
    (
        99,
        'DANIEL REIS MAIOLINO DE MENDONÇA',
        null,
        TRUE
    ),
    (
        100,
        'DANIELA CRISTINA FERREIRA',
        null,
        TRUE
    ),
    (
        101,
        'DANIELA DE MELO',
        null,
        TRUE
    ),
    (
        102,
        'DANIELA HOYOS BENJUMEA',
        null,
        TRUE
    ),
    (
        103,
        'DANIELE POLOTOW',
        null,
        TRUE
    ),
    (
        104,
        'DANIELLE KATHARINE PETSCH',
        null,
        TRUE
    ),
    (
        105,
        'DANIELLE R. G. RIBEIRO BRASIL',
        null,
        TRUE
    ),
    (
        106,
        'DANILO OLIVEIRA RAMOS',
        null,
        TRUE
    ),
    (
        107,
        'DAPHNE SOARES',
        null,
        TRUE
    ),
    (
        108,
        'DARCY JOSÉ DOS SANTOS',
        null,
        TRUE
    ),
    (
        109,
        'DARRYL GRANGER',
        null,
        TRUE
    ),
    (
        110,
        'DAVID C. CULVER',
        null,
        TRUE
    ),
    (
        111,
        'DAYANA FERREIRA TORRES',
        null,
        TRUE
    ),
    (
        112,
        'DAYANNE FERREIRA DOS SANTOS SIRQUEIRA',
        null,
        TRUE
    ),
    (
        113,
        'DEBORA MARINA BANDEIRA',
        null,
        TRUE
    ),
    (
        114,
        'DEBORAH LEE V.B.V. BERTOLINI',
        null,
        TRUE
    ),
    (
        115,
        'DENILSON MENDES DOS SANTOS',
        null,
        TRUE
    ),
    (
        116,
        'DERMEVAL APARECIDO DO CARMO',
        null,
        TRUE
    ),
    (
        117,
        'DEYVISON BONFIM RIBEIRO',
        null,
        TRUE
    ),
    (
        118,
        'DIANA J. K. ALMEIDA',
        null,
        TRUE
    ),
    (
        119,
        'DIEGO DE MEDEIROS BENTO',
        null,
        TRUE
    ),
    (
        120,
        'DIEGO MONTEIRO VON SCHIMONSKY',
        null,
        TRUE
    ),
    (
        121,
        'DIVA MARIA BORGES',
        null,
        TRUE
    ),
    (
        122,
        'DOUGLAS ZEPPELINI',
        null,
        TRUE
    ),
    (
        123,
        'DRIELLY SOUZA RODRIGUES',
        null,
        TRUE
    ),
    (
        124,
        'EDENILSON ROBERTO DO NASCIMENTO',
        null,
        TRUE
    ),
    (
        125,
        'ÉDER BARBIER',
        null,
        TRUE
    ),
    (
        126,
        'EDISON ZEFA',
        null,
        TRUE
    ),
    (
        127,
        'EDNA DE A. SILVA',
        null,
        TRUE
    ),
    (
        128,
        'EDUARDA SILVA DE LIMA',
        null,
        TRUE
    ),
    (
        129,
        'ELAINE MALOSSO',
        null,
        TRUE
    ),
    (
        130,
        'ELEONORA TRAJANO',
        null,
        TRUE
    ),
    (
        131,
        'ELIANE NUNES CHIM',
        null,
        TRUE
    ),
    (
        132,
        'ELIS R. FREIRE',
        null,
        TRUE
    ),
    (
        133,
        'EMILLY LETÍCIA SILVA',
        null,
        TRUE
    ),
    (
        134,
        'EMILY OLIVEIRA FONSECA',
        null,
        TRUE
    ),
    (
        135,
        'ENEIDA MARIA ESKINAZI-SANT''ANNA',
        null,
        TRUE
    ),
    (
        136,
        'ENRICO BERNARD',
        null,
        TRUE
    ),
    (
        137,
        'ERIC S. FORTUNE',
        null,
        TRUE
    ),
    (
        138,
        'ERICK SABOIA',
        null,
        TRUE
    ),
    (
        139,
        'ESTEVAM C.A. DE LIMA',
        null,
        TRUE
    ),
    (
        140,
        'ÉZIO LUIZ RUBBIOLI',
        null,
        TRUE
    ),
    (
        141,
        'FABIANA GISELE DA SILVA PINTO',
        null,
        TRUE
    ),
    (
        142,
        'FABIANO N. PUPIM',
        null,
        TRUE
    ),
    (
        143,
        'FABIANO PEREIRA SANTOS',
        null,
        TRUE
    ),
    (
        144,
        'FÁBIO ALEX CUSTÓDIO',
        null,
        TRUE
    ),
    (
        145,
        'FÁBIO AZEVEDO KHALED ABDEL RAHMAN',
        null,
        TRUE
    ),
    (
        146,
        'FABRÍCIA C. M. MOTA',
        null,
        TRUE
    ),
    (
        147,
        'FELIPE BAIA RODRIGUES',
        null,
        TRUE
    ),
    (
        148,
        'FELIPE FERRAZ FIGUEIREDO MOREIRA',
        null,
        TRUE
    ),
    (
        149,
        'FERNANDA ALEXANDRE SILVA',
        null,
        TRUE
    ),
    (
        150,
        'FERNANDA CARVALHO CALDEIRA',
        null,
        TRUE
    ),
    (
        151,
        'FERNANDA DOS SANTOS SILVA',
        null,
        TRUE
    ),
    (
        152,
        'FERNANDA LANDIM',
        null,
        TRUE
    ),
    (
        153,
        'FERNANDA S. SILVA',
        null,
        TRUE
    ),
    (
        154,
        'FERNANDO L. MANTELATTO',
        null,
        TRUE
    ),
    (
        155,
        'FERNANDO PACHECO RODRIGUES',
        null,
        TRUE
    ),
    (
        156,
        'FERNANDO VERASSANI LAUREANO',
        null,
        TRUE
    ),
    (
        157,
        'FLÁVIO SILVA RAMOS',
        null,
        TRUE
    ),
    (
        158,
        'FRANCISCO WESLEY DA SILVA DE NOJOSA',
        null,
        TRUE
    ),
    (
        159,
        'FRANCISCO WILLIAN DA CRUZ JÚNIOR',
        null,
        TRUE
    ),
    (
        160,
        'FREDERIC NGUYEN',
        null,
        TRUE
    ),
    (
        161,
        'FREDERICO DE SIQUEIRA NEVES',
        null,
        TRUE
    ),
    (
        162,
        'GABRIEL AUGUSTO SILVA VAZ',
        null,
        TRUE
    ),
    (
        163,
        'GABRIEL LOURENÇO CARVALHO DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        164,
        'GABRIEL LUCAS BOCHINI',
        null,
        TRUE
    ),
    (
        165,
        'GABRIEL S. ARINI',
        null,
        TRUE
    ),
    (
        166,
        'GABRIEL SANTOS DA SILVA',
        null,
        TRUE
    ),
    (
        167,
        'GABRIEL VASCONCELOS',
        null,
        TRUE
    ),
    (
        168,
        'GABRIELA CRESTANA RABELLO',
        null,
        TRUE
    ),
    (
        169,
        'GABRIELA DUARTE',
        null,
        TRUE
    ),
    (
        170,
        'GEORGE M. TALIAFERRO MATTOX',
        null,
        TRUE
    ),
    (
        171,
        'GEOVANA DE OLIVEIRA DA SILVA',
        null,
        TRUE
    ),
    (
        172,
        'GILSON ARGOLO',
        null,
        TRUE
    ),
    (
        173,
        'GILSON BURIGO GUIMARÃES',
        null,
        TRUE
    ),
    (
        174,
        'GIOVANA GUTSTEIN GNATA',
        null,
        TRUE
    ),
    (
        175,
        'GIOVANNA MONTICELLI CARDOSO',
        null,
        TRUE
    ),
    (
        176,
        'GISELE CRISTINA SESSEGOLO',
        null,
        TRUE
    ),
    (
        177,
        'GISELE OLIVEIRA SILVA',
        null,
        TRUE
    ),
    (
        178,
        'GIULY G. ITURRALDE',
        null,
        TRUE
    ),
    (
        179,
        'GLEYCE KELLY DOS SANTOS MELO',
        null,
        TRUE
    ),
    (
        180,
        'GUILHERME CARVALHO PRADO',
        null,
        TRUE
    ),
    (
        181,
        'GUILHERME OLIVEIRA',
        null,
        TRUE
    ),
    (
        182,
        'GUILHERME ZAKAREWICZ DE AGUIAR',
        null,
        TRUE
    ),
    (
        183,
        'GUSTAVO GRACIOLLI',
        null,
        TRUE
    ),
    (
        184,
        'GUSTAVO LIMA URBIETA',
        null,
        TRUE
    ),
    (
        185,
        'HANS BALDER HAVENITH',
        null,
        TRUE
    ),
    (
        186,
        'HARUAN STRAIOTO',
        null,
        TRUE
    ),
    (
        187,
        'HELENA SEIVANE',
        null,
        TRUE
    ),
    (
        188,
        'HENRIQUE MARINHO LEITE CHAVES',
        null,
        TRUE
    ),
    (
        189,
        'HERNAN MARTINEZ CARVAJAL',
        null,
        TRUE
    ),
    (190, 'HUANG', null, TRUE),
    (
        191,
        'IARA SIQUEIRA SANTOS SILVA',
        null,
        TRUE
    ),
    (
        192,
        'IGOR CIZAUKAS',
        null,
        TRUE
    ),
    (
        193,
        'ISABELA RESENDE',
        null,
        TRUE
    ),
    (
        194,
        'ISABELLE DA ROCHA SILVA CORDEIRO',
        null,
        TRUE
    ),
    (
        195,
        'ISSAC DANIEL RUDNITKI',
        null,
        TRUE
    ),
    (
        196,
        'ÍTALO MOREIRA MARTINS',
        null,
        TRUE
    ),
    (
        197,
        'IVAN BRAGA CAMPOS',
        null,
        TRUE
    ),
    (
        198,
        'IVANKLIN SOARES CAMPOS FILHO',
        null,
        TRUE
    ),
    (
        199,
        'IVES SIMÕES ARNONE',
        null,
        TRUE
    ),
    (
        200,
        'IVO KARMANN',
        null,
        TRUE
    ),
    (
        201,
        'JADSON DIOGO PEREIRA BEZERRA',
        null,
        TRUE
    ),
    (
        202,
        'JAMILY LORENA RAMOS DE LIMA',
        null,
        TRUE
    ),
    (
        203,
        'JAQUELINE APARECIDA DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        204,
        'JENNIFER B. DA SILVA',
        null,
        TRUE
    ),
    (
        205,
        'JEREMIE GARNIEW',
        null,
        TRUE
    ),
    (
        206,
        'JÉSSICA BARATA DA SILVA',
        null,
        TRUE
    ),
    (
        207,
        'JÉSSICA ROSSET',
        null,
        TRUE
    ),
    (
        208,
        'JÉSSICA SCAGLIONE GALLO',
        null,
        TRUE
    ),
    (
        209,
        'JHAVANA FERRO PALOMINO',
        null,
        TRUE
    ),
    (210, 'JIE DOU', null, TRUE),
    (
        211,
        'JOÃO BRACCINI',
        null,
        TRUE
    ),
    (
        212,
        'JOÃO GABRIEL CAVALCANTE VIEIRA',
        null,
        TRUE
    ),
    (
        213,
        'JOÃO LUCAS VITORIO RIBEIRO CARVALHO',
        null,
        TRUE
    ),
    (
        214,
        'JOÃO MARCELO TEIXEIRA',
        null,
        TRUE
    ),
    (
        215,
        'JOÃO PEDRO SANTIAGO GOULART',
        null,
        TRUE
    ),
    (
        216,
        'JOCY BRANDÃO CRUZ',
        null,
        TRUE
    ),
    (
        217,
        'JOENNY MARIA DA SILVEIRA DE LIMA',
        null,
        TRUE
    ),
    (
        218,
        'JONAS EDUARDO GALLÃO',
        null,
        TRUE
    ),
    (
        219,
        'JORDANE PIMENTEL NÓBREGA',
        null,
        TRUE
    ),
    (
        220,
        'JORGE DUARTE ROSÁRIO',
        null,
        TRUE
    ),
    (
        221,
        'JOSÉ AUGUSTO PIRES BITENCOURT',
        null,
        TRUE
    ),
    (
        222,
        'JOSÉ CARLOS RIBEIRO REINO',
        null,
        TRUE
    ),
    (
        223,
        'JOSÉ ELOI GUIMARÃES CAMPOS',
        null,
        TRUE
    ),
    (
        224,
        'JOSÉ FREDSON DA SILVA ALVES DOS PRAZERES',
        null,
        TRUE
    ),
    (
        225,
        'JOSÉ GUSTAVO DA SILVA NUNES',
        null,
        TRUE
    ),
    (
        226,
        'JOSÉ IATAGAN MENDES DE FREITAS',
        null,
        TRUE
    ),
    (
        227,
        'JOSÉ LUÍS PASSOS CORDEIRO',
        null,
        TRUE
    ),
    (
        228,
        'JOSÉ RASSO FELIX GUIMARÃES',
        null,
        TRUE
    ),
    (
        229,
        'JUAN C. DÍAZ-SANDOVAL',
        null,
        TRUE
    ),
    (
        230,
        'JÚLIA BARBOSA GALO',
        null,
        TRUE
    ),
    (
        231,
        'JÚLIA DE OLIVEIRA FRANÇA',
        null,
        TRUE
    ),
    (
        232,
        'JULIA RANDOW CAVALCANTI',
        null,
        TRUE
    ),
    (
        233,
        'JULIANA DEO DIAS',
        null,
        TRUE
    ),
    (
        234,
        'JULIO CESAR PIECZARKA',
        null,
        TRUE
    ),
    (
        235,
        'JÚLIO FERREIRA DA COSTA NETO',
        null,
        TRUE
    ),
    (
        236,
        'KAREM F.SOUSA',
        null,
        TRUE
    ),
    (
        237,
        'KARINA DIAS DA SILVA',
        null,
        TRUE
    ),
    (
        238,
        'KATHRYN GALLMAN',
        null,
        TRUE
    ),
    (
        239,
        'KENNED DA SILVA SOUSA',
        null,
        TRUE
    ),
    (
        240,
        'KESLEY GADELHA FERREIRA',
        null,
        TRUE
    ),
    (
        241,
        'KHURRAM ASLAM',
        null,
        TRUE
    ),
    (
        242,
        'KLEBER MAKOTO MISE',
        null,
        TRUE
    ),
    (
        243,
        'LAURA FERREIRA SANTOS',
        null,
        TRUE
    ),
    (
        244,
        'LEANDRA PEIXOTO NOLASCO SELOS',
        null,
        TRUE
    ),
    (
        245,
        'LEANDRA ROSE PALHETA',
        null,
        TRUE
    ),
    (
        246,
        'LEANDRO R. MONTEIRO',
        null,
        TRUE
    ),
    (247, 'LEDA ZOGBI', null, TRUE),
    (
        248,
        'LEILA APARECIDA SOUZA',
        null,
        TRUE
    ),
    (
        249,
        'LENIZE CALVÃO',
        null,
        TRUE
    ),
    (
        250,
        'LEO LINKE FERREIRA',
        null,
        TRUE
    ),
    (
        251,
        'LEONARDO CARREIRA TREVELIN',
        null,
        TRUE
    ),
    (
        252,
        'LEONARDO CHAVES MENDES',
        null,
        TRUE
    ),
    (
        253,
        'LEONARDO DE ASSIS',
        null,
        TRUE
    ),
    (
        254,
        'LEONARDO FORTES VIEIRA',
        null,
        TRUE
    ),
    (
        255,
        'LEONARDO P. A. RESENDE',
        null,
        TRUE
    ),
    (
        256,
        'LEONARDO SOUSA CARVALHO',
        null,
        TRUE
    ),
    (
        257,
        'LEONARDO TORTORIELLO MESSIAS',
        null,
        TRUE
    ),
    (
        258,
        'LETÍCIA AMARAL CARDOS0',
        null,
        TRUE
    ),
    (
        259,
        'LETÍCIA APARECIDA DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        260,
        'LETÍCIA LIMA CORREIA',
        null,
        TRUE
    ),
    (
        261,
        'LETÍCIA VIEIRA',
        null,
        TRUE
    ),
    (
        262,
        'LÍGIA MARIA SABACK MOREIRA DORNELLAS',
        null,
        TRUE
    ),
    (
        263,
        'LIGIER MODESTO BRAGA',
        null,
        TRUE
    ),
    (
        264,
        'LINDSEY HELLMANN',
        null,
        TRUE
    ),
    (
        265,
        'LISANDRA  BENÍTEZ ÁLVAREZ',
        null,
        TRUE
    ),
    (
        266,
        'LÍVIA MEDEIROS CORDEIRO',
        null,
        TRUE
    ),
    (
        267,
        'LORENA OLIVEIRA PIRES',
        null,
        TRUE
    ),
    (
        268,
        'LORENA SOUZA MIRANDA',
        null,
        TRUE
    ),
    (
        269,
        'LOYRIANE MOURA SOUSA',
        null,
        TRUE
    ),
    (
        270,
        'LUANA CRISTINA LOURENÇO GUIMARÃES',
        null,
        TRUE
    ),
    (
        271,
        'LUANA DE SOUZA',
        null,
        TRUE
    ),
    (
        272,
        'LUANA MARÇAL SORROCHE',
        null,
        TRUE
    ),
    (
        273,
        'LUCAS DE OLIVEIRA CARNEIRO',
        null,
        TRUE
    ),
    (
        274,
        'LUCAS GUIMARÃES DE SOUZA',
        null,
        TRUE
    ),
    (
        275,
        'LUCAS MENDES RABELO',
        null,
        TRUE
    ),
    (
        276,
        'LUCAS PADOAN DE SÁ GODINHO',
        null,
        TRUE
    ),
    (
        277,
        'LUCAS PEREIRA LEÃO',
        null,
        TRUE
    ),
    (
        278,
        'LUCIANA DE MENDOONÇA GALVÃO',
        null,
        TRUE
    ),
    (
        279,
        'LUCIANA DE RESENDE ALT',
        null,
        TRUE
    ),
    (
        280,
        'LUCIANA LAIBE SANTOS SILVA',
        null,
        TRUE
    ),
    (
        281,
        'LUCIANO EMERICH FARIA',
        null,
        TRUE
    ),
    (
        282,
        'LUCIANO JOSÉ ALVARENGA',
        null,
        TRUE
    ),
    (
        283,
        'LUCIANO SOARES DA CUNHA',
        null,
        TRUE
    ),
    (
        284,
        'LÚCIO MAURO DOARES FRAGA',
        null,
        TRUE
    ),
    (
        285,
        'LUCIO MAURO FRAGA',
        null,
        TRUE
    ),
    (
        286,
        'LUDMILA ROCHA PENONI',
        null,
        TRUE
    ),
    (
        287,
        'LUDMILLA MOURA DE SOUZA AGUIAR',
        null,
        TRUE
    ),
    (
        288,
        'LUIS BEETHOVEN PILÓ',
        null,
        TRUE
    ),
    (
        289,
        'LUIS C. STIEVANO',
        null,
        TRUE
    ),
    (
        290,
        'LUÍS G.F. SANCHEZ',
        null,
        TRUE
    ),
    (
        291,
        'LUIZ EDUARDO PANISSET TRAVASSOS',
        null,
        TRUE
    ),
    (
        292,
        'LUIZ F. SALEMI',
        null,
        TRUE
    ),
    (
        293,
        'LUIZA SANTOS REIS',
        null,
        TRUE
    ),
    (
        294,
        'MAGALI G. GARCIA',
        null,
        TRUE
    ),
    (
        295,
        'MAIARA BEATRIZ MENDES DA SILVA',
        null,
        TRUE
    ),
    (
        296,
        'MAIARA ZONIN',
        null,
        TRUE
    ),
    (
        297,
        'MANUEL DIMITRI DE ALIMEIDA GOMES',
        null,
        TRUE
    ),
    (
        298,
        'MANUELA FREIRA GALVÃO',
        null,
        TRUE
    ),
    (
        299,
        'MARCEL SANTOS DE ARAÚJO',
        null,
        TRUE
    ),
    (
        300,
        'MARCELO R. NOGUEIRA',
        null,
        TRUE
    ),
    (
        301,
        'MARCELO TAYLOR DE LIMA',
        null,
        TRUE
    ),
    (
        302,
        'MARCIANA LEANDRO DE LIMA',
        null,
        TRUE
    ),
    (
        303,
        'MARCIONE BRITO DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        304,
        'MARCONI SOUZA SILVA',
        null,
        TRUE
    ),
    (
        305,
        'MARCUS PAULO ALVES OLIVEIRA',
        null,
        TRUE
    ),
    (
        306,
        'MARCUS VINÍCIUS DA SILVA AGUA DUARTE',
        null,
        TRUE
    ),
    (
        307,
        'MARIA CATARINA MEGUMI KASUYA',
        null,
        TRUE
    ),
    (
        308,
        'MARIA DA CONCEIÇÃO TAVARES FRIGO',
        null,
        TRUE
    ),
    (
        309,
        'MARIA EDUARDA ALVES NUNES',
        null,
        TRUE
    ),
    (
        310,
        'MARIA ELINA BICHUETTE',
        null,
        TRUE
    ),
    (
        311,
        'MARIA FERNANDA CASTILHO ZANCHETA',
        null,
        TRUE
    ),
    (
        312,
        'MARIA FERNANDA TAVARES DE ARAÚJO',
        null,
        TRUE
    ),
    (
        313,
        'MARIA GIMENA CHAVES FITZGERALD',
        null,
        TRUE
    ),
    (
        314,
        'MARIA IDALETE LOPES SILVA',
        null,
        TRUE
    ),
    (
        315,
        'MARIA JOÃO RAMOS PEREIRA',
        null,
        TRUE
    ),
    (
        316,
        'MARIA PAULA PEREIRA',
        null,
        TRUE
    ),
    (
        317,
        'MARIA RITA SOUZA FONSECA',
        null,
        TRUE
    ),
    (
        318,
        'MARIA TAMARA C. FELIPE',
        null,
        TRUE
    ),
    (
        319,
        'MARINA VENDRAMINI RODRIGUES PEREIRA',
        null,
        TRUE
    ),
    (
        320,
        'MÁRIO B. B. SIQUEIRA',
        null,
        TRUE
    ),
    (
        321,
        'MARTA RIUTORT',
        null,
        TRUE
    ),
    (
        322,
        'MARTÍN CÁRDENAS SOTO',
        null,
        TRUE
    ),
    (
        323,
        'MATHEUS ARTHUR LÚCIO DA ROCHA',
        null,
        TRUE
    ),
    (
        324,
        'MATHEUS FERNANDES',
        null,
        TRUE
    ),
    (
        325,
        'MATHEUS SANTIAGO VIEIRA',
        null,
        TRUE
    ),
    (
        326,
        'MAURÍCIO CARLOS MARTINS DE ANDRADE',
        null,
        TRUE
    ),
    (
        327,
        'MAURO DE OLIVEIRA NETO',
        null,
        TRUE
    ),
    (
        328,
        'MAURO GOMES',
        null,
        TRUE
    ),
    (
        329,
        'MAYARA MARIA DE SOUZA',
        null,
        TRUE
    ),
    (
        330,
        'MAYARA PEREIRA',
        null,
        TRUE
    ),
    (
        331,
        'MELISSA RINCON SANDOVAL',
        null,
        TRUE
    ),
    (
        332,
        'MICHELINE CARVALHO SILVA',
        null,
        TRUE
    ),
    (
        333,
        'MILENA MELO DE  LIMA',
        null,
        TRUE
    ),
    (
        334,
        'MISAEL A. OLIVEIRA-NETO',
        null,
        TRUE
    ),
    (
        335,
        'NÁDIA M. C. SANTOS-CAVALCANTE',
        null,
        TRUE
    ),
    (
        336,
        'NARJARA TÉRCIA PIMENTAL',
        null,
        TRUE
    ),
    (
        337,
        'NATÁLIA N. KATO',
        null,
        TRUE
    ),
    (
        338,
        'NATHALIA KALUANA RODRIGUES DA COSTA',
        null,
        TRUE
    ),
    (
        339,
        'NATHALIA MARIA STOPPA',
        null,
        TRUE
    ),
    (
        340,
        'NEI ALVES GONDIM JÚNIOR',
        null,
        TRUE
    ),
    (
        341,
        'NELSON BAPTISTA DE O. R. COSTA',
        null,
        TRUE
    ),
    (
        342,
        'NELSON PADRON SANCHEZ',
        null,
        TRUE
    ),
    (
        343,
        'NEUCIR SZINWELSKI',
        null,
        TRUE
    ),
    (
        344,
        'NORBERTO P. LOPES',
        null,
        TRUE
    ),
    (
        345,
        'OLAVO AMANCIO DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        346,
        'OLIANE M. C. MAGALHÃES',
        null,
        TRUE
    ),
    (
        347,
        'OLINTO LIPARINI PEREIRA',
        null,
        TRUE
    ),
    (348, 'OMAR HAMZA', null, TRUE),
    (
        349,
        'ORIGILENE BEZERRA DANTAS',
        null,
        TRUE
    ),
    (
        350,
        'OSÉIAS MARTINS MAGALHÃES',
        null,
        TRUE
    ),
    (
        351,
        'PAMELA B. HART',
        null,
        TRUE
    ),
    (
        352,
        'PAMELA SILVEIRA COSTA',
        null,
        TRUE
    ),
    (
        353,
        'PAMELLA MOURA',
        null,
        TRUE
    ),
    (
        354,
        'PAOLLA GABRYELLE CAVALCANTE DE SOUZA',
        null,
        TRUE
    ),
    (
        355,
        'PATRÍCIA VIEIRA TIGO',
        null,
        TRUE
    ),
    (
        356,
        'PATRÍCIA X. A. SIMÃO',
        null,
        TRUE
    ),
    (
        357,
        'PATRÍCIO ADRIANO DA ROCHA',
        null,
        TRUE
    ),
    (
        358,
        'PAULA CABRAL ETEROVICK',
        null,
        TRUE
    ),
    (
        359,
        'PAULO CÉSAR REIS VENÂNCIO',
        null,
        TRUE
    ),
    (
        360,
        'PAULO DE MARCO JÚNIOR',
        null,
        TRUE
    ),
    (
        361,
        'PAULO DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        362,
        'PAULO EDUARDO AGUIAR SARAIVA CÂMARA',
        null,
        TRUE
    ),
    (
        363,
        'PAULO EDUARDO DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        364,
        'PAULO EDUARDO SANTOS LIMA',
        null,
        TRUE
    ),
    (
        365,
        'PAULO GALVÃO',
        null,
        TRUE
    ),
    (
        366,
        'PAULO HENRIQUE FERREIRA GALVÃO',
        null,
        TRUE
    ),
    (
        367,
        'PAULO HENRIQUE ROSADO ARENAS',
        null,
        TRUE
    ),
    (
        368,
        'PEDRO EDSON FACE MOURA',
        null,
        TRUE
    ),
    (
        369,
        'PEDRO GABRIEL LOPES DA SILVA',
        null,
        TRUE
    ),
    (
        370,
        'PEDRO GIOVÂNI DA SILVA',
        null,
        TRUE
    ),
    (
        371,
        'PEDRO HENRIQUE ASSUNÇÃO',
        null,
        TRUE
    ),
    (
        372,
        'PEDRO HENRIQUE FÉLIX DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        373,
        'PEDRO HENRIQUE MENDES CARVALHO',
        null,
        TRUE
    ),
    (
        374,
        'PEDRO P. RIZZATO',
        null,
        TRUE
    ),
    (
        375,
        'PEDRO RODRIGUES BUSANA',
        null,
        TRUE
    ),
    (
        376,
        'PEDRO T. S. NOGUEIRA',
        null,
        TRUE
    ),
    (
        377,
        'PRISCILA EMANUELA DE SOUZA',
        null,
        TRUE
    ),
    (378, 'QIANG YAO', null, TRUE),
    (
        379,
        'QIANGSHAN GAO',
        null,
        TRUE
    ),
    (
        380,
        'RAFAEL COSTA CARDOSO',
        null,
        TRUE
    ),
    (
        381,
        'RAFAEL DOS SANTOS SCHERER',
        null,
        TRUE
    ),
    (
        382,
        'RAFAEL OLIVEIRA SILVA',
        null,
        TRUE
    ),
    (
        383,
        'RAFAEL SCHERER',
        null,
        TRUE
    ),
    (
        384,
        'RAFAELA ALVES DE LIRA',
        null,
        TRUE
    ),
    (
        385,
        'RAFAELA BASTOS PEREIRA',
        null,
        TRUE
    ),
    (
        386,
        'RAFAELA JEMELY RODRIGUES ALEXANDRE',
        null,
        TRUE
    ),
    (
        387,
        'RAMERSON LUCAS FERREIRA AZEVEDO',
        null,
        TRUE
    ),
    (
        388,
        'RAPHAEL PARRA',
        null,
        TRUE
    ),
    (
        389,
        'RAPHAELLE SILVA DE ALMEIDA',
        null,
        TRUE
    ),
    (
        390,
        'RAYSSA KAROLINA FERREIRA',
        null,
        TRUE
    ),
    (
        391,
        'REGIANNE KELLY MOREIRA DA SILVA',
        null,
        TRUE
    ),
    (
        392,
        'REJANE ENNES CICERELLI',
        null,
        TRUE
    ),
    (
        393,
        'RENAN DO NASCIMENTO BARBOSA',
        null,
        TRUE
    ),
    (
        394,
        'RENAN SMITH LOUZADA',
        null,
        TRUE
    ),
    (
        395,
        'RENATA SANTOS MOMOLI',
        null,
        TRUE
    ),
    (
        396,
        'RENATO PRADO',
        null,
        TRUE
    ),
    (
        397,
        'RIANDRA FREITAS VAREJÃO',
        null,
        TRUE
    ),
    (
        398,
        'RICARDO BETANCUR',
        null,
        TRUE
    ),
    (
        399,
        'RICARDO BORJA ARRIETA',
        null,
        TRUE
    ),
    (
        400,
        'RICARDO GALENO FRAGA DE ARAÚJO PEREIRA',
        null,
        TRUE
    ),
    (
        401,
        'RICARDO ROBERTO SILVA',
        null,
        TRUE
    ),
    (
        402,
        'ROBERTA MAFRA FREITAS DA SILVA',
        null,
        TRUE
    ),
    (
        403,
        'RODRIGO ANTÔNIO CASTRO SOUZA',
        null,
        TRUE
    ),
    (
        404,
        'RODRIGO B. SALVADOR',
        null,
        TRUE
    ),
    (
        405,
        'RODRIGO CINTRA DA COSTA',
        null,
        TRUE
    ),
    (
        406,
        'RODRIGO ELIAS DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        407,
        'RODRIGO LOPES FERREIRA',
        null,
        TRUE
    ),
    (
        408,
        'RODRIGO S. BOUZAN',
        null,
        TRUE
    ),
    (
        409,
        'ROGER FAGNER RIBEIRO MELLO',
        null,
        TRUE
    ),
    (
        410,
        'ROGÉRIO BERTANI',
        null,
        TRUE
    ),
    (
        411,
        'ROGÉRIO ELIAS SOARES UAGODA',
        null,
        TRUE
    ),
    (
        412,
        'RONALD SLUYS',
        null,
        TRUE
    ),
    (
        413,
        'RONALDO LUIZ MINCATO',
        null,
        TRUE
    ),
    (
        414,
        'RUBSON PINHEIRO MAIA',
        null,
        TRUE
    ),
    (
        415,
        'SABRINA ALVES DA SILVA',
        null,
        TRUE
    ),
    (
        416,
        'SALU COELHO DA SILVA',
        null,
        TRUE
    ),
    (
        417,
        'SALVATORE MARTINO',
        null,
        TRUE
    ),
    (
        418,
        'SAMANTHA VALENTE DIAS',
        null,
        TRUE
    ),
    (
        419,
        'SANDY DOS SANTOS NASCIMENTO',
        null,
        TRUE
    ),
    (
        420,
        'SANTELMO VASCONCELOS',
        null,
        TRUE
    ),
    (
        421,
        'SELMA R. MAGGIOTTO',
        null,
        TRUE
    ),
    (
        422,
        'SERGEI I. GOLOVATCH',
        null,
        TRUE
    ),
    (
        423,
        'SERGIO KOIDE',
        null,
        TRUE
    ),
    (
        424,
        'SÉRGIO L. S. BUENO',
        null,
        TRUE
    ),
    (
        425,
        'SERGIO MAIA QUEIROZ LIMA',
        null,
        TRUE
    ),
    (
        426,
        'SÉRGIO MAIA QUEIROZ LIMA',
        null,
        TRUE
    ),
    (
        427,
        'SIMONE ALBINO PAES',
        null,
        TRUE
    ),
    (
        428,
        'SIMONE ALMEIDA PENA',
        null,
        TRUE
    ),
    (
        429,
        'SORAYA DE CARVALHO NEVES',
        null,
        TRUE
    ),
    (
        430,
        'SUSANNE MACIEL',
        null,
        TRUE
    ),
    (
        431,
        'TAMIRES ZEPON',
        null,
        TRUE
    ),
    (
        432,
        'TANJA PIPAN',
        null,
        TRUE
    ),
    (
        433,
        'TARSILA CARVALHO DE JESUS',
        null,
        TRUE
    ),
    (
        434,
        'THADEU SOBRAL SOUZA',
        null,
        TRUE
    ),
    (
        435,
        'THAIRIK MATEUS SILVA MARQUES',
        null,
        TRUE
    ),
    (
        436,
        'THAÍS GIOVANNI PELEGRINI',
        null,
        TRUE
    ),
    (
        437,
        'THALIA R. DA SILVA',
        null,
        TRUE
    ),
    (
        438,
        'THAMYRES OLIVEIRA DOS SANTOS',
        null,
        TRUE
    ),
    (
        439,
        'THAYSE CRISTINE MELO BENATHAR',
        null,
        TRUE
    ),
    (
        440,
        'THIAGO BERNARDI VIEIRA',
        null,
        TRUE
    ),
    (
        441,
        'THIAGO CARVALHO',
        null,
        TRUE
    ),
    (
        442,
        'THIAGO CORREIA DA SILVA',
        null,
        TRUE
    ),
    (
        443,
        'THIAGO OLIVEIRA CONDÉ',
        null,
        TRUE
    ),
    (
        444,
        'TIAGO B.KISAKA',
        null,
        TRUE
    ),
    (
        445,
        'TIAGO CASTRO SILVA',
        null,
        TRUE
    ),
    (
        446,
        'TIAGO VILAÇA BASTOS',
        null,
        TRUE
    ),
    (
        447,
        'TITO AURELIANO',
        null,
        TRUE
    ),
    (
        448,
        'TOM DIAS MOTTA MORITA',
        null,
        TRUE
    ),
    (
        449,
        'TONY VINÍCIUS MOREIRA SAMPAIO',
        null,
        TRUE
    ),
    (
        450,
        'ULISSES BRIGATTO ALBINO',
        null,
        TRUE
    ),
    (
        451,
        'ÚRSULA DE AZEVEDO RUCHKYS',
        null,
        TRUE
    ),
    (
        452,
        'VALÉRIA C. TAVARES',
        null,
        TRUE
    ),
    (
        453,
        'VALÉRIA MARTINS',
        null,
        TRUE
    ),
    (
        454,
        'AIDVANE MORAES NOGUEIRA',
        null,
        TRUE
    ),
    (
        455,
        'ANANDA ANDRADE CORDOVIL',
        null,
        TRUE
    ),
    (
        456,
        'ANTONIEL FERNANDES',
        null,
        TRUE
    ),
    (
        457,
        'BEATRIZ M. SANTOS',
        null,
        TRUE
    ),
    (458, 'BENTO', null, TRUE),
    (
        459,
        'BERNARDO MACHADO GONTIJO',
        null,
        TRUE
    ),
    (
        460,
        'BRUNO CAVALCANTE BELLINI',
        null,
        TRUE
    ),
    (
        461,
        'CAIO HENRIQUE ROCHA VASCONCELOS',
        null,
        TRUE
    ),
    (
        462,
        'CAMILA S. OLIVEIRA',
        null,
        TRUE
    ),
    (
        463,
        'CARLOS JOSÉ SOUSA PASSOS',
        null,
        TRUE
    ),
    (
        464,
        'CHRISTIANO FERREIRA',
        null,
        TRUE
    ),
    (
        465,
        'CLEBER CUNHA FIGUEREDO',
        null,
        TRUE
    ),
    (
        466,
        'DAPHNE HELOISA DE FREITAS MUNIZ',
        null,
        TRUE
    ),
    (
        467,
        'DIEGO RODRIGUES',
        null,
        TRUE
    ),
    (
        468,
        'DOMINNYKES S. S. NEVES',
        null,
        TRUE
    ),
    (
        469,
        'ÉRICA MARTINS DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        470,
        'GABRIEL LUCAS DE FREITAS COSTA',
        null,
        TRUE
    ),
    (
        471,
        'GLEYCE DA SILVA MEDEIROS',
        null,
        TRUE
    ),
    (
        472,
        'HUGO RODRIGUES DE ARAÚJO',
        null,
        TRUE
    ),
    (
        473,
        'INSTITUTO BRASILEIRO DE DESENVOLVIMENTO',
        null,
        TRUE
    ),
    (
        474,
        'JACKSON C. MEANS',
        null,
        TRUE
    ),
    (
        475,
        'JARBAS JORGE DE ALCANTARA',
        null,
        TRUE
    ),
    (
        476,
        'JÉSSICA RUSSEL',
        null,
        TRUE
    ),
    (
        477,
        'JÉSSICA S. GALLO',
        null,
        TRUE
    ),
    (
        478,
        'JESSICA SCAGLIONE GALLO',
        null,
        TRUE
    ),
    (
        479,
        'JOÃO PEDRO PINHEIRO FARIA',
        null,
        TRUE
    ),
    (480, 'JOSÉ NUNES', null, TRUE),
    (
        481,
        'KALOYAN IVANOV',
        null,
        TRUE
    ),
    (
        482,
        'LAIS FURTADO OLICEIRA',
        null,
        TRUE
    ),
    (
        483,
        'LAYANNE O. FERRO',
        null,
        TRUE
    ),
    (
        484,
        'LEONARDO MENDES',
        null,
        TRUE
    ),
    (
        485,
        'LOPES FERREIRA',
        null,
        TRUE
    ),
    (
        486,
        'LUCIANO A. F. OLIVIERA FILHO',
        null,
        TRUE
    ),
    (
        487,
        'LUCIANO FARIA',
        null,
        TRUE
    ),
    (
        488,
        'LUIZ F.M. INIESTA',
        null,
        TRUE
    ),
    (
        489,
        'MAIARA BEATRIZ M. SILVA',
        null,
        TRUE
    ),
    (490, 'MAOLINO', null, TRUE),
    (
        491,
        'MARCOS MOREIRA',
        null,
        TRUE
    ),
    (
        492,
        'MATHEUS HENRIQUE SIMÕES',
        null,
        TRUE
    ),
    (
        493,
        'MAYARA MARINA DE SOUZA',
        null,
        TRUE
    ),
    (
        494,
        'MEDEIROS BENTO',
        null,
        TRUE
    ),
    (
        495,
        'NATHAN SILVA',
        null,
        TRUE
    ),
    (
        496,
        'OLITNO LIPARINI PEREIRA',
        null,
        TRUE
    ),
    (
        497,
        'OLITON LIPARINI PEREIRA',
        null,
        TRUE
    ),
    (
        498,
        'PAULO ENRIQUE CARDOSO PEIXOTO',
        null,
        TRUE
    ),
    (
        499,
        'RAONI JAPIASSU MERISSE',
        null,
        TRUE
    ),
    (
        500,
        'RAQUEL FARIA SCALCO',
        null,
        TRUE
    ),
    (
        501,
        'RENATO F.F. FRANCO',
        null,
        TRUE
    ),
    (
        502,
        'ROGEW F. R. MELO',
        null,
        TRUE
    ),
    (
        503,
        'SAMILA NERES FARIAS DA SILVA',
        null,
        TRUE
    ),
    (
        504,
        'SANDRO RAPHAEL BORGES',
        null,
        TRUE
    ),
    (
        505,
        'SÉRIGO KOIDE.',
        null,
        TRUE
    ),
    (
        506,
        'SIMONE NUNES FONSECA',
        null,
        TRUE
    ),
    (
        507,
        'SOUZA SILVA',
        null,
        TRUE
    ),
    (
        508,
        'SUSTENTABILIDADE IABS)',
        null,
        TRUE
    ),
    (
        509,
        'TÁSSIA RAYANE FERREIRA CHAGAS',
        null,
        TRUE
    ),
    (
        510,
        'TATIANE M. DA SILVA',
        null,
        TRUE
    ),
    (
        511,
        'VALDINEY AMARAL LEITE',
        null,
        TRUE
    ),
    (
        512,
        'VALERIA DA CUNHA TAVARES',
        null,
        TRUE
    ),
    (
        513,
        'VÂNIA APARECIDA VICENTE',
        null,
        TRUE
    ),
    (
        514,
        'VELIBOR SPALEVIC',
        null,
        TRUE
    ),
    (
        515,
        'VICTORIA BONFIM BARROS',
        null,
        TRUE
    ),
    (
        516,
        'VITOR DE OLIVEIRA LUNARDI',
        null,
        TRUE
    ),
    (
        517,
        'VITOR GABRIEL PEREIRA JUNTA',
        null,
        TRUE
    ),
    (
        518,
        'VITOR MARCOS AGUIAR DE MOURA',
        null,
        TRUE
    ),
    (
        519,
        'VITÓRIA ALVES',
        null,
        TRUE
    ),
    (
        520,
        'VITORIA CRISTINA SANTIAGO ALVES',
        null,
        TRUE
    ),
    (
        521,
        'VITÓRIA ELIZ DOS SANTOS MELO',
        null,
        TRUE
    ),
    (
        522,
        'VITÓRIA SANTIAGO',
        null,
        TRUE
    ),
    (
        523,
        'WALTER APARECIDO ARRUDA DE OLIVEIRA',
        null,
        TRUE
    ),
    (
        524,
        'WELITOM RODRIGUES BORGES',
        null,
        TRUE
    ),
    (
        525,
        'WILLIAM BRUNO DE SOUZA ALMEIDA',
        null,
        TRUE
    ),
    (
        526,
        'YAWAR HUSSAIN',
        null,
        TRUE
    ),
    (
        527,
        'YESENIA M. CARPIO DIAZ',
        null,
        TRUE
    ),
    (
        528,
        'ZACARIAS TARGINO DE FREITAS NETO',
        null,
        TRUE
    ),
    (
        529,
        'ZENEIDE DAMIÃO DA SILVAO',
        null,
        TRUE
    ),
    (
        530,
        'VINÍCIUS DA F. SPERANDEI',
        null,
        TRUE
    ),
    (
        531,
        'WILLIAM HANSON',
        null,
        TRUE
    ),
    (
        532,
        'VANESSA L. GONZÁLEZ',
        null,
        TRUE
    ),
    (
        533,
        'VICTOR H. VALIATI',
        null,
        TRUE
    ),
    (
        534,
        'VERÔNICA SLOBODIAN',
        null,
        TRUE
    ),
    (
        535,
        'VINÍCIUS VENTURA',
        null,
        TRUE
    ),
    (
        536,
        'GISELLE RIBEIRO',
        null,
        TRUE
    )
ON CONFLICT (id) DO NOTHING;

INSERT INTO
    repositorio_areatematica (id, nome, ativo)
VALUES (1, 'MEIO FÍSICO', TRUE),
    (2, 'MEIO BIÓTICO', TRUE),
    (3, 'OUTROS', TRUE)
ON CONFLICT (id) DO NOTHING;

INSERT INTO
    repositorio_subareatematica (
        id,
        nome,
        ativo,
        area_tematica_id
    )
VALUES (
        1,
        'Geologia e Geomorfologia',
        TRUE,
        1
    ),
    (
        2,
        'Hidrologia e Hidrogeologia',
        TRUE,
        1
    ),
    (
        3,
        'Espeleologia e Caracterização Ambiental',
        TRUE,
        1
    ),
    (
        4,
        'Biodiversidade Subterrânea',
        TRUE,
        2
    ),
    (5, 'Ecologia', TRUE, 2),
    (
        6,
        'Conservação da biodiversidade',
        TRUE,
        2
    ),
    (
        7,
        'Socioeconômico e socioambiental',
        TRUE,
        3
    ),
    (
        8,
        'Gestão Ambiental',
        TRUE,
        3
    ),
    (
        9,
        'Espeleoturismo e Uso Público',
        TRUE,
        3
    )
ON CONFLICT (id) DO NOTHING;

INSERT INTO
    repositorio_status (id, nome, ativo, is_public)
VALUES (1, 'PUBLICADO', TRUE, TRUE),
    (2, 'PRODUZIDO', TRUE, TRUE)
ON CONFLICT (id) DO NOTHING;

INSERT INTO
    repositorio_tipopublicacao (id, nome, ativo)
VALUES (1, 'ARQUIVO PDF', TRUE),
    (
        2,
        'OUTRO TIPO DE ARQUIVO',
        TRUE
    ),
    (3, 'LINK WEB PAGE', TRUE),
    (4, 'LINK ARQUIVO', TRUE),
    (5, 'LINK VIDEO', TRUE)
ON CONFLICT (id) DO NOTHING;

INSERT INTO
    repositorio_tag (id, nome, ativo)
VALUES (1, 'ABRIGO CAVERNÍCOLA', TRUE),
    (2, 'ACERVO', TRUE),
    (3, 'ÁGUAS SUBTERRÂNEAS', TRUE),
    (
        4,
        'ALGORITIMO DE ZONAÇÃO',
        TRUE
    ),
    (5, 'ALIMENTAÇÃO', TRUE),
    (6, 'ALÚVIO', TRUE),
    (7, 'AMAZÔNIA', TRUE),
    (
        8,
        'AMAZÔNIA BRASILEIRA',
        TRUE
    ),
    (
        9,
        'AMBIENTE CAVERNÍCOLA',
        TRUE
    ),
    (
        10,
        'AMBIENTE SUBTERRÂNEO',
        TRUE
    ),
    (11, 'AMEAÇAS', TRUE),
    (12, 'AMPHIPODA', TRUE),
    (
        13,
        'ANÁLISE DE ATRIBUTOS',
        TRUE
    ),
    (14, 'ANÁLISE ESPECTRAL', TRUE),
    (15, 'ANÁLISES', TRUE),
    (
        16,
        'ANÁLISES FILOGENÉTICAS',
        TRUE
    ),
    (17, 'ANFÍBIO', TRUE),
    (18, 'ANISOPTERA', TRUE),
    (19, 'ANTIMICROBIANOS', TRUE),
    (20, 'ANURO', TRUE),
    (
        21,
        'APA NASCENTES DO RIO VERMELHO',
        TRUE
    ),
    (22, 'APANRV', TRUE),
    (23, 'APERIODICIDADE', TRUE),
    (
        24,
        'APLICAÇÃO BIOTECNOLOGICA',
        TRUE
    ),
    (25, 'AQUÁTICO', TRUE),
    (26, 'AQUÍFERO', TRUE),
    (
        27,
        'AQUÍFEROS CÁRSTICOS',
        TRUE
    ),
    (28, 'ARACHNIDA', TRUE),
    (29, 'ARACNÍDEOS', TRUE),
    (30, 'ARCHNIDA', TRUE),
    (31, 'ÁREA CÁRSTICA', TRUE),
    (
        32,
        'ÁREA DE PRESERVAÇÃO',
        TRUE
    ),
    (33, 'ÁREAS CÁRSTICAS', TRUE),
    (
        34,
        'ÁREAS CÁRSTICAS RESTAURADAS',
        TRUE
    ),
    (
        35,
        'ÁREAS PRIORITÁRIAS',
        TRUE
    ),
    (36, 'ÁREAS PROTEGIDAS', TRUE),
    (37, 'ARQUEOLOGIA', TRUE),
    (38, 'ARRITIMIA', TRUE),
    (39, 'ARTHOPODA', TRUE),
    (40, 'ARTHROPODA', TRUE),
    (41, 'ARTROPHODA', TRUE),
    (
        42,
        'ASCOMICETOS ASSEXUAIS',
        TRUE
    ),
    (43, 'ASCOMYCOTA', TRUE),
    (44, 'ASPERGILLUS', TRUE),
    (
        45,
        'ATIVIDA ANTIMICROBIANA',
        TRUE
    ),
    (
        46,
        'ATIVIDADE LOCOMOTORA',
        TRUE
    ),
    (
        47,
        'ATRIBUTOS GEORADAS',
        TRUE
    ),
    (48, 'AVE', TRUE),
    (49, 'AVES', TRUE),
    (
        50,
        'BACIA DO ALTO TAPAJÓS',
        TRUE
    ),
    (
        51,
        'BACIA DO RIO SÃO FRANCISCO',
        TRUE
    ),
    (
        52,
        'BACIA DO SÃO FRANCISCO',
        TRUE
    ),
    (
        53,
        'BACIA EXPERIMENTAL',
        TRUE
    ),
    (
        54,
        'BACIA HIDROGEOLÓGICA',
        TRUE
    ),
    (
        55,
        'BÁCIA SÃO FRANCISCO',
        TRUE
    ),
    (56, 'BAHIA', TRUE),
    (57, 'BAT CAVES', TRUE),
    (58, 'BIOACÚSTICA', TRUE),
    (59, 'BIODIVERSIDADE', TRUE),
    (
        60,
        'BIODIVERSIDADE SUBTERRÂNEA',
        TRUE
    ),
    (
        61,
        'BIODIVERSIDADE TROPICA',
        TRUE
    ),
    (62, 'BIOFLORA', TRUE),
    (63, 'BIOGEOMORFOLOGIA', TRUE),
    (64, 'BIOINDICADORES', TRUE),
    (
        65,
        'BIOLOGIA SUBTERRÂNEA',
        TRUE
    ),
    (66, 'BIOMA CERRADO', TRUE),
    (67, 'BIOMAS', TRUE),
    (
        68,
        'BIOTECNOLOGIA AMBIENTAL',
        TRUE
    ),
    (
        69,
        'BIOTECNOLOGIA FUNGICA',
        TRUE
    ),
    (70, 'BOLETIM', TRUE),
    (71, 'BRASIL', TRUE),
    (72, 'BRIÓFITAS', TRUE),
    (73, 'C14', TRUE),
    (74, 'CAATINGA', TRUE),
    (75, 'CADASTRO', TRUE),
    (76, 'CANAÃ DOS CARAJÁS', TRUE),
    (77, 'CANGA', TRUE),
    (78, 'CANIE', TRUE),
    (79, 'CARACTERIZAÇÃO', TRUE),
    (80, 'CARAJÁS', TRUE),
    (81, 'CARBONÁTICA', TRUE),
    (
        82,
        'CARBONATOS CONTINENTAIS',
        TRUE
    ),
    (83, 'CARGA HIDRÁULICA', TRUE),
    (84, 'CARIÓTIPO', TRUE),
    (85, 'CARJÁS', TRUE),
    (86, 'CARST', TRUE),
    (87, 'CARSTE', TRUE),
    (
        88,
        'CARSTE SILICISLÁSTICO',
        TRUE
    ),
    (89, 'CARTILHA', TRUE),
    (90, 'CATEGORIAS IUCN', TRUE),
    (91, 'CAVERNA', TRUE),
    (92, 'CAVERNA TARIMBA', TRUE),
    (93, 'CAVERNA VADOSA', TRUE),
    (94, 'CAVERNAS', TRUE),
    (
        95,
        'CAVERNAS FERRÍFERA',
        TRUE
    ),
    (
        96,
        'CAVIDADE NATURAL SUBTERRÂNEA',
        TRUE
    ),
    (
        97,
        'CAVIDADES NATURAIS',
        TRUE
    ),
    (98, 'CENTRO-OESTE', TRUE),
    (99, 'CENTRUROIDINAE', TRUE),
    (100, 'CERRADO', TRUE),
    (101, 'CHELONIAN', TRUE),
    (102, 'CHILOPODA', TRUE),
    (103, 'CHIROPTERA', TRUE),
    (104, 'CLPI', TRUE),
    (105, 'CNC', TRUE),
    (106, 'CO-OCORRÊNCIA', TRUE),
    (
        107,
        'CÓDIGO DE BARRAS DE DNA',
        TRUE
    ),
    (108, 'COLLEMBOLA', TRUE),
    (109, 'COLORIR', TRUE),
    (110, 'COLÚVIO', TRUE),
    (111, 'COMPARTIMENTOS', TRUE),
    (112, 'COMPOSIÇÃO', TRUE),
    (113, 'COMUNIDADE', TRUE),
    (114, 'COMUNIDADES', TRUE),
    (
        115,
        'COMUNIDADES MICROBIANAS',
        TRUE
    ),
    (
        116,
        'CONDUTOS SUBTERRÂNEOS',
        TRUE
    ),
    (
        117,
        'CONECTIVIDADE CAVERNAS SOLO',
        TRUE
    ),
    (118, 'CONFINAMENTO', TRUE),
    (119, 'CONGRESSO', TRUE),
    (
        120,
        'CONGRESSO INTERNACIONAL',
        TRUE
    ),
    (
        121,
        'CONJUNTO DE PÓLEM',
        TRUE
    ),
    (122, 'CONSERVAÇÃO', TRUE),
    (
        123,
        'CONSERVAÇÃO DA FAUNA SUBTERRÂNEA',
        TRUE
    ),
    (
        124,
        'CONSERVAÇÃO DE MORCEGOS',
        TRUE
    ),
    (
        125,
        'CONSERVAÇÃO DO SOLO',
        TRUE
    ),
    (126, 'CONTAMINAÇÃO', TRUE),
    (127, 'CORAL', TRUE),
    (
        128,
        'CORROSÃO BIOGÊNICA',
        TRUE
    ),
    (129, 'COX 1', TRUE),
    (130, 'CRINOCHETA', TRUE),
    (131, 'CRONOBIOLOGIA', TRUE),
    (132, 'CRUSTACEAE', TRUE),
    (
        133,
        'CRUSTÁCEOS SUBTERRÂNEOS',
        TRUE
    ),
    (
        134,
        'DELIMITAÇÃO DE ESPÉCIE',
        TRUE
    ),
    (
        135,
        'DELIMITAÇÃO DE LINHAGEM',
        TRUE
    ),
    (
        136,
        'DELIMITAÇÃO DE LINHAGENS',
        TRUE
    ),
    (
        137,
        'DELIZAMENTO DE TERRA',
        TRUE
    ),
    (
        138,
        'DELIZAMENTO DE TERRA EM SOBRADINHO',
        TRUE
    ),
    (139, 'DEM', TRUE),
    (140, 'DENSIDADE', TRUE),
    (
        141,
        'DEPOSIÇÃO DE SEDIMENTO',
        TRUE
    ),
    (
        142,
        'DEPÓSITOS FLUVIAIS',
        TRUE
    ),
    (
        143,
        'DEPÓSITOS SEDIMENTARES',
        TRUE
    ),
    (
        144,
        'DEPRESSÃO FECHADA',
        TRUE
    ),
    (
        145,
        'DESNUDAÇÃO NATURAL',
        TRUE
    ),
    (
        146,
        'DETECÇÃO DE FEIÇÕES',
        TRUE
    ),
    (147, 'DIAFNOSES', TRUE),
    (148, 'DIPOLO-DIPOLO', TRUE),
    (
        149,
        'DÍPTERAS ECTOPARASITAS',
        TRUE
    ),
    (150, 'DISPERSÃO', TRUE),
    (151, 'DISTRIBUIÇÃO', TRUE),
    (
        152,
        'DISTRIBUIÇÃO POTENCIAL DE ESPÉCIES',
        TRUE
    ),
    (153, 'DISTRITO FEDERAL', TRUE),
    (154, 'DIVERSIDADE', TRUE),
    (
        155,
        'DIVERSIDADE MICROBIANA',
        TRUE
    ),
    (156, 'DOLINA', TRUE),
    (157, 'DOLINAS', TRUE),
    (
        158,
        'DOMINÍNIOS GEOMORFOLÓGICO',
        TRUE
    ),
    (159, 'ECOLOGIA', TRUE),
    (
        160,
        'ECOLOGIA DE PAISAGEM',
        TRUE
    ),
    (161, 'ECOSSISTEMA', TRUE),
    (
        162,
        'ECOSSISTEMAS SUBTERRÂNEOS',
        TRUE
    ),
    (163, 'EDIAL', TRUE),
    (164, 'EDITAL', TRUE),
    (
        165,
        'EDITAL FERRUGINOSAS',
        TRUE
    ),
    (166, 'EDTAL', TRUE),
    (
        167,
        'EDUCAÇÃO AMBIENTAL',
        TRUE
    ),
    (168, 'EDUCOMUNICAÇÃO', TRUE),
    (
        169,
        'ELETRORRESISTIVIDADE',
        TRUE
    ),
    (170, 'ENCONTRO', TRUE),
    (171, 'ENCOSTA', TRUE),
    (172, 'ENDECOUS', TRUE),
    (173, 'ENDEMISMO', TRUE),
    (174, 'ENDURO', TRUE),
    (
        175,
        'ENRIQUECIMENTO DE FINOS',
        TRUE
    ),
    (176, 'ENSIFERA', TRUE),
    (177, 'ENVELOPE', TRUE),
    (178, 'ENZIMAS', TRUE),
    (179, 'EROSÃO', TRUE),
    (180, 'EROSÃO HÍDRICA', TRUE),
    (181, 'ERT', TRUE),
    (182, 'ESCALA ESPACIAL', TRUE),
    (183, 'ESCALA EVOLUTIVA', TRUE),
    (
        184,
        'ESCALAS AMOSTRAIS',
        TRUE
    ),
    (185, 'ESCOAMENTO', TRUE),
    (
        186,
        'ESCOAMENTO SUPERFICIAL',
        TRUE
    ),
    (187, 'ESCURIDÃO', TRUE),
    (
        188,
        'ESPÉCIE CAVERNÍCOLA',
        TRUE
    ),
    (
        189,
        'ESPÉCIE TROGLÓBIA',
        TRUE
    ),
    (
        190,
        'ESPÉCIES AMEAÇADAS',
        TRUE
    ),
    (
        191,
        'ESPÉCIES CAVERNÍCOLA',
        TRUE
    ),
    (
        192,
        'ESPÉCIES CRÍPTICAS',
        TRUE
    ),
    (193, 'ESPECTROGRAMA', TRUE),
    (
        194,
        'ESPECTRORRADIOMETRIA',
        TRUE
    ),
    (195, 'ESPELEOFAUNA', TRUE),
    (
        196,
        'ESPELEOFOTOGRAFIA',
        TRUE
    ),
    (197, 'ESPELEOGÊNES', TRUE),
    (198, 'ESPELEOGENESE', TRUE),
    (199, 'ESPELEOLOGIA', TRUE),
    (200, 'ESPELEOMICOLOGIA', TRUE),
    (
        201,
        'ESPELEOTOPOGRAFIA',
        TRUE
    ),
    (202, 'ESPELEOTURISMO', TRUE),
    (203, 'ESPELOMETRIA', TRUE),
    (204, 'ESPINHAÇO', TRUE),
    (205, 'ESTABILIDADE', TRUE),
    (
        206,
        'ESTABILIDADE GEOTÉCNICA',
        TRUE
    ),
    (
        207,
        'ESTADO DE CONSERVAÇÃO',
        TRUE
    ),
    (
        208,
        'ESTASE MORFOLÓGICA',
        TRUE
    ),
    (209, 'ESTIMADORES', TRUE),
    (210, 'ESTRATIGRAFICA', TRUE),
    (
        211,
        'ESTRUTURA DA COMUNIDADE',
        TRUE
    ),
    (
        212,
        'ESTRUTURAÇÃO DE HABITAT',
        TRUE
    ),
    (213, 'EVOLUÇÃO', TRUE),
    (
        214,
        'EVOLUÇÃO MOLECULA',
        TRUE
    ),
    (215, 'EXPLORAÇÃO', TRUE),
    (216, 'EXPOSIÇÃO', TRUE),
    (
        217,
        'FACES SEDIMETARES',
        TRUE
    ),
    (218, 'FÁCIES', TRUE),
    (219, 'FATOR AMBIENTAL', TRUE),
    (
        220,
        'FAUNA CAVERNÍCOLA',
        TRUE
    ),
    (
        221,
        'FAUNA DE CAVERNAS',
        TRUE
    ),
    (
        222,
        'FAUNA SUBTERRÂNEA',
        TRUE
    ),
    (
        223,
        'FAZENDA ÁGUA LIMPA',
        TRUE
    ),
    (224, 'FERRÍFERAS', TRUE),
    (225, 'FERRUGINOSAS', TRUE),
    (226, 'FERRUGIONOSAS', TRUE),
    (227, 'FERRUGNOSAS', TRUE),
    (
        228,
        'FILOGENIA COMPARATIVA',
        TRUE
    ),
    (
        229,
        'FILOGENIA MOLECULAR',
        TRUE
    ),
    (230, 'FILOGEOGRAFIA', TRUE),
    (
        231,
        'FILOGEOGRAFIA COMPARATIVA',
        TRUE
    ),
    (
        232,
        'FILOGEOGRAFIA DE ESPÉCIES TROGLÓBIAS',
        TRUE
    ),
    (
        233,
        'FLORA CAVERNÍCOLA',
        TRUE
    ),
    (
        234,
        'FLORESTA AMAZÔNICA',
        TRUE
    ),
    (
        235,
        'FLORESTA TROPICAL',
        TRUE
    ),
    (236, 'FLUVIOCARSTE', TRUE),
    (237, 'FLUVIOCÁRSTE', TRUE),
    (238, 'FLUXO', TRUE),
    (239, 'FLUXO REGIONAL', TRUE),
    (
        240,
        'FLUXO SUBTERRÂNEO',
        TRUE
    ),
    (
        241,
        'FORMAÇÃO FERRÍFERA CARAJÁS',
        TRUE
    ),
    (
        242,
        'FORMAÇÃO JANDAÍRA',
        TRUE
    ),
    (
        243,
        'FORMAÇÃO TOMBADOR',
        TRUE
    ),
    (244, 'FÓSSIL', TRUE),
    (245, 'FOTOGAMETRIA', TRUE),
    (246, 'FOTOGRAFIA', TRUE),
    (247, 'FRATURA', TRUE),
    (248, 'FRUGIVORIA', TRUE),
    (249, 'FUNGOS', TRUE),
    (
        250,
        'FUNGOS ANEMÓFILOS',
        TRUE
    ),
    (
        251,
        'FUNGOS CAVERNÍCOLAS',
        TRUE
    ),
    (
        252,
        'FUNGOS EM CAVERNAS',
        TRUE
    ),
    (253, 'FURNA FEIA', TRUE),
    (254, 'GAP ANALYSIS', TRUE),
    (255, 'GENÉTICA', TRUE),
    (
        256,
        'GENÉTICA DA CONSERVAÇÃO',
        TRUE
    ),
    (257, 'GEOCONSERVAÇÃO', TRUE),
    (258, 'GEOCRONOLOGIA', TRUE),
    (259, 'GEODIVERSIDADE', TRUE),
    (260, 'GEOECOLOGIA', TRUE),
    (261, 'GEOESPELEOLOGIA', TRUE),
    (262, 'GEOÉTICA', TRUE),
    (263, 'GEOFÍSICA', TRUE),
    (264, 'GEOMODELAGEM', TRUE),
    (265, 'GEOMORFOLOGIA', TRUE),
    (
        266,
        'GEOMORFOLOGIA CÁRSTICA',
        TRUE
    ),
    (
        267,
        'GEOPATRIMÔNIO ESPELEOLÓGICO',
        TRUE
    ),
    (268, 'GEOQUÍMICA', TRUE),
    (
        269,
        'GEOQUÍMICA DA ROCHA',
        TRUE
    ),
    (270, 'GERROMORPHA', TRUE),
    (271, 'GESTÃO', TRUE),
    (272, 'GESTÃO AMBIENTAL', TRUE),
    (
        273,
        'GESTÃO DE RECURSOS HÍDRICOS',
        TRUE
    ),
    (274, 'GIS', TRUE),
    (275, 'GODWANA', TRUE),
    (276, 'GPR', TRUE),
    (277, 'GRÁFICO', TRUE),
    (278, 'GRAVAÇÃO', TRUE),
    (
        279,
        'GRUPOS HIDROLÓGICOS DE SOLOS',
        TRUE
    ),
    (280, 'GUANO DE MORCEGO', TRUE),
    (
        281,
        'GUANO DE MORCEGOS',
        TRUE
    ),
    (282, 'GUILDA TRÓFICA', TRUE),
    (283, 'HABITAT', TRUE),
    (284, 'HABITAT FREÁTICO', TRUE),
    (
        285,
        'HABITAT SUBTERRÂNEO SUPERFICIAL',
        TRUE
    ),
    (
        286,
        'HABITAT SUBTERRÂNEOS',
        TRUE
    ),
    (287, 'HEMIPTERA', TRUE),
    (288, 'HEPÁTICA', TRUE),
    (289, 'HEPÁTICAS', TRUE),
    (290, 'HERPETOFAUNA', TRUE),
    (
        291,
        'HETEROGENEIDADE DE HÁBITAR',
        TRUE
    ),
    (292, 'HIDROLOGIA', TRUE),
    (
        293,
        'HIDROLOGIA CÁRSTICA',
        TRUE
    ),
    (
        294,
        'HIDROLOGIA DE BACIA',
        TRUE
    ),
    (295, 'HIPPOBOSCOIDEA', TRUE),
    (296, 'HISTERESE', TRUE),
    (297, 'HISTÓRIA', TRUE),
    (298, 'HOT CAVES', TRUE),
    (299, 'HVSR', TRUE),
    (
        300,
        'ICTIOFAUNA SUBTERRÂNEA',
        TRUE
    ),
    (301, 'IGARAPÉ', TRUE),
    (302, 'IGARAPÉS', TRUE),
    (303, 'ILUSTRATIVO', TRUE),
    (304, 'IMPACTO', TRUE),
    (
        305,
        'IMPACTO ANTRÓPICO',
        TRUE
    ),
    (
        306,
        'IMPACTOS DA MINERAÇÃO',
        TRUE
    ),
    (
        307,
        'INDÍCES PARASITÁRIOS',
        TRUE
    ),
    (308, 'INDÍGENA', TRUE),
    (309, 'INFORMAÇÕES', TRUE),
    (310, 'INSETO', TRUE),
    (311, 'INSETOS', TRUE),
    (312, 'INTERAÇÃO', TRUE),
    (
        313,
        'INTERAÇÃO MORCEGO-PLANTA',
        TRUE
    ),
    (
        314,
        'INTERAÇÃO PARASITA-HOSPEDEIRO',
        TRUE
    ),
    (
        315,
        'INTERAÇÃO PREDADOR-PRESA',
        TRUE
    ),
    (316, 'INTERPOLAÇÃO', TRUE),
    (
        317,
        'INTERPRETAÇÃO DE IMAGENS',
        TRUE
    ),
    (318, 'INVENTÁRIO', TRUE),
    (
        319,
        'INVENTÁRIO FAUNÍSTICO',
        TRUE
    ),
    (320, 'INVERTEBRADO', TRUE),
    (321, 'INVERTEBRADOS', TRUE),
    (322, 'IPHONE', TRUE),
    (323, 'ISOPODA', TRUE),
    (
        324,
        'ISÓPODE TERRESTRE',
        TRUE
    ),
    (
        325,
        'ISÓPODES TERRESTRES',
        TRUE
    ),
    (
        326,
        'ISÓPODOS ANFÍBIOS',
        TRUE
    ),
    (327, 'ISÓTOPOS', TRUE),
    (
        328,
        'KINNAPOTIGUARA TROGLOBIA',
        TRUE
    ),
    (329, 'LAGO PARANOÁ', TRUE),
    (330, 'LAJEDO', TRUE),
    (331, 'LEGISLAÇÃO', TRUE),
    (
        332,
        'LEVANTAMENTO DA FLORA',
        TRUE
    ),
    (
        333,
        'LEVANTAMENTO DE CAMPO',
        TRUE
    ),
    (334, 'LICÓFITAS', TRUE),
    (335, 'LIVRO', TRUE),
    (336, 'LUZES', TRUE),
    (337, 'MACIÇO ROCHOSOS', TRUE),
    (
        338,
        'MACROINVERTEBRADOS',
        TRUE
    ),
    (339, 'MAMBAÍ', TRUE),
    (340, 'MAMÍFERO', TRUE),
    (341, 'MAMÍFEROS', TRUE),
    (
        342,
        'MAMÍFEROS VOADORES',
        TRUE
    ),
    (343, 'MAMMALIA', TRUE),
    (344, 'MAPEAMENTO', TRUE),
    (
        345,
        'MAPEAMENTO DO SOLO',
        TRUE
    ),
    (
        346,
        'MAPEAMENTO PEDOLÓGICO',
        TRUE
    ),
    (
        347,
        'MARCADORES MOLECULARES',
        TRUE
    ),
    (348, 'MDE', TRUE),
    (349, 'MDT', TRUE),
    (350, 'MECANISMO', TRUE),
    (
        351,
        'MEIO SUBTERRÂNEO SUPERFICIAL',
        TRUE
    ),
    (352, 'MESOCAVIDADES', TRUE),
    (353, 'MESOGAMMARIDAE', TRUE),
    (354, 'META ANÁLISE', TRUE),
    (355, 'METABARCODIN', TRUE),
    (
        356,
        'METABOLISMO DO FERRO',
        TRUE
    ),
    (
        357,
        'METABOLISMO FUNGICO',
        TRUE
    ),
    (358, 'METAGENÔMICA', TRUE),
    (359, 'METAIS', TRUE),
    (360, 'METARENITOS', TRUE),
    (361, 'MÉTODO COP', TRUE),
    (
        362,
        'MÉTODO DE EROSÃO POTENCIAL',
        TRUE
    ),
    (
        363,
        'METODOLOGIAS DE COLETA INDIRETA',
        TRUE
    ),
    (
        364,
        'MÉTODOS DE AMOSTRAGEM',
        TRUE
    ),
    (
        365,
        'MÉTODOS DIRETOS E INDIRETOS',
        TRUE
    ),
    (366, 'MICOBIOTA', TRUE),
    (367, 'MICOLOGIA', TRUE),
    (368, 'MICROBIOLOGIA', TRUE),
    (
        369,
        'MICROBIOMA DE CAVERNA',
        TRUE
    ),
    (370, 'MICRORGANISMO', TRUE),
    (371, 'MINAS GERAIS', TRUE),
    (
        372,
        'MINERAÇÃO SUSTENTÁVEL',
        TRUE
    ),
    (373, 'MINERALOGIA', TRUE),
    (374, 'MODELAGEM', TRUE),
    (
        375,
        'MODELAGEM DE DISTRIBUIÇÃO DE ESPÉCIES',
        TRUE
    ),
    (
        376,
        'MODELO DE DISTRIBUIÇÃO DE ESPÉCIES',
        TRUE
    ),
    (
        377,
        'MODELO DE NICHO ECOLÓGICO',
        TRUE
    ),
    (
        378,
        'MODIFICAÇÃO DE HABITAT',
        TRUE
    ),
    (
        379,
        'MONITORAMENTO ACÚSTICO PASSIVO',
        TRUE
    ),
    (
        380,
        'MONITORAMENTO DO FLUXO DE ÁGUA SUBTERRÂNEA',
        TRUE
    ),
    (
        381,
        'MONITORAMENTO SAZONAL',
        TRUE
    ),
    (
        382,
        'MORCEGO DE CAUDA CURTA',
        TRUE
    ),
    (383, 'MORCEGOS', TRUE),
    (384, 'MOROFOLOGIA', TRUE),
    (385, 'MSS', TRUE),
    (
        386,
        'MUDANÇA CLIMÁTICA',
        TRUE
    ),
    (387, 'MUSEU', TRUE),
    (388, 'MUSGOS', TRUE),
    (389, 'MUTUALISMO', TRUE),
    (390, 'NÃO INVASIVAS', TRUE),
    (
        391,
        'NASCENTE CÁRSTICA',
        TRUE
    ),
    (392, 'NEOTROPICAIS', TRUE),
    (393, 'NEOTROPICAL', TRUE),
    (394, 'NETROPICAL', TRUE),
    (395, 'NORDESTE', TRUE),
    (396, 'NOVA ESPÉCIE', TRUE),
    (397, 'ODONATA', TRUE),
    (398, 'ONISCIDEA', TRUE),
    (399, 'ÓRGÃOS', TRUE),
    (
        400,
        'OTIMIZAÇÃO DE ARRANJOS',
        TRUE
    ),
    (401, 'PAISAGEM', TRUE),
    (402, 'PALEOAMBIENTAIS', TRUE),
    (403, 'PALEOAMBIENTE', TRUE),
    (404, 'PALEOBURROW', TRUE),
    (405, 'PALEOCLIMA', TRUE),
    (406, 'PALEOECOLOGIA', TRUE),
    (407, 'PALINOLOGIA', TRUE),
    (408, 'PALINOMORFO', TRUE),
    (409, 'PANGEIA', TRUE),
    (410, 'PARAUAPEBAS', TRUE),
    (
        411,
        'PARCELAS DE ESCOAMENTO SUPERFICIAL',
        TRUE
    ),
    (412, 'PASTAGEM', TRUE),
    (413, 'PATRIMÔNIO', TRUE),
    (
        414,
        'PATRIMÔNIO CAVERNÍCOLA',
        TRUE
    ),
    (
        415,
        'PATRIMÔNIO ESPELEOLÓGICO',
        TRUE
    ),
    (416, 'PEIXE', TRUE),
    (
        417,
        'PEIXES FREATÓBIOS',
        TRUE
    ),
    (418, 'PELEOVALE', TRUE),
    (419, 'PENICILLIUM', TRUE),
    (
        420,
        'PEQUENOS MAMÍFEROS',
        TRUE
    ),
    (421, 'PERDA DE SOLO', TRUE),
    (
        422,
        'PERDAS DE SOLO E ÁGUA',
        TRUE
    ),
    (
        423,
        'PERFIL DE RESISTÊNCIA',
        TRUE
    ),
    (
        424,
        'PERFIL MICROBIANO',
        TRUE
    ),
    (425, 'PERUAÇU', TRUE),
    (426, 'PESQUISA', TRUE),
    (427, 'PHYLLOSTOMIDAE', TRUE),
    (428, 'PHYLLOSTOMINAE', TRUE),
    (429, 'PIABA', TRUE),
    (430, 'PIABA BRANCA', TRUE),
    (431, 'PLANÁRIAS', TRUE),
    (432, 'PLÁSTICO', TRUE),
    (
        433,
        'POÇO DE BOMBEAMENTO',
        TRUE
    ),
    (434, 'POÇOS TUBULARES', TRUE),
    (435, 'POLÉM', TRUE),
    (436, 'PÓLEM', TRUE),
    (
        437,
        'PONTOS DE VULNERABILIDADE',
        TRUE
    ),
    (438, 'PONTOS FRACOS', TRUE),
    (
        439,
        'POTENCIAL BIOTECNOLÓGICO',
        TRUE
    ),
    (
        440,
        'PRECIPITAÇÃO EXTREMA',
        TRUE
    ),
    (441, 'PREDAÇÃO', TRUE),
    (
        442,
        'PRIORIDADE DE CONSERVAÇÃO',
        TRUE
    ),
    (443, 'PRIORITÁRIA', TRUE),
    (
        444,
        'PRIORIZAÇÃO DA CONSERVAÇÃO',
        TRUE
    ),
    (
        445,
        'PRIORIZAÇÃO ESPACIAL',
        TRUE
    ),
    (
        446,
        'PRODUÇÃO DE SEDIMENTO',
        TRUE
    ),
    (
        447,
        'PRODUÇÃO E ENRIQUECIMENTO DE SEDIMENTOS',
        TRUE
    ),
    (
        448,
        'PROPRIEDADES DO SOLO',
        TRUE
    ),
    (449, 'PROSPECÇÃO', TRUE),
    (
        450,
        'PROVÍNCIA MINERALÓGICA DE CARAJÁS',
        TRUE
    ),
    (
        451,
        'QUADRILÁTERO FERRÍFERO',
        TRUE
    ),
    (
        452,
        'QUALIDADE DA ÁGUA',
        TRUE
    ),
    (453, 'QUATERNÁRIO', TRUE),
    (454, 'QUELÔNIO', TRUE),
    (455, 'QUETOTAZIA', TRUE),
    (
        456,
        'QUIMIOHETEROTROFIA',
        TRUE
    ),
    (457, 'QUIROPTEROCORIA', TRUE),
    (458, 'RADIOCARBONO', TRUE),
    (459, 'RECONSTRUÇÃO', TRUE),
    (460, 'RECUPERAÇÃO', TRUE),
    (
        461,
        'RECURSOS ORGÂNICOS',
        TRUE
    ),
    (462, 'REEF', TRUE),
    (463, 'REFLECTOMETRIA', TRUE),
    (464, 'REFORMA', TRUE),
    (
        465,
        'REGIÃO NEOTROPICAL',
        TRUE
    ),
    (
        466,
        'RELAÇÃO PARASITA-HOSPEDEIRO',
        TRUE
    ),
    (
        467,
        'RELÓGIO BIOLÓGICO',
        TRUE
    ),
    (468, 'REOLOGIA', TRUE),
    (469, 'RÉPTIL', TRUE),
    (
        470,
        'RESÍDUOS PLÁSTICOS',
        TRUE
    ),
    (
        471,
        'RESISTÊNCIA BACTERIANA',
        TRUE
    ),
    (
        472,
        'RESISTIVIDADE ELÉTRICA',
        TRUE
    ),
    (
        473,
        'RESITÂNCIA ANTIMICROBIANOS',
        TRUE
    ),
    (474, 'RESPIRAÇÃO', TRUE),
    (
        475,
        'RESTAURAÇÃ ECOLÓGICA',
        TRUE
    ),
    (476, 'RESTAURAÇÃO', TRUE),
    (
        477,
        'RESTAURAÇÃO ECOLÓGICA',
        TRUE
    ),
    (478, 'REUNIÃO', TRUE),
    (479, 'REVISÃO', TRUE),
    (
        480,
        'RIO GRANDE DO NORTE',
        TRUE
    ),
    (481, 'RIQUESA', TRUE),
    (482, 'RIQUEZA', TRUE),
    (
        483,
        'RIQUEZA DE ESPÉCIES',
        TRUE
    ),
    (484, 'RITMO', TRUE),
    (485, 'RITMO CIRCADIANO', TRUE),
    (486, 'ROCHA FRATURADA', TRUE),
    (
        487,
        'RUÍDO AMBIENTE RMS',
        TRUE
    ),
    (488, 'RUÍDO SÍSMICO', TRUE),
    (489, 'SAMAMBAIAS', TRUE),
    (490, 'SBE', TRUE),
    (491, 'SBEQ', TRUE),
    (492, 'SDM', TRUE),
    (493, 'SEDIMENTAÇÃO', TRUE),
    (494, 'SEDIMENTO', TRUE),
    (495, 'SEDIMENTOLOGIA', TRUE),
    (496, 'SEMINÁRIO', TRUE),
    (
        497,
        'SENSORES ORBITAIS',
        TRUE
    ),
    (
        498,
        'SENSORIAMENTO REMOTO',
        TRUE
    ),
    (499, 'TAXONÔMIA', TRUE),
    (500, 'SERPERTES', TRUE),
    (501, 'SERRA DO SINCORÁ', TRUE),
    (
        502,
        'SERVIÇOS ECOSSISTÊMICOS',
        TRUE
    ),
    (503, 'SIG', TRUE),
    (504, 'SILICICLÁSTICO', TRUE),
    (505, 'SIMILARIDADE', TRUE),
    (
        506,
        'SISTEMA DE ALERTA DE INUNDAÇÃO',
        TRUE
    ),
    (
        507,
        'SISTEMAS FERRUGINOSOS',
        TRUE
    ),
    (508, 'SOFTWARE', TRUE),
    (509, 'SOLO', TRUE),
    (510, 'SOLO TROPICAL', TRUE),
    (511, 'SRS', TRUE),
    (512, 'STENODERMATINAE', TRUE),
    (513, 'STYGOBITIC', TRUE),
    (514, 'SUBAQUÁTICAS', TRUE),
    (515, 'SUBMARINAS', TRUE),
    (516, 'SUBTERRÂNEO', TRUE),
    (517, 'SUMIDOUROS', TRUE),
    (
        518,
        'SUPERFÍCIE DE DESLIZAMENTO',
        TRUE
    ),
    (519, 'SYNOCHETA', TRUE),
    (
        520,
        'SÍTIOS ARQUEOLÓGICOS',
        TRUE
    ),
    (521, 'TAFÔNOMIA', TRUE),
    (
        522,
        'TATUZINHO-DE-JARDIM',
        TRUE
    ),
    (523, 'TAXONOMIA', TRUE),
    (
        524,
        'TAXONOMIA FUNGICA',
        TRUE
    ),
    (
        525,
        'TAXONOMIA INTEGRATIVA',
        TRUE
    ),
    (
        526,
        'TAXONOMIA PLATELMINTOS TROGLÓBIOS',
        TRUE
    ),
    (527, 'TECNOLOGIA', TRUE),
    (
        528,
        'TEORES TOTAIS DE METAIS',
        TRUE
    ),
    (529, 'TERRA INDÍGENA', TRUE),
    (530, 'THEOBROMA CACAO', TRUE),
    (531, 'TOLERÂNCIA', TRUE),
    (532, 'TOPOGRAFIA', TRUE),
    (533, 'TRADICIONAIS', TRUE),
    (
        534,
        'TRANSPORTE DE HILBERT',
        TRUE
    ),
    (535, 'TRAÇADORES', TRUE),
    (
        536,
        'TRAÇADORES CORANTES FLUORESCENTES',
        TRUE
    ),
    (537, 'TRICLADIDA', TRUE),
    (538, 'TROGLOFAUNA', TRUE),
    (539, 'TROGLÓBIO', TRUE),
    (540, 'TROGLÓBIOS', TRUE),
    (541, 'TUFAS CALCÁREAS', TRUE),
    (542, 'TURBIDEZ', TRUE),
    (543, 'TÁXONS NOVOS', TRUE),
    (
        544,
        'TÉCNICAS DIRETAS E INDIRETAS DE MAPEAMENTO',
        TRUE
    ),
    (545, 'TÉCNICO', TRUE),
    (546, 'TÉRMICO', TRUE),
    (547, 'UAV', TRUE),
    (548, 'UFLA NATURALIST', TRUE),
    (
        549,
        'UNIDADE DE CONSERVAÇÃO',
        TRUE
    ),
    (
        550,
        'UNIDADES DE CONSERVAÇÃO',
        TRUE
    ),
    (551, 'USO DA TERRA', TRUE),
    (552, 'VALES', TRUE),
    (553, 'VALES CEGOS', TRUE),
    (554, 'VALES SECOS', TRUE),
    (555, 'VANT', TRUE),
    (556, 'VARIAÇÃO SAZONAL', TRUE),
    (
        557,
        'VARIÁVEIS BIOCLIMÁTICAS',
        TRUE
    ),
    (558, 'VERTEBRADO', TRUE),
    (559, 'VICARIÂNCIA', TRUE),
    (560, 'VISITANTE', TRUE),
    (561, 'VLF-EM', TRUE),
    (562, 'VLFEM', TRUE),
    (563, 'VOLUME 2', TRUE),
    (564, 'VOLUME 3', TRUE),
    (565, 'VOLUME 4', TRUE),
    (566, 'VOLUME 5', TRUE),
    (567, 'VOLUME 6', TRUE),
    (568, 'VOLUME 7', TRUE),
    (
        569,
        'VULNERABILIDADE INTRÍNSECA',
        TRUE
    ),
    (570, 'WALLACEANA', TRUE),
    (571, 'WOODLICE', TRUE),
    (572, 'ZONAÇÃO', TRUE),
    (573, 'ZOOPLANCTON', TRUE),
    (574, 'ZYGOPTERA', TRUE),
    (575, 'FORCIPATORINA', TRUE),
    (576, 'REICHEIINA', TRUE),
    (
        577,
        'NORDESTE BRASILEIRO',
        TRUE
    ),
    (578, 'TROGLOMÓRFICO', TRUE),
    (579, 'PEIXE ELÉTRICO', TRUE),
    (580, 'EOD', TRUE),
    (581, 'TERRITÓRIO', TRUE),
    (582, 'TROGLOMORFISMO', TRUE),
    (
        583,
        'INSETOS SEMIAQUÁTICOS',
        TRUE
    ),
    (
        584,
        'SERRA DA BODOQUENA',
        TRUE
    ),
    (
        585,
        'SERRA DO RAMALHO TROGLÓBIO',
        TRUE
    ),
    (
        586,
        'PEIXE CAVERNÍCOLA',
        TRUE
    ),
    (587, 'GUANO', TRUE),
    (588, 'REPRODUÇÃO', TRUE),
    (589, 'HEPTAPTERIDAE', TRUE),
    (
        590,
        'CHAPADA DIAMANTINA',
        TRUE
    ),
    (
        591,
        'CAVERNAS BRASILEIRAS',
        TRUE
    ),
    (592, 'CENTIPEDE', TRUE),
    (593, 'ALTO RIBEIRA', TRUE),
    (594, 'METAGENOMAS', TRUE),
    (595, 'METABOLISMO', TRUE),
    (596, 'PROCARIONTES', TRUE),
    (597, 'METABOLITOS', TRUE),
    (598, 'MULTI-OMICS', TRUE),
    (599, 'NOVO GÊNERO', TRUE),
    (
        600,
        'SUDOESTE BRASILEIRO',
        TRUE
    ),
    (
        601,
        'ESPÉCIES TROGLÓBIAS',
        TRUE
    ),
    (
        602,
        'CAVERNAS FERRUGIONOSAS',
        TRUE
    ),
    (
        603,
        'ARQUIPÉLAGO DE FERNANDO DE NORONHA',
        TRUE
    ),
    (
        604,
        'NOVAS OCORRÊNCIAS',
        TRUE
    ),
    (605, 'PSEUDOESCROPIÕES', TRUE),
    (606, 'ATLÂNTICO SUL', TRUE),
    (607, 'ZALMOXOIDEA', TRUE),
    (608, 'RELÍCTO', TRUE),
    (
        609,
        'DIMORFISMO SEXUAL',
        TRUE
    ),
    (
        610,
        'ESPÉCIES CAVERNÍCOLAS',
        TRUE
    ),
    (611, 'ADAPTAÇÃO', TRUE),
    (612, 'COMPENSAÇÃO', TRUE),
    (
        613,
        'FORMAÇÃO FERRÍFERA',
        TRUE
    ),
    (
        614,
        'RIGÃO SUL DO ESPINHAÇO',
        TRUE
    ),
    (615, 'DIVERSIDADE BETA', TRUE),
    (616, 'CONECTIVIDADE', TRUE),
    (
        617,
        'MUDANÇAS CLIMÁTICAS',
        TRUE
    ),
    (618, 'ECOSSISTEMAS', TRUE),
    (619, 'CICLO D''ÁGUA', TRUE),
    (620, 'CAENOGASTROPODA', TRUE),
    (621, 'GONDWANA', TRUE),
    (
        622,
        'FILOGÊNIA MOLECULAR',
        TRUE
    ),
    (623, 'SPIRIPOCKIA', TRUE),
    (624, 'TRUNCATELLOIDEA', TRUE),
    (625, 'GASTROPODA', TRUE),
    (
        626,
        'ESPÉCIES TROGLÓBIA',
        TRUE
    ),
    (
        627,
        'VARIÁVEIS ABIÓTICAS',
        TRUE
    ),
    (628, 'BETA DIVERSIDADE', TRUE),
    (629, 'BACIAS RIOS', TRUE),
    (630, 'PLANÁRIA', TRUE),
    (631, 'CALCÁRIO', TRUE),
    (632, 'ARENITO', TRUE),
    (633, 'AMÉRICA DO SUL', TRUE),
    (
        634,
        'ANFÍPODOS HIPOGENOS',
        TRUE
    ),
    (
        635,
        'DIVERSIDADE SUBTERRANEAN',
        TRUE
    ),
    (
        636,
        'ANFÍPODOS DE CAVERNAS',
        TRUE
    ),
    (637, 'CRUSTÁCEO', TRUE),
    (638, 'MORFOLOGIA', TRUE),
    (639, 'BRAZIL', TRUE),
    (640, 'NOVA OCORRÊNCIA', TRUE),
    (641, 'SUBTRATO', TRUE),
    (642, 'FLUXO DE ÁGUA', TRUE),
    (643, 'TROGLÓFILOS', TRUE),
    (644, 'LEVANTAMENTO', TRUE),
    (645, 'SHORTFALL', TRUE),
    (646, 'BioTroglophileBR', TRUE),
    (647, 'MINIGUIA', TRUE),
    (648, 'UFSCAR', TRUE),
    (649, 'FOLDER', TRUE),
    (
        650,
        'CAVERNÍCOLA DA VEZ',
        TRUE
    ),
    (651, 'MATA ATLÂNTICA', TRUE),
    (
        652,
        'TATUZINHOS-DE-JARDIM',
        TRUE
    ),
    (653, 'NEOTRÓPICO', TRUE),
    (654, 'GRUTA', TRUE),
    (655, 'SYNARMADILLO', TRUE),
    (656, 'VENEZILLO', TRUE),
    (
        657,
        'CANRANGUEJO-DE-ÁGUA-DOCE',
        TRUE
    ),
    (658, 'TRICHODACTYLUS', TRUE),
    (659, 'TROGLÓFILO', TRUE),
    (660, 'BANCO GENÉTICO', TRUE),
    (661, 'DECAPODA', TRUE),
    (
        662,
        'DIVERSIDADE TAXONÔMICA',
        TRUE
    ),
    (
        663,
        'REPOSITÓRIO CIENTÍFICO',
        TRUE
    ),
    (
        664,
        'INTERIOR PAULISTA',
        TRUE
    ),
    (
        665,
        'IMPACTO ANTRÓPICOS',
        TRUE
    ),
    (666, 'HYALELLA', TRUE),
    (
        667,
        'AMBIENTE HIPOGENO',
        TRUE
    ),
    (668, 'SUL', TRUE),
    (669, 'ANFÍPODOS', TRUE),
    (
        670,
        'PARQUE ESTADUAL INTERVALES',
        TRUE
    ),
    (
        671,
        'ANATOMIA COMPARADA',
        TRUE
    ),
    (
        672,
        'PIMELODELLA KRONEI',
        TRUE
    ),
    (
        673,
        'PEIXES SUBTERRÂNEOS',
        TRUE
    ),
    (674, 'TROGLOMORFISMOS', TRUE),
    (675, 'AÇUNGUI', TRUE),
    (
        676,
        'ESTADO DE SÃO PAULO',
        TRUE
    ),
    (677, 'HIPÓGEO', TRUE),
    (678, 'IMAGEM 3D', TRUE),
    (
        679,
        'NANOTOMOGRAFIA COMPUTADORIZADA',
        TRUE
    ),
    (680, 'PIOLHO-DE-COBRA', TRUE),
    (681, 'PMA', TRUE),
    (682, 'FAUNA', TRUE),
    (683, 'PEIXES', TRUE),
    (684, 'BOTUCATU', TRUE),
    (685, 'CAVIDADES', TRUE),
    (686, 'FAUNÍSTICA', TRUE),
    (687, 'ITAQUERI', TRUE),
    (688, 'ARMADILLIDAE', TRUE),
    (689, 'ISÓPODES', TRUE),
    (690, 'MICROHABITATS', TRUE),
    (691, 'BOTHRIURIDAE', TRUE),
    (692, 'BUTHIDAE', TRUE),
    (693, 'MIGALOMORFAS', TRUE),
    (694, 'SAPO', TRUE),
    (695, 'SERRA', TRUE),
    (696, 'CERRRADO', TRUE),
    (
        697,
        'HABITAT SUBTERRÂNEO',
        TRUE
    ),
    (
        698,
        'DIVERSIDADE ESCONDIDA',
        TRUE
    ),
    (699, 'MODELAGEM 3D', TRUE),
    (700, 'LiDAR', TRUE),
    (701, 'FOTOGRAMETRIA', TRUE),
    (702, 'RECONSTRUÇÃO 3D', TRUE),
    (703, 'BAIXO CUSTO', TRUE),
    (704, 'SENSORES RGB-D', TRUE),
    (
        705,
        'RECONSTRUÇÃO DE BAIXO CUSTO',
        TRUE
    ),
    (
        706,
        'LEVANTAMENTO DE CAVERNAS',
        TRUE
    ),
    (
        707,
        'INVENTÁRIO DE CAVIDADES',
        TRUE
    ),
    (
        708,
        'CADASTRAMENTO ESPELEOLÓGICO',
        TRUE
    ),
    (
        709,
        'CONSERVAÇÃO PATRIMÔNIO ESPELEOLÓGICO',
        TRUE
    ),
    (710, 'GLOSSOPHAGINAE', TRUE),
    (
        711,
        'VARIAÇÃO MORFOLÓGICA',
        TRUE
    ),
    (
        712,
        'DETECÇÃO DE NÉCTAR',
        TRUE
    ),
    (713, 'ANOURA CADENAI', TRUE),
    (714, 'MICROCLIMA', TRUE),
    (
        715,
        'MONITORAMENTO ACÚSTICO',
        TRUE
    ),
    (
        716,
        'MORCEGOS INSETÍVOROS AÉREOS',
        TRUE
    ),
    (717, 'PANTANAL', TRUE),
    (718, 'ANOMALIAS DENTAL', TRUE),
    (719, 'ASAS', TRUE),
    (720, 'ACONDROPLASIA', TRUE),
    (
        721,
        'CAROLLIA PERSPICILLATA',
        TRUE
    ),
    (722, 'VÍDEO', TRUE),
    (723, 'CECAV', TRUE),
    (724, 'DIVULGAÇÃO', TRUE),
    (725, 'INSTITUCIONAL', TRUE),
    (726, 'CARSTE DA BAHIA', TRUE),
    (
        727,
        'CAVERNAS DA BAHIA',
        TRUE
    ),
    (728, 'OPILIOACARIDA', TRUE),
    (729, 'ARACNÍDEO', TRUE),
    (
        730,
        'ECOLOGIA DE POPULAÇÃO',
        TRUE
    ),
    (731, 'BIOFILME', TRUE),
    (
        732,
        'INSETOS CAVERNÍCOLAS',
        TRUE
    ),
    (733, 'DUGESIIDAE', TRUE),
    (734, 'BACIA AMAZÔNICA', TRUE),
    (
        735,
        'FLORESTA ATLÂNTICA',
        TRUE
    ),
    (
        736,
        'GRUPO GEOMORFOLÓGICO AÇUNGUI',
        TRUE
    ),
    (
        737,
        'GRUPO GEOMORFOLÓGICO BAMBUÍ',
        TRUE
    ),
    (
        738,
        'ESPÉCIE SUBTERRÂNEA',
        TRUE
    ),
    (739, 'CAVERNÍCOLA', TRUE),
    (740, 'CARNOGASTROPODA', TRUE),
    (741, 'CHARACIDAE', TRUE),
    (742, 'ARDISTOMINA', TRUE),
    (
        743,
        'ARQUIPÉLOGO DE FERNANDO DE NORONHA',
        TRUE
    ),
    (
        744,
        'TAXONÔMIA INTEGRATIVA',
        TRUE
    ),
    (745, 'AMEAÇADA', TRUE),
    (
        746,
        'COMPLEXO DE ESPÉCIES',
        TRUE
    ),
    (
        747,
        'CONSERVAÇÃO DE CAVERNAS',
        TRUE
    ),
    (
        748,
        'BIODIVERSDADE SUBTERRÂNEA',
        TRUE
    ),
    (749, 'ANÁLISE SWOT', TRUE),
    (750, 'IMPACTO HUMANO', TRUE),
    (751, 'CRESCIMENTO', TRUE),
    (752, 'CARABID', TRUE),
    (
        753,
        'DISTRIBUIÇÃO GEOGRÁFICA',
        TRUE
    ),
    (754, 'SAPOS', TRUE),
    (755, 'CTENINAE', TRUE),
    (
        756,
        'BESOURO TERRESTRE',
        TRUE
    ),
    (
        757,
        'HABITAT CAVERNÍCOLA',
        TRUE
    ),
    (
        758,
        'HABITAR CAVERNÍCOLA',
        TRUE
    ),
    (
        759,
        'PEIXES CAVERNÍCOLAS',
        TRUE
    ),
    (
        760,
        'HABITANTES DE CAVERNAS',
        TRUE
    ),
    (761, 'ESPÉCIE ENDÊMICA', TRUE),
    (762, 'CLIVININA', TRUE),
    (
        763,
        'SERRA DO RAMALHO. TROGLÓBIO',
        TRUE
    ),
    (764, 'AEGLIDAE', TRUE),
    (
        765,
        'RECUPERAÇÃO AMBIENTAL',
        TRUE
    ),
    (
        766,
        'CARBONATOS DA BAHIA',
        TRUE
    ),
    (767, 'HIPOGÊNICO', TRUE),
    (768, 'CHTHONIINAE', TRUE),
    (769, 'IUCN', TRUE),
    (770, 'FREÁTICO', TRUE),
    (771, 'MOVIMENTOS', TRUE),
    (772, 'ESPÉCIE AMEAÇADA', TRUE),
    (
        773,
        'FAUNA ESTIGOBIONTE',
        TRUE
    ),
    (
        774,
        'ESPONJAS CONTINENTAL',
        TRUE
    ),
    (
        775,
        'DIVERSIDADE BIOLÓGICA',
        TRUE
    ),
    (776, 'ROCHA ÍGNEA', TRUE),
    (
        777,
        'GRUPO GEOMORFOLÓGICO CASA NOVA',
        TRUE
    ),
    (778, 'HELICINIDAE', TRUE),
    (779, 'STRONGYLOSOMIDES', TRUE),
    (780, 'IULIDESMUS', TRUE),
    (781, 'PHANEROMERIUM', TRUE),
    (782, 'SEQUÊNCIA RNA', TRUE),
    (
        783,
        'AMBIENTES SUBTERRÂNEOS',
        TRUE
    ),
    (784, 'NERITIMORPHA', TRUE),
    (785, 'SETOR PRODUTIVO', TRUE),
    (
        786,
        'CAVERNAS TURÍSTICAS',
        TRUE
    ),
    (
        787,
        'TAXONOMIA. PLATELMINTOS TROGLÓBIOS',
        TRUE
    ),
    (
        788,
        'REGIONALIZAÇÃO DO CARSTE',
        TRUE
    ),
    (
        789,
        'GESTÃO DE CAVERNAS',
        TRUE
    ),
    (790, 'CONSERVATION', TRUE),
    (791, 'EPICARSTE', TRUE),
    (792, 'SAO DOMINGOS', TRUE),
    (
        793,
        'FORMAÇÃO CARSTICA',
        TRUE
    ),
    (794, 'RIACHOS HIPÓGEOS', TRUE),
    (795, 'CYLINDRONISCUS', TRUE),
    (796, 'STYLOMMATOPHORA', TRUE),
    (797, 'SCOLODONTIDAE', TRUE),
    (798, 'ROTUNDOTERGUM', TRUE),
    (799, 'ONCIUROSOMA', TRUE),
    (800, 'MOOJENODESMUS', TRUE),
    (801, 'POMATIOPSIDAE', TRUE),
    (
        802,
        'FORMAÇÃO UTIARITI',
        TRUE
    ),
    (
        803,
        'DIFERENCIAL DE EXPRESSÃO GÊNICA',
        TRUE
    ),
    (804, 'SPELAEOGRIPHACEA', TRUE),
    (805, 'ENDEMIC', TRUE),
    (806, 'ESPÉCIE', TRUE),
    (807, 'STREPTAXIDAE', TRUE),
    (
        808,
        'FLORESTAS TROPICAIS SECAS',
        TRUE
    ),
    (809, 'CLIMA SEMI ÁRIDO', TRUE),
    (810, 'TOMICHIIDAE', TRUE),
    (811, 'SUBTERRÂNEA', TRUE),
    (812, 'STYLONISCIDAE', TRUE),
    (813, 'PECTENONISCUS', TRUE),
    (
        814,
        'MAPEAMENTO PEDAGÓGICO',
        TRUE
    ),
    (815, 'PALEOCLIO', TRUE),
    (
        816,
        'QUADRILÁTERO FERRUGUEIRO',
        TRUE
    ),
    (817, 'SILICISLÁSTICO', TRUE),
    (818, 'CURSO', TRUE),
    (819, 'PAN CAVERNAS', TRUE),
    (820, 'LICENCIAMENTO', TRUE)
ON CONFLICT (nome) DO NOTHING;