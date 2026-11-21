# Gera data/estudo/apocalipse-historia.json: fontes EXTRABÍBLICAS ligadas ao Apocalipse
import json, sys
H = []
def h(id, titulo, refs, tipo, fonte, referencia, data_fonte, data_evento, resumo, relacao, grau, link=None):
    H.append({"id":id,"titulo":titulo,"refs":refs,"tipo":tipo,"fonte":fonte,"referencia":referencia,"data_fonte":data_fonte,
              "data_evento":data_evento,"resumo":resumo,"relacao":relacao,"grau":grau,**({"link":link} if link else {})})
A, P = "historiador antigo", "imprensa e arqueologia"
D, I = "documentado", "associacao"

h("patmos-domiciano","João exilado em Patmos sob Domiciano",["1:9"],A,"Eusébio de Cesareia, História Eclesiástica","livro 3, cap. 18","c. 325 d.C.","c. 95 d.C.",
  "Eusébio registra a tradição de que o apóstolo João foi condenado a viver na ilha de Patmos durante a perseguição de Domiciano.",
  "Confirma fora da Bíblia o cenário de 1:9: João está em Patmos \"por causa da palavra de Deus\".",D)
h("ireneu-data","Data do Apocalipse: fim do reinado de Domiciano",["1:1","13:18"],A,"Ireneu de Lião, Contra as Heresias","livro 5, cap. 30, §1 e §3","c. 180 d.C.","c. 95 d.C.",
  "Ireneu diz que a visão foi vista quase em sua própria geração, no fim do reinado de Domiciano. No mesmo capítulo comenta manuscritos que traziam 616 em vez de 666.",
  "É o testemunho mais antigo sobre a data do livro (c. 95 d.C.) e sobre a variante do número da besta.",D)
h("patmos-plinio","Patmos entre as ilhas do Egeu",["1:9"],A,"Plínio, o Velho, História Natural","livro 4, cap. 12 (§69)","c. 77 d.C.","séc. I d.C.",
  "Plínio lista Patmos entre as ilhas Espórades, perto da costa da Ásia. Ilhas pequenas eram usadas por Roma como lugar de desterro.",
  "Situa a ilha da visão, a cerca de 100 km de Éfeso por mar.",D)
h("domiciano-deus","Domiciano exigia ser chamado \"Senhor e Deus\"",["4:11","13:4","13:8"],A,"Suetônio, A Vida dos Doze Césares: Domiciano","cap. 13","c. 121 d.C.","81–96 d.C.",
  "Suetônio conta que Domiciano fazia seus procuradores começarem cartas oficiais com a fórmula \"nosso Senhor e Deus\" (dominus et deus noster).",
  "Em 4:11 os anciãos dão esse título ao Criador: \"Digno és, Senhor e Deus nosso\". O culto ao imperador é o pano de fundo da adoração à besta.",I)
h("domiciano-clemente","Execução de Flávio Clemente e exílio de Domitila",["2:10","2:13"],A,"Dião Cássio, História Romana","livro 67, cap. 14","c. 230 d.C.","95 d.C.",
  "Domiciano mandou matar o cônsul Flávio Clemente, seu primo, e exilou a esposa dele, Flávia Domitila, sob acusação de \"ateísmo\" e de adotar costumes judaicos. Muitos outros foram condenados pelo mesmo motivo.",
  "Mostra o clima de acusação contra quem recusava os deuses de Roma, o mesmo das cartas às igrejas.",I)
h("nero-64","Nero persegue os cristãos após o incêndio de Roma",["6:9","13:7","17:6"],A,"Tácito, Anais","livro 15, cap. 44","c. 116 d.C.","64 d.C.",
  "Depois do grande incêndio de Roma, Nero culpou os cristãos. Tácito descreve execuções cruéis: alguns foram queimados como tochas nos jardins do imperador.",
  "É a primeira perseguição oficial aos cristãos. Ajuda a entender as almas dos mártires (6:9) e a mulher \"embriagada com o sangue dos santos\" (17:6).",D)
h("nero-redivivo","A lenda de Nero que voltaria",["13:3","17:8","17:11"],A,"Tácito, Histórias; Suetônio, Nero","Histórias 2.8; Nero 57","c. 110 e c. 121 d.C.","69 d.C. em diante",
  "Depois da morte de Nero (68 d.C.), correu o boato de que ele estava vivo e voltaria do Oriente. Apareceram impostores dizendo ser Nero.",
  "Muitos estudiosos veem aqui o pano de fundo da besta \"ferida de morte\" que volta a viver (13:3) e da que \"era e não é\" (17:8).",I)
h("plinio-cristaos","Cristãos obrigados a sacrificar à imagem do imperador",["13:15","2:13"],A,"Plínio, o Jovem, Cartas","livro 10, carta 96","c. 112 d.C.","c. 112 d.C.",
  "Governador da Bitínia, Plínio escreve ao imperador Trajano: soltava quem invocava os deuses, oferecia incenso e vinho à imagem do imperador e amaldiçoava Cristo. Quem se recusava era executado.",
  "É o retrato, fora da Bíblia, de 13:15: quem não adorasse a imagem era morto.",D)
h("vinho-domiciano","O edito do vinho de Domiciano",["6:6"],A,"Suetônio, Domiciano","cap. 7 (§2) e cap. 14","c. 121 d.C.","c. 92 d.C.",
  "Num ano de muito vinho e pouco trigo, Domiciano proibiu plantar novas vinhas na Itália e mandou cortar metade das vinhas das províncias. Depois voltou atrás.",
  "Alguns intérpretes ligam a isso a voz do terceiro selo: trigo caríssimo, mas \"não danifiques o azeite e o vinho\" (6:6).",I)
h("jerusalem-70","Destruição de Jerusalém e do templo",["11:1","11:2"],A,"Flávio Josefo, Guerra dos Judeus","livro 6","c. 75 d.C.","70 d.C.",
  "Josefo, testemunha ocular, narra o cerco de Tito e o incêndio do templo de Jerusalém em 70 d.C.",
  "Para a leitura preterista, 11:1-2 (o átrio pisado pelas nações) alude a esse evento. Outras linhas leem o templo como símbolo da Igreja.",I)
h("vesuvio-79","A erupção do Vesúvio",["8:8"],A,"Plínio, o Jovem, Cartas","livro 6, cartas 16 e 20","c. 106 d.C.","24 de agosto de 79 d.C.",
  "Plínio descreve a nuvem que subiu do monte, as pedras em chamas e o mar recuando na baía de Nápoles, onde morreu seu tio.",
  "Alguns comentaristas lembram essa erupção, que impressionou todo o mundo romano, ao ler \"um grande monte ardendo em fogo foi lançado ao mar\" (8:8).",I)
h("laodiceia-terremoto","Laodiceia se reergue sozinha após o terremoto",["3:17"],A,"Tácito, Anais","livro 14, cap. 27","c. 116 d.C.","60 d.C.",
  "Laodiceia foi arruinada por um terremoto e se reconstruiu com os próprios recursos, sem ajuda de Roma.",
  "Ajuda a ouvir o orgulho da igreja local: \"Estou rica, enriqueci e de nada tenho falta\" (3:17).",I)
h("laodiceia-la-colirio","Lã negra e escola de medicina perto de Laodiceia",["3:18"],A,"Estrabão, Geografia","livro 12, cap. 8, §16 e §20","c. 20 d.C.","séc. I a.C. – I d.C.",
  "Estrabão elogia as ovelhas de lã negra e macia de Laodiceia e menciona uma famosa escola de medicina entre Laodiceia e Carura.",
  "Muitos veem nisso a ironia de 3:18: vestes brancas e colírio para quem se orgulhava da lã e da medicina.",I)
h("laodiceia-agua","Águas quentes de Hierápolis e frias de Colossos",["3:15","3:16"],A,"Estrabão, Geografia","livro 13, cap. 4, §14","c. 20 d.C.","séc. I",
  "Estrabão descreve as fontes termais de Hierápolis, vizinha de Laodiceia. Laodiceia recebia água por aqueduto, que chegava morna e cheia de calcário.",
  "Leitura comum de 3:15-16: nem quente como a água que cura, nem fria como a que refresca, mas morna.",I)
h("sardes-surpresa","Sardes tomada de surpresa duas vezes",["3:2","3:3"],A,"Heródoto, Histórias; Políbio, Histórias","Heródoto 1.84; Políbio 7.15-18","c. 430 a.C.; c. 150 a.C.","546 a.C. e 214 a.C.",
  "A acrópole de Sardes, tida como inexpugnável, caiu duas vezes porque ninguém vigiava: diante de Ciro e de Antíoco III, soldados escalaram o penhasco à noite.",
  "Ilumina o aviso: \"Sê vigilante… virei como ladrão\" (3:2-3).",I)
h("terremoto-17","O grande terremoto de 17 d.C. na Ásia",["3:12","6:12"],A,"Tácito, Anais; Estrabão, Geografia","Anais 2.47; Geografia 12.8.18","c. 116 d.C.; c. 20 d.C.","17 d.C.",
  "Um terremoto destruiu doze cidades da Ásia numa noite, entre elas Sardes e Filadélfia. Estrabão conta que em Filadélfia os tremores continuavam e muitos moravam fora da cidade.",
  "À igreja de Filadélfia Jesus promete: \"dele farei coluna no templo… e daí jamais sairá\" (3:12).",I)
h("pergamo-culto","Templo a Roma e Augusto em Pérgamo",["2:13"],A,"Tácito, Anais; Dião Cássio, História Romana","Anais 4.37; História 51.20","c. 116 d.C.; c. 230 d.C.","29 a.C.",
  "Pérgamo recebeu o primeiro templo da Ásia dedicado ao imperador vivo (Augusto) e à deusa Roma.",
  "É uma das explicações para \"onde está o trono de Satanás\" (2:13). Outras citam o grande altar de Zeus ou o santuário de Asclépio.",I)
h("esmirna-culto","Esmirna ganha o templo a Tibério",["2:8","2:10"],A,"Tácito, Anais","livro 4, caps. 55-56","c. 116 d.C.","26 d.C.",
  "Onze cidades da Ásia disputaram o direito de erguer um templo a Tibério; o Senado escolheu Esmirna pela antiga lealdade a Roma.",
  "Lealdade a Roma era o orgulho da cidade. A igreja recebe outra promessa de fidelidade: \"Sê fiel até a morte, e dar-te-ei a coroa da vida\" (2:10).",I)
h("efeso-porto","O porto de Éfeso enchendo de lodo",["2:5"],A,"Estrabão, Geografia","livro 14, cap. 1, §24","c. 20 d.C.","séc. II a.C. – I d.C.",
  "Estrabão conta que obras mal planejadas fizeram o porto de Éfeso acumular lodo. Com os séculos, o mar recuou e a cidade foi abandonada.",
  "Alguns leem aqui uma imagem para \"removerei do seu lugar o teu candelabro\" (2:5).",I)

h("pergamo-altar-berlim","Altar de Pérgamo: museu reabre em 2027",["2:13"],P,"The Associated Press (via ABC News)","\"Berlin's Pergamon Museum will reopen in mid-2027 as a lengthy restoration moves forward\"","4 de maio de 2026","altar: 197–156 a.C.",
  "O altar de Zeus de Pérgamo, levado para Berlim no séc. XIX, é a peça central do Museu Pergamon, fechado desde 2023. A fundação anunciou a reabertura em 4 de junho de 2027.",
  "O altar é um dos candidatos para o \"trono de Satanás\" de 2:13. Associação interpretativa.",I,"https://abcnews.com/International/wireStory/berlins-pergamon-museum-reopen-mid-2027-lengthy-restoration-132635570")
h("laodiceia-casa-igreja","Casa com igreja descoberta em Laodiceia",["3:14"],P,"Hürriyet Daily News","\"House with church unearthed in Laodicea\"","27 de outubro de 2020","casa usada desde o séc. I d.C.",
  "Escavações dirigidas pelo professor Celal Şimşek revelaram uma casa de 20 cômodos junto ao teatro norte; o salão leste foi convertido em igreja.",
  "Mostra a presença cristã na cidade da sétima carta.",D,"https://hurriyetdailynews.com/house-with-church-unearthed-in-laodicea-159481")
h("laodiceia-igreja-2011","Igreja do séc. IV em Laodiceia",["3:14"],P,"Biblical Archaeology Society (Bible History Daily), Noah Wiener","\"Laodicea Columns Reveal the Grandeur of an Early Christian Center\"","14 de agosto de 2013","igreja da época de Constantino (306–337)",
  "Relata colunas monumentais na ágora norte e lembra a igreja do séc. IV achada por radar em 2011, destruída por terremoto no início do séc. VII.",
  "A comunidade advertida em 3:14-22 seguiu viva e grande por séculos.",D,"https://www.biblicalarchaeology.org/daily/news/laodicea-columns-reveal-the-grandeur-of-an-early-christian-center/")
h("laodiceia-conselho","Salão de assembleia de 2.000 anos em Laodiceia",["3:14"],P,"Hürriyet Daily News","\"2,000-year-old assembly hall unearthed in Laodicea\"","4 de agosto de 2025","fim do séc. I a.C. até o séc. VII d.C.",
  "Na temporada de 2025 foi achado o prédio do conselho da cidade, para 600 a 800 membros. A Fox News (10 set. 2025) noticiou cruzes e um monograma cristão gravados na pedra.",
  "Era o centro político da cidade no tempo da carta de 3:14-22.",D,"https://www.hurriyetdailynews.com/2-000-year-old-assembly-hall-unearthed-in-laodicea-212147")
h("megido-mosaico","Mosaico \"ao Deus Jesus Cristo\" em Megido",["16:16"],P,"Autoridade de Antiguidades de Israel (via Ministério das Relações Exteriores de Israel); The Christian Century","\"Megiddo Prison dig yields rare 3rd-4th century Christian structure\"","novembro de 2005 (anúncio em 3 nov. 2005)","séc. III–IV d.C.",
  "Na prisão de Megido, o arqueólogo Yotam Tepper achou um salão com piso de mosaico, um peixe e inscrições gregas. Uma delas dedica uma mesa \"ao Deus Jesus Cristo\".",
  "Megido é o \"Har Megido\" de onde vem Armagedom (16:16). A ligação é de lugar, não de cumprimento profético.",D,"https://embassies.gov.il/MFA/IsraelExperience/religion/Pages/Megiddo%20Prison%20dig%20yields%20rare%203rd-4th%20century%20Christian%20structure%209-Nov-2005.aspx")

dados = {"livro":"apocalipse","aviso":"Fontes extrabíblicas. Não fazem parte do texto bíblico. Servem para entender o mundo em que o Apocalipse foi escrito. Quando a ligação é uma leitura de intérpretes, e não um fato documentado, isso vem marcado.",
 "graus":{"documentado":"Fato documentado","associacao":"Associação interpretativa"},"itens":H}
json.dump(dados, open(sys.argv[1],"w"), ensure_ascii=False, indent=1); print(len(H),"itens")
