# Ilustrações

## Estilo

Realismo pictórico cinematográfico, na tradição da arte sacra clássica, com cenários e roupas fiéis ao primeiro século no Oriente Médio. O prompt de estilo comum está em `ferramentas/quadros.py` (`ESTILO`).

Regras:

- Deus Pai aparece apenas como luz e glória, nunca com rosto humano.
- O rosto de Cristo glorificado é luz intensa (Ap 1:16), sem traços definidos.
- Criaturas simbólicas são realistas, mas sem sangue nem horror gráfico.
- Multidões com pessoas de todas as etnias, idades e povos (Ap 5:9; 7:9).
- Quando o texto explica o símbolo, a imagem segue a explicação do texto.

## Fluxo de produção

1. **Quadro:** cada cena está em `data/estudo/apocalipse-quadros.json`, com referência, descrição literal, raízes no AT e prompt.
2. **Geração:** prompt de estilo + prompt da cena, sempre com a mesma folha de personagens (João, anjos, o Cordeiro) para manter consistência.
3. **Revisão:** uma pessoa confere a fidelidade ao texto e a sensibilidade da imagem.
4. **Acessibilidade:** o campo `alt` recebe a descrição final da imagem.
5. **Publicação:** salvar em `img/apocalipse/<id>.webp` (1600 px de largura) e preencher o campo `imagem` do quadro.

## Situação

- 4 rascunhos em estilo vitral (caps. 1 a 4) foram gerados no Canva antes da mudança para o estilo realista.
- As 61 ilustrações realistas aguardam uma ferramenta de geração com créditos.
