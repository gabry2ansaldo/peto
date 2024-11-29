import streamlit as st

def commento(n):
    with st.popover("Commenta"):
        st.markdown(f"Inserisci il tuo commento sul racconto n.{n}")
        user_input = st.text_area(f"commento racconto n.{n}")

        if st.button(f"Salva il commento {n}"):
            if user_input.strip():
                with open("commenti.txt", "a") as file:
                    file.write(f"Comm Rac {n}" + user_input + "\n")
                st.success("Il tuo commento è stato salvato con successo!")
            else:
                st.warning("Il campo è vuoto. Per favore, inserisci del testo.")

st.image("peto.jpg")

tab1, tab2, tab3 = st.tabs(["Peto 1", "Peto 2", "Peto 3"])

with tab1:
    st.title("La Ballata di Peto il Cavaliere Solitario")
    """
    C’era una volta, nel cuore di un regno chiamato Viridia, un cavaliere di nome Peto. Egli non era come gli altri cavalieri che affollavano le corti con armature scintillanti e sguardi fieri. Peto indossava una cotta di maglia rattoppata e portava un elmo che sembrava più una pentola, ma il suo cuore era grande quanto il cielo, e il suo spirito indomito lo spingeva sempre verso l'ignoto.

    Un giorno, annoiato dalle giostre e dai tornei, decise di lasciare il castello e intraprendere un viaggio solitario alla ricerca di avventure. Attraversò valli nebbiose, foreste oscure e villaggi dimenticati dal tempo, incontrando lungo il cammino creature bizzarre e volgari come nessuno avrebbe mai potuto immaginare.

    ---
    ## L’Incontro con lo Sputagoblin
    Nel fitto di un bosco chiamato Nebbiamara, Peto si imbatté in un essere minuscolo, verde e puzzolente, che sputava continuamente per terra formando pozzanghere di una melma acida.

    «Chi sei tu, brutto arnese?» domandò il cavaliere, mantenendo una certa distanza.

    «Io sono Groglo il Sputagoblin!» rispose la creatura, con voce gracchiante. «E tu chi saresti, con quel coperchio da zuppa in testa?»

    Peto, offeso, sfoderò la spada e la puntò contro Groglo. «Io sono Peto, cavaliere solitario, e non tollero gli insulti!»

    Ma Groglo rise sguaiatamente. «Peto, eh? Che nome appropriato! Sai, il mio sputo può sciogliere anche l’acciaio!»

    Peto, con uno slancio improvviso, infilzò un sacco di tela che Groglo portava in spalla. Da esso uscirono cipolle marce, segatura e un odore che fece svenire persino i corvi sugli alberi. Il goblin scappò urlando insulti, ma Peto continuò il suo cammino, soddisfatto della sua vittoria.

    ---
    ## La Sirena Strozzamare
    Proseguendo, Peto raggiunse un lago cristallino. Lì, immersa fino alla vita nell’acqua, cantava una creatura dalla voce incantevole. Era una sirena, ma non una sirena qualunque: invece di una coda di pesce, aveva una pinna simile a quella di una rana, e il suo canto era interrotto da improvvisi colpi di tosse.

    «Chi osa disturbare il mio lago?» chiese la sirena, sputando un’alga.

    «Io sono Peto, e non ho paura delle creature di questo mondo o dell’altro!» rispose il cavaliere, benché fosse visibilmente confuso dalla creatura.

    La sirena, che si chiamava Strozzamare, scoppiò a ridere. «Sei il primo cavaliere che non cerca di decapitarmi a vista. Per questo, ti concederò un dono!»

    Detto ciò, tirò fuori un pettine fatto di lische di pesce. «Usalo con saggezza. Potrebbe salvarti la vita... o almeno la dignità.»

    Peto, grato, accettò il pettine e proseguì il suo viaggio.

    ---
    ## Il Villaggio dei Gargobestiami
    Dopo giorni di marcia, Peto giunse in un villaggio popolato da creature metà uomo e metà animale. Vi erano uomini con teste di capra che litigavano nei campi, donne con coda di mucca che danzavano intorno a un falò e un gallo antropomorfo che predicava dal tetto di una stalla.

    «Benvenuto a Gargopoli!» annunciò il gallo. «Sono il Profeta Cluccas, guida spirituale di questa comunità!»

    Peto osservò la scena con incredulità. I gargobestiami si comportavano in modo grottesco e assurdo: uno di loro, con il corpo di un toro, si lamentava del latte che non usciva; un altro, con zampe di coniglio, cercava di insegnare a una gallina come volare.

    Il cavaliere chiese ospitalità per la notte, ma i gargobestiami imposero una condizione: doveva partecipare a una gara di rutti rituali. Peto, non volendo offendere, accettò. Con un incredibile sforzo di polmoni (e un pasto a base di cavoli e birra), vinse la gara, conquistando il rispetto di tutto il villaggio.

    ---
    ## Il Finale
    Dopo settimane di avventure, Peto tornò a casa con storie incredibili e trofei improbabili: un pettine di lische, una pentola di sputo goblin e un corno di capra che emetteva un suono osceno ogni volta che lo suonava. Anche se nessuno gli credeva, egli si sentiva soddisfatto. Sapeva che la vera gloria non stava nelle corti o nei tornei, ma nelle stranezze del mondo e nella capacità di affrontarle con coraggio... e un pizzico di ironia.

    Così finisce la ballata di Peto, cavaliere solitario, amico delle creature bizzarre e campione indiscusso del Medioevo più strambo.
    """
    #commento(1)
with tab2:
    st.title("Le Nuove Avventure di Peto e Monica dai Tentacoli")
    """
    Dopo le sue incredibili avventure, Peto il cavaliere solitario si era convinto che non ci fosse più nulla nel mondo capace di sorprenderlo. Tuttavia, la vita aveva piani ben diversi. Un giorno, mentre attraversava le montagne Nebbiospine, si imbatté in un essere così strano che persino le sue passate esperienze sembravano comuni.

    ---
    ## L’Incontro con Monica
    Peto stava accendendo un fuoco per la notte quando sentì un suono insolito, un misto di gorgoglii e cinguettii. Si voltò e vide una figura che sembrava uscita da un incubo... o da un sogno molto confuso.

    L'essere era alto quanto lui, con un corpo esile coperto da un’armatura di squame luccicanti che parevano vive. Ma ciò che lo colpì di più erano i capelli: lunghi tentacoli che si muovevano come se avessero una volontà propria, avvolgendosi e snodandosi nell'aria.

    «Chi sei?» chiese Peto, mano sull’elsa della spada.

    «Io sono Monica,» rispose la creatura con una voce che sembrava provenire da più direzioni contemporaneamente, «e non ho un genere definito. Ma tu puoi chiamarmi "compagna d’avventura".»

    Peto, confuso ma intrigato, decise che un po' di compagnia non avrebbe guastato. Monica dimostrò subito di essere tanto bizzarra quanto utile: i suoi tentacoli potevano accendere fuochi, afferrare oggetti lontani e perfino spaventare i briganti. In breve tempo, i due divennero amici inseparabili.

    ---
    ## La Missione del Re Melmoso
    Durante il loro viaggio, Peto e Monica giunsero a un villaggio infestato da un problema assai particolare: un mostro, conosciuto come il Re Melmoso, aveva invaso i campi e trasformava ogni raccolto in un mare di gelatina verde.

    I due eroi si offrirono di affrontare la minaccia. Dopo aver seguito una scia di melma, giunsero alla tana del mostro, un’enorme caverna che gocciolava di liquido appiccicoso.

    Il Re Melmoso non era un mostro qualunque: era un’enorme creatura gelatinosa con occhi che galleggiavano nella sua massa viscida. Parlava con una voce lenta e gutturale.

    «Chi osa disturbare il mio regno di viscosità?» ruggì il Re Melmoso.

    Monica prese l’iniziativa. «Io sono Monica dai Tentacoli, e questa è la mia spada vivente!» gridò, brandendo uno dei suoi tentacoli che si era indurito come acciaio.

    Peto, non volendo essere da meno, sfoderò la sua spada e si lanciò nella battaglia. I due combatterono coraggiosamente, schivando ondate di melma e attacchi vischiosi. Monica, con i suoi tentacoli, afferrò una pietra gigante e la scagliò sul mostro, mentre Peto infilzava il cuore del Re Melmoso, che esplose in una cascata di gelatina verde.

    Quando la battaglia finì, Peto raccolse un frammento di gelatina solidificata, che brillava come una gemma, come trofeo della vittoria.

    ---
    ## Il Labirinto dei Tre Indovinelli
    Poco dopo, i due amici si ritrovarono davanti a un portale di pietra decorato con simboli arcani. Un antico guardiano, metà uomo e metà rospo, li avvisò: per attraversare il labirinto e raggiungere il tesoro nascosto, avrebbero dovuto rispondere a tre indovinelli.

    Il primo indovinello era: “Cosa cresce più quando meno ce n’è?”

    Monica rispose subito: «La pazienza.» E il guardiano annuì.

    Il secondo indovinello era: “Qual è la cosa che, quando la condividi, raddoppia?”

    Peto ci pensò un momento e disse: «La gioia.» Anche questa risposta fu accettata.

    L’ultimo indovinello, però, fu il più difficile: “Cosa pesa più del piombo ma è più leggero dell’aria?”

    Peto e Monica si guardarono, confusi. Poi Monica sorrise. «La promessa infranta.» Il guardiano gracidò di approvazione e li lasciò passare.

    Nel labirinto, trovarono non solo oro e gioielli, ma un antico manufatto: un calice che si riempiva di qualunque bevanda si desiderasse. Monica scelse del succo di melagrana, mentre Peto riempì il calice con idromele.

    ---
    ## Lo Scherzo della Città di Bifolcurbe
    Dopo settimane di avventure, i due giunsero a Bifolcurbe, una città famosa per i suoi abitanti grotteschi e volgari. Qui, ogni parola era accompagnata da un insulto o una risata sguaiata. Monica, con i suoi tentacoli, attirò subito l’attenzione della folla.

    «Guarda là, un polpo che cammina!» gridò un mercante con una pancia enorme.

    Monica, senza scomporsi, afferrò il cappello dell’uomo con un tentacolo e lo posò sul capo di una capra vicina. La folla scoppiò a ridere.

    Peto, invece, fu sfidato a una gara di braccio di ferro da una donna con braccia che sembravano tronchi d’albero. Dopo aver perso miseramente, si consolò bevendo dal calice magico e offrendo idromele a tutto il villaggio.

    ---
    ## Il Finale
    Alla fine del loro viaggio, Peto e Monica tornarono al punto di partenza, arricchiti non solo dai tesori raccolti, ma soprattutto dall’amicizia che li univa. Insieme, erano pronti ad affrontare qualunque sfida il mondo avesse in serbo, certi che, con un po’ di coraggio e un bel po’ di follia, non c’era nulla che non potessero superare.
    """
    #commento(2)
with tab3:
    st.title("Le Follie di Peto: La Grande Celebrazione")
    """
    Dopo aver sconfitto melme, risolto enigmi e stretto amicizia con la misteriosa Monica dai Tentacoli, Peto si trovava a riflettere sulla sua vita. Era un cavaliere ormai noto per le sue strambe avventure, ma qualcosa mancava: un viaggio che unisse non solo il bizzarro e il grottesco, ma anche l’assurdo puro.

    Un giorno, mentre vagava per una piana desolata, un vento ululante gli portò una voce melodiosa e misteriosa. Seguendo quel canto, Peto trovò un nuovo compagno destinato a rendere il suo mondo ancora più folle: un essere dall’aspetto sorprendentemente elegante... e ridicolmente stravagante.

    ---
    ## L’Incontro con Maximus il Gonfiabile
    Nella radura trovò Maximus, una creatura alta e imponente, fatta interamente di qualcosa che somigliava a pelle gonfiabile. Maximus ondeggiava al vento come un pupazzo delle feste, ma parlava con l’accento grave di un saggio.

    «Sono Maximus, il gonfiabile eterno! Sono qui per portare leggerezza e caos nelle vite altrui. E tu chi sei, piccolo uomo dalla testa di pentola?»

    «Io sono Peto, cavaliere solitario, ma a quanto pare sempre meno solitario. Sei il benvenuto nel nostro gruppo... se riesci a non volare via al prossimo vento!»

    Monica, che stava osservando da dietro un albero, scoppiò a ridere. «Mi piace! Finalmente qualcuno che si gonfia più di te, Peto.»

    Così Maximus si unì al duo, portando con sé non solo saggezza, ma anche la capacità di farsi esplodere per spaventare i nemici – per poi rigonfiarsi con un soffio magico.

    ---
    ## L’Annuncio della Grande Festa
    Durante un’accidentale caduta in una taverna sotterranea (causata da una mossa troppo entusiasta di Maximus), il gruppo scoprì un antico manoscritto: un invito a una leggendaria festa chiamata La Grande Celebrazione di Tutte le Assurdità. Secondo il manoscritto, la festa si sarebbe svolta in un luogo nascosto tra le montagne, accessibile solo a coloro che avevano superato prove di coraggio, follia e, soprattutto, buon umore.

    Decisi a partecipare, Peto, Monica e Maximus si misero in viaggio, raccogliendo lungo il cammino tutti i vecchi amici di Peto:

    Groglo lo Sputagoblin, che ora sputava brillantini e saliva zuccherata grazie a un incantesimo sbagliato.
    Strozzamare la Sirena, che aveva trovato un accordo con la sua tosse e cantava brani di ballate strappalacrime.
    I Gargobestiami, che arrivarono in massa con i loro strumenti musicali e una quantità spaventosa di birra fermentata.
    La Festa: Un Tripudio di Follia
    Quando tutti giunsero nel luogo della festa, scoprirono che si trattava di una gigantesca sala naturale all'interno di una montagna illuminata da migliaia di cristalli colorati. Al centro, una piattaforma rotante ospitava i musicisti più strampalati mai visti: un orso che suonava il liuto con i piedi, un goblin batterista e una gallina cantante.

    La celebrazione iniziò con danze sfrenate, canti stonati e una quantità di cibo che sfidava le leggi della fisica. Maximus si sgonfiò e rigonfiò più volte, usandosi come trampolino per i gargobestiami. Monica, con i suoi tentacoli, sollevava intere tavolate per far ballare la sirena Strozzamare, mentre Peto si esibiva in un’improbabile coreografia con il Profeta Cluccas, il gallo predicatore.

    ---
    ## L’Esplosione Finale
    A un certo punto, la festa raggiunse un livello di caos che sfuggì a ogni controllo: Groglo iniziò a lanciare il suo sputo zuccherato ovunque, Strozzamare propose un concorso di canto "gorgheggiato", e Maximus... beh, esplose. Ma questa volta, la sua esplosione causò una reazione a catena: i cristalli sulla montagna iniziarono a pulsare, trasformando la sala in un caleidoscopio di luci psichedeliche.

    Tutti, ormai sopraffatti dall’entusiasmo e dall’energia del momento, si abbracciarono, si rincorsero, ballarono e ridevano senza freni. La sala riecheggiava di voci, suoni e risate, creando un’atmosfera che nessuno dimenticò mai più.

    ---
    ## Il Finale: L’Amicizia al Centro
    Al termine della festa, Peto si trovò seduto su una roccia, osservando i suoi compagni che dormivano sparsi nella sala, esausti ma felici. Monica si avvolgeva nei suoi tentacoli come una coperta, Maximus ondeggiava piano come una mongolfiera ancorata, e gli altri russavano in armonia perfetta.

    «Forse non sono più un cavaliere solitario,» pensò Peto con un sorriso, «ma con amici così, la solitudine non mi manca affatto.»

    E così, con il cuore pieno e lo spirito leggero, Peto decise che il mondo poteva aspettare per la prossima avventura... almeno fino a quando qualcuno non avesse inventato una nuova follia.
    """
    #commento(3)