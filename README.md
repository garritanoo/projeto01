# Projeto: Airline Loyalty Campaign
Dataset Airline Loaylty Campaign: [Airline Loaylty Campaign](https://www.kaggle.com/datasets/agungpambudi/airline-loyalty-campaign-program-impact-on-flights)

## 1. Problema de negócio

Uma companhia área gostaria de realizar um campanha de marketing para aumentar o número de passageiros que participam do programa de fidelidade da empresa.

O programa de fidelidade da empresa oferece 3 tipos de benefícios, de acordo com o uso e o engajamento do passageiro com a empresa, ao longo do tempo. Esses níveis de prêmios são representados pelos tipos de cartões de fidelidade.

O programa de fidelidade possui 3 cartões de participação: Star, Nova e Aurora. Cada cartão possui níveis de benefícios e prêmios, sendo o Star com menos e o Aurora com mais prêmios.

O time de marketing forneceu uma base de novos clientes para o time comercial entrar em contato e fazer a oferta da assinatura do programa de fidelidade. Porém, não há vendedores suficientes no time comercial para abordar todos os clientes, obrigando o time alcançarem altas taxas de compra da assinatura, para baterem a meta.

Para alcançar a meta o time comercial precisa entrar em contato com o cliente, sabendo qual a probabilidade dele assinar o cartão Star, Nova ou Aurora. Assim, o vendedor consegue oferecer o cartão de maior probabilidade, diminuindo o tempo da venda e aumentando a receita, através da oferta do cartão mais adequado para o perfil de uso de cada cliente.

Por exemplo:

> **O cliente A tem  probabilidade de 70% de assinar o cartão Star, 20% de assinar o cartão Nova e 10% de assinar o cartão Aurora.**

Como essa informação em mãos, o vendedor pode oferecer para o cliente A, o cartão Star, diretamente.

## 2. Premissas do negócio

1. Análise foi realizada com dados entre os anos de 2017 e 2018

## 3. Descrição dos dados

| Field |	Description |
| :---- | :---------- |
| Loyalty Number | Número de identificação única do cliente |
| Year |	Ano |
Month |	Mês |
Flights Booked |	Número de vos reservados |
Flights with Companions | 	Número de vôos reservados com acompanhante |
Total Flights | 	Quantidade de vôos reservados e vôos com acompanhante |
Distance | 	Distância percorrida (km) |
Points Accumulated | 	Pontos de fidelidade acumulado |
Points Redeemed |	Pontos de fidelidade resgatados |
| Dollar Cost Points Redeemed |	Valor em dólar dos pontos resgatados |


## 4. Estratégia da solução

Um painel estratégico com visualização de todos os clientes com potencial para aquisição do cartão Star.

Abaixo segue um modelo do painel:

![Imagem da Aplicação](https://docs.google.com/drawings/d/e/2PACX-1vR2amL0k041GIlv8OYdRQzXVDpJ3i8VQjc9P9ePCh_qRnDPOigM4DN851J0hifDn8IZfGHlhMfB5FgT/pub?w=960&h=720)

## 5. Insights

1. Distancia média percorrida foi de 1.208km

## 6. O produto final

Painel online hospedado em Cloud e disponível para acesso em qualquer dispositivo conectado a internet.

O painel pode ser acessado através do link:
[Projeto01 - Previsão de Clientes](https://huggingface.co/spaces/garritanoo/projeto01_previsao_clientes)

## 7. Conclusão

O objetivo desse projeto foi eterminar qual a probabilidade de cada cliente assinar cada um dos 3 cartões do programa de fidelidade. 

## 8. Próximos passos

1. Melhorar o treinamento do modelo de machine learning
2. Criação de abas para uma melhor navegação:
3. Incluir mais insights

# Próximos passos

1. Melhorar o treinamento do modelo de machine learning
2. Criação de abas para uma melhor navegação:
3. Incluir mais insights

