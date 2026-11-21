# Gera data/estudo/apocalipse-palavras.json (palavras-chave nas línguas originais)
import json, sys
H = lambda l,t,s,ref="",lingua="hebraico": {"lingua":lingua,"lema":l,"translit":t,"strong":s,**({"ref":ref} if ref else {})}
A = lambda l,t,s,ref="": H(l,t,s,ref,"aramaico")
P = []
def p(id, pt, refs, g, sentido, heb, lat, explic, outras=None, interp=False):
    P.append({"id":id,"pt":pt,"refs":refs,"grego":{"lema":g[0],"translit":g[1],"strong":g[2]},"sentido":sentido,
              "semitico":heb,"latim":lat,"outras":outras or [],"explicacao":explic,"interpretacao":interp})

p("apokalypsis","Revelação",["1:1"],("ἀποκάλυψις","apokálypsis","G602"),"tirar o véu, descobrir o que estava escondido",
  [H("גָּלָה","galah","H1540","Dn 2:28")],{"forma":"Apocalypsis Iesu Christi","nota":"A Vulgata manteve a palavra grega; daí o nome \"Apocalipse\"."},
  "O título não anuncia catástrofe, e sim revelação: Deus descobre o que a história esconde. Em Daniel 2:28, \"há um Deus nos céus que revela (galah) os mistérios\".")
p("alfa-omega","Alfa e Ômega",["1:8","21:6","22:13"],("Ἄλφα … Ὦ","Álpha … Ō","G1, G5598"),"a primeira e a última letra do alfabeto grego",
  [H("רִאשׁוֹן … אַחֲרוֹן","ri'shon … acharon","H7223, H314","Is 44:6")],{"forma":"Ego sum Alpha et Omega, principium et finis","nota":""},
  "Ecoa Isaías 44:6, \"Eu sou o primeiro e o último\". Em hebraico o par seria álef e tav, a primeira e a última letra. Em 22:13 o título passa a Jesus.")
p("ho-on","Aquele que é, que era e que há de vir",["1:4","1:8","4:8"],("ὁ ὢν καὶ ὁ ἦν καὶ ὁ ἐρχόμενος","ho ōn kai ho ēn kai ho erchómenos","G1510, G2064"),"o que existe, existia e está vindo",
  [H("אֶהְיֶה אֲשֶׁר אֶהְיֶה","'ehyeh asher 'ehyeh","H1961","Êx 3:14"),H("יהוה","YHWH","H3068","Êx 3:15")],{"forma":"qui est et qui erat et qui venturus est","nota":""},
  "Uma paráfrase do nome divino revelado a Moisés (Êx 3:14). João mantém a forma no nominativo mesmo depois de preposição, quebrando a gramática de propósito para não \"declinar\" o nome de Deus.")
p("pantokrator","Todo-poderoso",["1:8","4:8","11:17","15:3","16:7","16:14","19:6","19:15","21:22"],("παντοκράτωρ","pantokrátōr","G3841"),"o que tem poder sobre tudo",
  [H("יהוה צְבָאוֹת","YHWH tseva'ot","H6635","Is 6:3"),H("שַׁדַּי","Shaddai","H7706","Gn 17:1")],{"forma":"omnipotens","nota":""},
  "A Septuaginta (tradução grega do AT) usa pantokrátōr para traduzir \"SENHOR dos Exércitos\". Nove das dez vezes que aparece no Novo Testamento estão no Apocalipse.")
p("hagios","Santo, santo, santo",["4:8","15:4"],("ἅγιος","hágios","G40"),"separado, totalmente outro",
  [H("קָדוֹשׁ קָדוֹשׁ קָדוֹשׁ","qadosh qadosh qadosh","H6918","Is 6:3")],{"forma":"Sanctus, sanctus, sanctus","nota":"Origem do \"Sanctus\" da liturgia cristã."},
  "O hebraico repete uma palavra para dar o grau máximo. A tripla repetição de Isaías 6:3 é cantada outra vez pelos seres viventes em 4:8.")
p("arnion","Cordeiro",["5:6","5:12","7:17","14:1","17:14","19:9","21:23","22:1"],("ἀρνίον","arníon","G721"),"cordeirinho; usado 29 vezes para Cristo",
  [H("שֶׂה","seh","H7716","Êx 12:3"),H("כֶּבֶשׂ","kevesh","H3532","Is 53:7")],{"forma":"agnus","nota":"De onde vem o \"Agnus Dei\"."},
  "João ouve falar de um Leão (5:5) e, ao olhar, vê um Cordeiro \"como que morto\" (5:6). O poder do livro é o do cordeiro pascal (Êx 12) e do servo levado ao matadouro (Is 53:7).")
p("leao-juda","Leão da tribo de Judá",["5:5"],("λέων ὁ ἐκ τῆς φυλῆς Ἰούδα","léōn ho ek tēs phylēs Iouda","G3023, G2455"),"leão; Judá",
  [H("גּוּר אַרְיֵה יְהוּדָה","gur aryeh Yehudah","H738, H3063","Gn 49:9")],{"forma":"leo de tribu Iuda","nota":""},
  "Título messiânico tirado da bênção de Jacó a Judá (Gn 49:9-10).")
p("riza","Raiz de Davi",["5:5","22:16"],("ῥίζα Δαυίδ","rhíza Dauíd","G4491, G1138"),"raiz, broto",
  [H("שֹׁרֶשׁ יִשַׁי","shoresh Yishai","H8328","Is 11:10")],{"forma":"radix David","nota":""},
  "Isaías 11 promete um rebento do tronco de Jessé. Jesus é ao mesmo tempo a raiz (a origem) e a descendência de Davi (22:16).")
p("iesous","Jesus",["1:1","22:20"],("Ἰησοῦς","Iēsoûs","G2424"),"forma grega do nome hebraico",
  [H("יְהוֹשֻׁעַ","Yehoshua","H3091","Nm 13:16")],{"forma":"Iesus","nota":""},
  "Yehoshua (Josué) significa \"o SENHOR salva\".")
p("christos","Cristo",["1:1","11:15","12:10","20:4"],("Χριστός","Christós","G5547"),"ungido",
  [H("מָשִׁיחַ","mashiach","H4899","Sl 2:2")],{"forma":"Christus","nota":""},
  "Christós traduz mashiach, \"Messias\". Em 11:15 ecoa o Salmo 2: \"o reino é do Senhor e do seu Cristo\".")
p("huios-anthropou","Filho do homem",["1:13","14:14"],("υἱὸς ἀνθρώπου","huiòs anthrṓpou","G5207, G444"),"um ser humano",
  [A("כְּבַר אֱנָשׁ","kevar 'enash","H1247, H606","Dn 7:13")],{"forma":"similem Filio hominis","nota":""},
  "Expressão aramaica de Daniel 7:13: um \"como filho de homem\" recebe o reino eterno. É o título que Jesus mais usou para si mesmo.")
p("logos","Verbo (Palavra) de Deus",["19:13"],("λόγος τοῦ θεοῦ","lógos tou theou","G3056"),"palavra, razão, mensagem",
  [H("דָּבָר","davar","H1697","Sl 33:6"),A("מֵימְרָא","memra","","Targum Onqelos, Gn 3:8")],{"forma":"Verbum Dei","nota":""},
  "O cavaleiro de 19:13 se chama \"a Palavra de Deus\", como em João 1:1. No AT a palavra (davar) cria (Sl 33:6). Os targumim aramaicos falam da \"Memra\" do SENHOR agindo no mundo.",
  outras=[{"lingua":"aramaico (targumim)","forma":"Memra","nota":"As traduções aramaicas antigas do AT."}])
p("martys","Testemunha",["1:5","2:13","11:3","17:6"],("μάρτυς","mártys","G3144"),"testemunha; daí \"mártir\"",
  [H("עֵד","'ed","H5707","Is 43:10")],{"forma":"testis","nota":""},
  "No Apocalipse, testemunhar custa a vida (Antipas, 2:13). Por isso a palavra grega para testemunha virou \"mártir\" nas línguas modernas.")
p("ekklesia","Igreja",["1:4","2:1","22:16"],("ἐκκλησία","ekklēsía","G1577"),"assembleia convocada",
  [H("קָהָל","qahal","H6951","Dt 4:10")],{"forma":"ecclesia","nota":""},
  "A Septuaginta usa ekklēsía para o qahal, a assembleia de Israel no deserto.")
p("charis-eirene","Graça e paz",["1:4"],("χάρις … εἰρήνη","cháris … eirḗnē","G5485, G1515"),"favor imerecido; paz",
  [H("חֵן","chen","H2580"),H("שָׁלוֹם","shalom","H7965","Nm 6:26")],{"forma":"gratia vobis et pax","nota":""},
  "A saudação une o grego (cháris) e o hebraico (shalom, paz e inteireza).")
p("amen","Amém",["1:6","3:14","22:20"],("ἀμήν","amḗn","G281"),"firme, verdadeiro",
  [H("אָמֵן","'amen","H543","Is 65:16")],{"forma":"Amen","nota":"A palavra passou sem tradução do hebraico ao grego, ao latim e ao português."},
  "Em 3:14 Jesus se chama \"o Amém\". Isaías 65:16 fala do \"Deus do amém\", o Deus fiel.")
p("hallelouia","Aleluia",["19:1","19:3","19:4","19:6"],("ἁλληλουϊά","hallēlouiá","G239"),"transliteração do hebraico",
  [H("הַלְלוּ־יָהּ","hallelu-Yah","H1984, H3050","Sl 146:1")],{"forma":"Alleluia","nota":""},
  "\"Louvai a Yah\". Só aparece no Novo Testamento aqui, em 19:1-6, como os Salmos de louvor (Sl 146-150).")
p("hepta","Sete",["1:4","5:1","8:2","15:1"],("ἑπτά","heptá","G2033"),"sete",
  [H("שֶׁבַע","sheva'","H7651","Gn 2:2")],{"forma":"septem","nota":""},
  "Sete é o número da obra completa de Deus (Gn 2:2). O livro é montado em setenários: igrejas, selos, trombetas e taças.", interp=True)
p("thronos","Trono",["4:2","7:10","20:11","22:3"],("θρόνος","thrónos","G2362"),"trono; 47 vezes no livro",
  [H("כִּסֵּא","kisse'","H3678","Is 6:1"),A("כָּרְסֵא","korse'","H3764","Dn 7:9")],{"forma":"thronus / sedes","nota":""},
  "O trono é o centro do livro: quem governa a história, apesar das aparências.")
p("zoa","Seres viventes",["4:6","5:8","19:4"],("ζῷα","zōa","G2226"),"viventes",
  [H("חַיּוֹת","chayyot","H2416","Ez 1:5")],{"forma":"animalia","nota":"A Vulgata diz \"animalia\", no sentido de seres que têm vida (anima)."},
  "Os quatro viventes de 4:6-8 juntam traços dos querubins de Ezequiel 1 e dos serafins de Isaías 6.")
p("presbyteroi","Anciãos",["4:4","5:8","19:4"],("πρεσβύτεροι","presbýteroi","G4245"),"anciãos; daí \"presbítero\"",
  [H("זְקֵנִים","zeqenim","H2205","Êx 24:9")],{"forma":"seniores","nota":""},
  "Vinte e quatro anciãos: muitos leem como as 12 tribos mais os 12 apóstolos, o povo de Deus completo.", interp=True)
p("lychnia","Candelabro",["1:12","1:20","2:5","11:4"],("λυχνία","lychnía","G3087"),"suporte de lâmpada",
  [H("מְנוֹרָה","menorah","H4501","Zc 4:2")],{"forma":"candelabrum","nota":""},
  "O próprio texto explica: os candelabros são as igrejas (1:20). A imagem vem da menorá do tabernáculo e de Zacarias 4.")
p("sphragis","Selo",["5:1","6:1","7:2","9:4"],("σφραγίς","sphragís","G4973"),"selo; marca de posse",
  [H("חוֹתָם","chotam","H2368","Ct 8:6")],{"forma":"signaculum / sigillum","nota":""},
  "Um rolo selado só podia ser aberto por quem tinha autoridade. Em 7:3, o mesmo selo marca os servos de Deus como propriedade dele.")
p("salpinx","Trombeta",["1:10","8:2","8:6","11:15"],("σάλπιγξ","sálpinx","G4536"),"trombeta",
  [H("שׁוֹפָר","shofar","H7782","Js 6:4"),H("חֲצֹצְרָה","chatsotsrah","H2689","Nm 10:9")],{"forma":"tuba","nota":""},
  "O shofar anunciava guerra, festa e a presença de Deus no Sinai (Êx 19:16). As sete trombetas lembram as de Jericó (Js 6).")
p("phiale","Taça",["5:8","15:7","16:1"],("φιάλη","phiálē","G5357"),"taça larga e rasa",
  [H("מִזְרָק","mizraq","H4219","Êx 27:3")],{"forma":"phiala","nota":""},
  "As taças do altar: em 5:8 cheias das orações dos santos, em 16:1 da ira de Deus. As orações e o juízo saem do mesmo altar.")
p("thymos-orge","Ira (furor)",["14:10","15:1","16:19","19:15"],("θυμός / ὀργή","thymós / orgḗ","G2372, G3709"),"furor ardente; ira firme",
  [H("חֵמָה","chemah","H2534","Jr 25:15"),H("אַף","'af","H639")],{"forma":"ira / indignatio","nota":""},
  "O \"cálice do vinho da ira\" vem de Jeremias 25:15. Não é descontrole, é a resposta de Deus à injustiça.")
p("thysiasterion","Altar",["6:9","8:3","9:13"],("θυσιαστήριον","thysiastḗrion","G2379"),"lugar do sacrifício",
  [H("מִזְבֵּחַ","mizbeach","H4196","Lv 4:7")],{"forma":"altare","nota":""},
  "As almas dos mártires estão \"debaixo do altar\" (6:9), onde se derramava o sangue dos sacrifícios (Lv 4:7).")
p("therion","Besta",["11:7","13:1","13:11","17:8","19:20"],("θηρίον","thēríon","G2342"),"fera selvagem",
  [A("חֵיוָה","cheyvah","H2423","Dn 7:3")],{"forma":"bestia","nota":""},
  "As quatro feras de Daniel 7 (em aramaico) eram impérios. A besta de 13:1 junta traços das quatro.")
p("drakon","Dragão",["12:3","12:9","20:2"],("δράκων","drákōn","G1404"),"serpente grande, monstro",
  [H("תַּנִּין","tannin","H8577","Is 27:1"),H("לִוְיָתָן","Livyatan","H3882","Is 27:1")],{"forma":"draco","nota":""},
  "O próprio texto explica: o dragão é \"a antiga serpente, que se chama diabo e Satanás\" (12:9). Isaías 27:1 promete que Deus matará o monstro do mar.")
p("satanas","Satanás e diabo",["2:9","12:9","20:2","20:10"],("Σατανᾶς / διάβολος","Satanâs / diábolos","G4567, G1228"),"adversário; caluniador",
  [H("שָׂטָן","satan","H7854","Jó 1:6"),A("סָטָנָא","satana'","")],{"forma":"Satanas / diabolus","nota":""},
  "Satan é palavra hebraica (o acusador de Jó 1 e Zc 3). Diábolos é a tradução grega: \"o que acusa\". Em 12:10 ele é \"o acusador dos nossos irmãos\".")
p("ophis","Serpente antiga",["12:9","12:15","20:2"],("ὄφις ὁ ἀρχαῖος","óphis ho archaîos","G3789"),"serpente",
  [H("נָחָשׁ","nachash","H5175","Gn 3:1")],{"forma":"serpens antiquus","nota":""},
  "\"Antiga\" aponta para o Éden (Gn 3). O livro termina onde a Bíblia começou: vencida a serpente, volta a árvore da vida.")
p("michael","Miguel",["12:7"],("Μιχαήλ","Michaḗl","G3413"),"nome próprio",
  [H("מִיכָאֵל","Mikha'el","H4317","Dn 12:1")],{"forma":"Michael","nota":""},
  "O nome é uma pergunta: \"Quem é como Deus?\". Em Daniel 12:1 ele protege o povo no tempo de angústia.")
p("abaddon","Abadom e Apoliom",["9:11"],("Ἀβαδδών / Ἀπολλύων","Abaddṓn / Apollýōn","G3, G623"),"destruição; destruidor",
  [H("אֲבַדּוֹן","'Avaddon","H11","Jó 26:6")],{"forma":"Abaddon … Apollyon … Exterminans","nota":"A Vulgata acrescenta o nome latino: \"Latine habens nomen Exterminans\"."},
  "O próprio versículo dá o nome em hebraico e em grego. Jerônimo, na Vulgata, completou com o latim. É o melhor exemplo do livro passando por três línguas.",
  outras=[{"lingua":"latim","forma":"Exterminans","nota":"\"o que extermina\", acréscimo da Vulgata."}])
p("abyssos","Abismo",["9:1","11:7","20:1"],("ἄβυσσος","ábyssos","G12"),"sem fundo",
  [H("תְּהוֹם","tehom","H8415","Gn 1:2")],{"forma":"abyssus","nota":""},
  "A Septuaginta usa ábyssos para o tehom, as águas do caos de Gênesis 1:2, que Deus organiza.")
p("hades","Hades (morada dos mortos)",["1:18","6:8","20:13"],("ᾅδης","háidēs","G86"),"mundo dos mortos",
  [H("שְׁאוֹל","she'ol","H7585","Os 13:14")],{"forma":"infernus","nota":""},
  "Hades traduz o she'ol hebraico. Jesus tem \"as chaves da morte e do Hades\" (1:18), como em Oseias 13:14.")
p("limne-pyros","Lago de fogo",["19:20","20:10","20:14","21:8"],("λίμνη τοῦ πυρός","límnē tou pyrós","G3041, G4442"),"lago de fogo",
  [A("נְהַר דִּי־נוּר","nehar di-nur","H5103, H5135","Dn 7:10")],{"forma":"stagnum ignis","nota":""},
  "Daniel 7:10 (em aramaico) vê \"um rio de fogo\" saindo do trono no juízo. O texto explica: o lago é \"a segunda morte\" (20:14).")
p("charagma","Marca",["13:16","14:9","20:4"],("χάραγμα","cháragma","G5480"),"gravação, carimbo",
  [H("תָּו","tav","H8420","Ez 9:4")],{"forma":"character","nota":"Daí a palavra \"caráter\"."},
  "Em Ezequiel 9:4, os fiéis recebem um sinal (tav, a última letra) na testa. A marca da besta é a paródia do selo de Deus (7:3).")
p("666","Seiscentos e sessenta e seis",["13:18"],("χξϛʹ","chi-xi-stigma","G5516"),"666 escrito com letras gregas",
  [H("נרון קסר","Nron Qsr","","grafia hebraica de \"Nero César\"")],{"forma":"sescenti sexaginta sex","nota":""},
  "Hebraico e grego usavam letras como números. Uma leitura antiga soma \"Nero César\" escrito em hebraico: 50+200+6+50+100+60+200 = 666. Alguns manuscritos trazem 616, que é o valor da grafia latina \"Nero Caesar\". Outros leem o 6 como o humano que nunca chega a 7.",
  outras=[{"lingua":"latim","forma":"Nero Caesar → 616","nota":"Variante registrada por Ireneu (Contra as Heresias 5.30), c. 180 d.C."}], interp=True)
p("babylon","Babilônia",["14:8","17:5","18:2"],("Βαβυλών","Babylṓn","G897"),"nome da cidade",
  [H("בָּבֶל","Bavel","H894","Jr 51:7")],{"forma":"Babylon","nota":""},
  "A Babilônia histórica destruiu Jerusalém em 586 a.C. Em 1 Pedro 5:13 o nome já é código para Roma. A queda de 18:2 repete Isaías 21:9 e Jeremias 51.", interp=True)
p("harmagedon","Armagedom",["16:16"],("Ἁρμαγεδών","Harmagedṓn","G717"),"\"em hebraico\", diz o texto",
  [H("הַר מְגִדּוֹ","har Megiddo","H2022, H4023","Zc 12:11")],{"forma":"Armagedon","nota":""},
  "Har é monte; Megido, a planície das grandes batalhas de Israel (Jz 5:19; 2Rs 23:29). Não há monte com esse nome, por isso muitos leem como símbolo do confronto final.", interp=True)
p("gog-magog","Gogue e Magogue",["20:8"],("Γὼγ καὶ Μαγώγ","Gōg kai Magṓg","G1136, G3098"),"nomes próprios",
  [H("גּוֹג … מָגוֹג","Gog … Magog","H1463, H4031","Ez 38:2")],{"forma":"Gog et Magog","nota":""},
  "Em Ezequiel 38, Gogue é um rei da terra de Magogue. João os transforma em símbolo de todas as nações rebeladas.")
p("manna","Maná escondido",["2:17"],("μάννα","mánna","G3131"),"transliteração do hebraico",
  [H("מָן","man","H4478","Êx 16:15")],{"forma":"manna absconditum","nota":""},
  "Man hu? \"O que é isto?\" (Êx 16:15). Uma tradição judaica dizia que um vaso de maná fora escondido e voltaria com o Messias.")
p("psephos","Pedra branca",["2:17"],("ψῆφος λευκή","psēphos leukḗ","G5586, G3022"),"seixo usado para votar ou como entrada",
  [],{"forma":"calculum candidum","nota":"\"Calculus\" (pedrinha) deu \"cálculo\": contava-se com pedrinhas."},
  "No mundo greco-romano, pedra branca era voto de absolvição e também servia de entrada para banquetes.", interp=True)
p("iezabel","Jezabel",["2:20"],("Ἰεζάβελ","Iezábel","G2403"),"nome próprio",
  [H("אִיזֶבֶל","'Izevel","H348","1Rs 16:31")],{"forma":"Iezabel","nota":""},
  "Apelido de uma profetisa de Tiatira, tirado da rainha que levou Israel à idolatria (1Rs 16:31).")
p("balaam","Balaão",["2:14"],("Βαλαάμ","Balaám","G903"),"nome próprio",
  [H("בִּלְעָם","Bil'am","H1109","Nm 31:16")],{"forma":"Balaam","nota":""},
  "Balaão aconselhou Moabe a seduzir Israel à idolatria (Nm 31:16). Em Pérgamo, havia quem ensinasse a mesma acomodação.")
p("nikao","Vencer",["2:7","3:21","12:11","21:7"],("νικάω","nikáō","G3528"),"vencer; daí \"Nike\"",
  [],{"forma":"qui vicerit","nota":""},
  "Cada carta termina com promessa \"ao vencedor\". Em 12:11 se vence \"pelo sangue do Cordeiro e pela palavra do testemunho\", não pela força.")
p("metanoeo","Arrepender-se",["2:5","2:16","3:3","3:19"],("μετανοέω","metanoéō","G3340"),"mudar de mente",
  [H("שׁוּב","shuv","H7725","Jl 2:12")],{"forma":"paenitentiam age","nota":"A Vulgata traduz por \"fazer penitência\", o que influenciou séculos de leitura."},
  "Grego: mudar a mente. Hebraico (shuv): dar meia-volta no caminho. As duas ideias estão nas cartas.")
p("doulos","Servo",["1:1","7:3","22:3"],("δοῦλος","doûlos","G1401"),"escravo, servo",
  [H("עֶבֶד","'eved","H5650","Am 3:7")],{"forma":"servus","nota":""},
  "Amós 3:7: Deus revela seus segredos \"aos seus servos, os profetas\". O livro abre exatamente assim (1:1).")
p("pseudoprophetes","Falso profeta",["16:13","19:20","20:10"],("ψευδοπροφήτης","pseudoprophḗtēs","G5578"),"falso profeta",
  [H("נְבִיא שֶׁקֶר","navi' sheqer","H5030, H8267","Jr 14:14")],{"forma":"pseudopropheta","nota":""},
  "O texto mostra que a segunda besta (13:11) é o falso profeta (19:20): a religião a serviço do poder.")
p("paradeisos","Paraíso",["2:7"],("παράδεισος","parádeisos","G3857"),"jardim, parque",
  [H("פַּרְדֵּס","pardes","H6508","Ec 2:5")],{"forma":"paradisus","nota":""},
  "A palavra veio do persa antigo: pairidaēza, \"cercado\", o jardim murado dos reis. Passou ao hebraico (pardes), ao grego e ao latim. A Septuaginta a usa para o Éden.",
  outras=[{"lingua":"persa antigo (avéstico)","forma":"pairidaēza","nota":"\"muro ao redor\"; jardim real."}])
p("xylon-zoes","Árvore da vida",["2:7","22:2","22:14"],("ξύλον τῆς ζωῆς","xýlon tēs zōēs","G3586, G2222"),"madeira, árvore; vida",
  [H("עֵץ הַחַיִּים","'ets ha-chayyim","H6086, H2416","Gn 2:9")],{"forma":"lignum vitae","nota":""},
  "Fechada em Gênesis 3:24, aberta de novo em 22:2. Xýlon também é a palavra usada para a cruz (At 5:30).")
p("skene","Tabernáculo de Deus com os homens",["7:15","21:3"],("σκηνή / σκηνόω","skēnḗ / skēnóō","G4633, G4637"),"tenda; armar tenda",
  [H("מִשְׁכָּן","mishkan","H4908","Lv 26:11"),H("שָׁכַן","shakhan","H7931","Êx 25:8")],{"forma":"tabernaculum Dei cum hominibus","nota":""},
  "De shakhan vem a palavra rabínica shekhiná, a presença de Deus que habita. As consoantes gregas s-k-n soam como o hebraico.",
  outras=[{"lingua":"hebraico rabínico","forma":"שְׁכִינָה shekhinah","nota":"a presença que habita."}])
p("ierousalem-kaine","Nova Jerusalém",["3:12","21:2","21:10"],("Ἰερουσαλὴμ καινή","Ierousalḗm kainḗ","G2419, G2537"),"Jerusalém nova (renovada)",
  [H("יְרוּשָׁלַיִם","Yerushalayim","H3389","Is 65:18")],{"forma":"Hierusalem nova","nota":""},
  "Kainós é novo em qualidade, não só em data: a mesma cidade, renovada. Ecoa Isaías 65:17-18.")
p("chilioi","Mil anos (milênio)",["20:2","20:4","20:6"],("χίλια ἔτη","chília étē","G5507, G2094"),"mil anos",
  [H("אֶלֶף","'elef","H505","Sl 90:4")],{"forma":"mille annos","nota":"Do latim \"mille annos\" veio \"milênio\" e \"milenarismo\"."},
  "O texto é a única passagem bíblica sobre o milênio. Pré-milenistas, pós-milenistas e amilenistas o leem de formas diferentes.", interp=True)
p("maranatha","Vem, Senhor Jesus",["22:20"],("ἔρχου κύριε Ἰησοῦ","érchou kýrie Iēsoû","G2064, G2962"),"vem, Senhor",
  [A("מָרַנָא תָא","marana tha","G3134","1Co 16:22")],{"forma":"Veni, Domine Iesu","nota":""},
  "É a tradução grega de uma das orações cristãs mais antigas, em aramaico: Maranatha, \"Senhor nosso, vem!\" (1Co 16:22; Didaquê 10:6).",
  outras=[{"lingua":"Didaquê (c. 100 d.C.)","forma":"Μαραναθά","nota":"Oração da ceia, cap. 10:6."}])

dados = {"livro":"apocalipse","descricao":"Palavras-chave de Apocalipse nas línguas originais: grego do NT, hebraico e aramaico do pano de fundo do AT e latim da Vulgata.",
 "fontes":[
  {"nome":"Números de Strong","detalhe":"James Strong, Exhaustive Concordance of the Bible (1890), domínio público. G = grego, H = hebraico/aramaico."},
  {"nome":"Vulgata Clementina","detalhe":"Biblia Sacra Vulgatae Editionis (1592), domínio público. Latim de Jerônimo (c. 405 d.C.)."},
  {"nome":"Septuaginta (LXX)","detalhe":"Tradução grega do AT (séc. III–I a.C.), citada para mostrar a ponte entre o hebraico e o grego."},
  {"nome":"Léxico on-line","detalhe":"Os números de Strong abrem o verbete no Bible Hub (biblehub.com), consulta gratuita."}],
 "palavras":P}
json.dump(dados, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
print(len(P),"palavras")
