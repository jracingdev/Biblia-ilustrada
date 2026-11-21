# Bíblia Ilustrada

Plataforma web pública, interativa e acessível para ler e estudar a Bíblia, livro por livro, com ilustrações. O primeiro livro é **Apocalipse**.

## O que já existe (Apocalipse)

- Texto completo dos 22 capítulos (404 versículos), com leitura em voz alta.
- Estudo por capítulo: resumo, lições, pergunta para reflexão e quiz.
- **Raízes no Antigo Testamento:** 187 conexões com 288 passagens de 26 livros do AT, com o texto do AT aberto ao lado, e uma linha do tempo em arcos que liga cada fato do AT, na sua época, ao versículo de Apocalipse.
- **Quadros:** 61 cenas figurativas do livro, cada uma com referência, raízes no AT e prompt para a ilustração realista.
- Símbolos explicados (separando o que o texto explica do que é interpretação), mapa das 7 igrejas e as 4 linhas de interpretação.
- Acessibilidade: texto até 180%, alto contraste, tema escuro, letra de alta legibilidade, teclado e leitor de tela (meta WCAG 2.2 AA).

## Como rodar

É um site estático, sem build. Sirva a pasta com qualquer servidor HTTP:

```bash
python3 -m http.server 8000
# abra http://localhost:8000
```

Funciona também no GitHub Pages (há um `.nojekyll` na raiz).

## Estrutura dos dados

```
data/
  fontes.json                      versões bíblicas avaliadas e licenças
  livros.json                      os 66 livros e o status de cada um
  textos/<versao>/<livro>.json     texto por capítulo e versículo
  textos/<versao>/at-<livro>.json  trechos do AT usados nas conexões
  estudo/<livro>.json              seções, resumos, lições, símbolos, quiz
  estudo/<livro>-at.json           conexões com o Antigo Testamento
  estudo/<livro>-quadros.json      quadros figurativos e prompts de ilustração
  estudo/linha-do-tempo.json       épocas dos livros do AT e fatos da linha do tempo em arcos
  fonte-original/biblialivre.json  Bíblia Livre completa (base para os próximos livros)
ferramentas/
  gerar_dados.py                   gera os JSON acima a partir da fonte original
  referencias_at.py                lista editável das conexões com o AT
  quadros.py                       lista editável dos quadros e do estilo de arte
```

Para trocar a versão do texto, adicione a pasta `data/textos/<versao>/` e mude `padrao` em `data/fontes.json`.

## Texto bíblico e licença

Todas as Escrituras em português citadas são da Bíblia Livre (BLIVRE), Copyright © Diego Santos, Mario Sérgio, e Marco Teles, http://sites.google.com/site/biblialivre/ - fevereiro de 2018. Licença Creative Commons Atribuição 4.0 Brasil (http://creativecommons.org/licenses/by/4.0/br/). Reprodução permitida desde que devidamente mencionados fonte e autores.

O texto foi convertido para JSON por livro, capítulo e versículo, sem alterar as palavras. Os autores da Bíblia Livre não endossam necessariamente esta edição. A licença foi conferida em https://ebible.org/porbr2018/copyright.htm.

Não usamos ARA (© Sociedade Bíblica do Brasil) nem BKJ 1611 (© BV Films), que exigem licença.

## Ilustrações

Veja [docs/ilustracoes.md](docs/ilustracoes.md).

## Publicação

O site é publicado no GitHub Pages pelo workflow `.github/workflows/pages.yml` a cada push na branch `main`, no endereço https://jracingdev.github.io/Biblia-ilustrada/. Antes do primeiro deploy, ative em Settings → Pages → Source: "GitHub Actions". Os pull requests passam pela validação dos dados (`.github/workflows/validar.yml`).

## Bíblia inteira

- `#livros`: seletor dos 66 livros; `#livro-<slug>-<cap>`: leitura de qualquer livro (Bíblia Livre).
- `#biblia`: arcos de toda a Bíblia (24 mil ligações mais fortes entre os 1.189 capítulos).
- `#conexoes-<slug>`: um livro-tema e suas ligações com os demais, com os pares de versículos.
- Dados gerados por `ferramentas/gerar_biblia.py` a partir das referências cruzadas do
  [OpenBible.info](https://www.openbible.info/labs/cross-references/) (CC BY), baseadas no
  Treasury of Scripture Knowledge (domínio público).
