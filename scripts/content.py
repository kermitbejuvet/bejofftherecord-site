"""Translated copy for the Bej Off The Record website (EN, DE, ES).

Keys are shared across languages. Page copy lives here; video lists live in
data/series-videos.json and data/video-meta.json; full episode pages live in
data/episodes/*.json.
"""

LANGS = ["en", "de", "es"]
LANG_NAMES = {"en": "EN", "de": "DE", "es": "ES"}
LOCALES = {"en": "en_US", "de": "de_DE", "es": "es_ES"}

UI = {
    "nav_home": {"en": "Home", "de": "Start", "es": "Inicio"},
    "nav_about": {"en": "About", "de": "Über", "es": "Sobre mí"},
    "nav_series": {"en": "Series", "de": "Serien", "es": "Series"},
    "nav_collabs": {"en": "Collabs", "de": "Kooperationen", "es": "Colaboraciones"},
    "menu": {"en": "Menu", "de": "Menü", "es": "Menú"},
    "all_series": {"en": "All series", "de": "Alle Serien", "es": "Todas las series"},
    "episodes": {"en": "episodes", "de": "Folgen", "es": "episodios"},
    "episode": {"en": "episode", "de": "Folge", "es": "episodio"},
    "ep": {"en": "Ep", "de": "Folge", "es": "Ep"},
    "play": {"en": "Play video", "de": "Video abspielen", "es": "Ver video"},
    "open_tiktok": {"en": "Open on TikTok", "de": "Auf TikTok öffnen", "es": "Abrir en TikTok"},
    "read_episode": {"en": "Read the full episode", "de": "Ganze Folge lesen", "es": "Leer el episodio completo"},
    "follow_tiktok": {"en": "Follow on TikTok", "de": "Auf TikTok folgen", "es": "Seguir en TikTok"},
    "follow_on": {"en": "Follow on", "de": "Folgen auf", "es": "Seguir en"},
    "see_all_series": {"en": "See all series", "de": "Alle Serien ansehen", "es": "Ver todas las series"},
    "by_bej": {"en": "By Bej", "de": "Von Bej", "es": "Por Bej"},
    "published": {"en": "Published", "de": "Veröffentlicht", "es": "Publicado"},
    "original": {"en": "Original", "de": "Original", "es": "Original"},
    "the_story": {"en": "The story", "de": "Die Geschichte", "es": "La historia"},
    "every_version": {"en": "Every version in the episode", "de": "Alle Versionen in der Folge", "es": "Todas las versiones del episodio"},
    "watch_episode": {"en": "Watch the episode", "de": "Folge ansehen", "es": "Ver el episodio"},
    "more_in_series": {"en": "More from", "de": "Mehr aus", "es": "Más de"},
    "captions_note": {
        "en": "",
        "de": "Die Videobeschreibungen sind im englischen Original.",
        "es": "Las descripciones de los videos están en su inglés original.",
    },
    "year_note": {
        "en": "Years are shown only where the release year is confirmed.",
        "de": "Jahreszahlen stehen nur dort, wo das Erscheinungsjahr bestätigt ist.",
        "es": "Los años solo aparecen cuando la fecha de publicación está confirmada.",
    },
    "oldest": {"en": "Oldest first", "de": "Älteste zuerst", "es": "Más antiguos primero"},
    "newest": {"en": "Newest first", "de": "Neueste zuerst", "es": "Más recientes primero"},
    "part": {"en": "Part", "de": "Teil", "es": "Parte"},
    "parts_title": {"en": "The series, part by part", "de": "Die Serie, Teil für Teil", "es": "La serie, parte por parte"},
    "rights": {"en": "Bej Off The Record", "de": "Bej Off The Record", "es": "Bej Off The Record"},
}

MONTHS = {
    "en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    "de": ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
    "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
}

# Series names and descriptions. Slugs must match data/series-videos.json.
SERIES = {
    "world-music-history": {
        "name": {"en": "World Music History", "de": "World Music History", "es": "World Music History"},
        "short": {
            "en": "Mexican music history, decade by decade. From ranchera and bolero to rock, norteño, cumbia and Canto Nuevo.",
            "de": "Mexikanische Musikgeschichte, Jahrzehnt für Jahrzehnt. Von Ranchera und Bolero über Rock und Norteño bis Cumbia und Canto Nuevo.",
            "es": "La historia de la música mexicana, década por década. De la ranchera y el bolero al rock, el norteño, la cumbia y el Canto Nuevo.",
        },
        "intro": {
            "en": "World Music History tells one country's music in order, one short episode at a time. The first country is Mexico. The series starts in the 1950s with ranchera, bolero and the singers of the cinema golden age, moves through La Nueva Ola and the Mexican rock scene of the 1960s, and reaches the 1970s with norteño, the corrido, cumbia, the balada romántica and Canto Nuevo. Each era gets a context episode, then spotlights on the artists who defined it, often followed by a top 10 of their songs.",
            "de": "World Music History erzählt die Musik eines Landes in chronologischer Reihenfolge, eine kurze Folge nach der anderen. Das erste Land ist Mexiko. Die Serie beginnt in den 1950ern mit Ranchera, Bolero und den Stimmen des goldenen Kinozeitalters, führt über La Nueva Ola und die mexikanische Rockszene der 1960er und erreicht die 1970er mit Norteño, Corrido, Cumbia, Balada Romántica und Canto Nuevo. Jede Epoche bekommt eine Einführungsfolge, danach Porträts der prägenden Künstlerinnen und Künstler, oft mit einer Top 10 ihrer Songs.",
            "es": "World Music History cuenta la música de un país en orden cronológico, un episodio corto a la vez. El primer país es México. La serie empieza en los años 50 con la ranchera, el bolero y las voces de la época de oro del cine, pasa por La Nueva Ola y la escena del rock mexicano de los 60 y llega a los 70 con el norteño, el corrido, la cumbia, la balada romántica y el Canto Nuevo. Cada época tiene un episodio de contexto y después retratos de los artistas que la definieron, a menudo con un top 10 de sus canciones.",
        },
    },
    "frontwoman": {
        "name": {"en": "Frontwoman", "de": "Frontwoman", "es": "Frontwoman"},
        "short": {
            "en": "The women who ran the stage, told as lives, not legends. Debbie Harry, Brody Dalle, Shirley Manson.",
            "de": "Die Frauen, die die Bühne geführt haben, erzählt als Leben, nicht als Legenden. Debbie Harry, Brody Dalle, Shirley Manson.",
            "es": "Las mujeres que dominaron el escenario, contadas como vidas, no como leyendas. Debbie Harry, Brody Dalle, Shirley Manson.",
        },
        "intro": {
            "en": "Frontwoman is a multi-part biography series about women who led rock bands, and about the gap between what they made and what was written about them. Each artist gets several episodes: where she came from, the sound she made, how the press and the industry treated her, and what she left behind. So far: Debbie Harry of Blondie, Brody Dalle of The Distillers, and Shirley Manson of Garbage.",
            "de": "Frontwoman ist eine mehrteilige Biografie-Serie über Frauen, die Rockbands angeführt haben, und über die Lücke zwischen dem, was sie geschaffen haben, und dem, was über sie geschrieben wurde. Jede Künstlerin bekommt mehrere Folgen: woher sie kam, welchen Sound sie geprägt hat, wie Presse und Musikindustrie mit ihr umgingen und was bleibt. Bisher: Debbie Harry von Blondie, Brody Dalle von The Distillers und Shirley Manson von Garbage.",
            "es": "Frontwoman es una serie biográfica en varias partes sobre mujeres que lideraron bandas de rock, y sobre la distancia entre lo que crearon y lo que se escribió de ellas. Cada artista tiene varios episodios: de dónde venía, el sonido que creó, cómo la trataron la prensa y la industria y lo que dejó. Hasta ahora: Debbie Harry de Blondie, Brody Dalle de The Distillers y Shirley Manson de Garbage.",
        },
    },
    "video-essays": {
        "name": {"en": "Video Essays", "de": "Videoessays", "es": "Videoensayos"},
        "short": {
            "en": "One artist, taken apart over several episodes. Technique, effect, and why.",
            "de": "Ein Künstler, über mehrere Folgen genau betrachtet. Technik, Wirkung und das Warum.",
            "es": "Un artista, analizado a fondo en varios episodios. Técnica, efecto y porqué.",
        },
        "intro": {
            "en": "Video Essays take one artist and look at the work closely across several episodes. The first essay is about Julian Casablancas of The Strokes and The Voidz: what his voice is actually doing, what it does to the listener, and why he keeps refusing the version of himself that worked.",
            "de": "Die Videoessays nehmen sich einen Künstler vor und betrachten sein Werk über mehrere Folgen hinweg genau. Der erste Essay handelt von Julian Casablancas von The Strokes und The Voidz: was seine Stimme eigentlich macht, was sie beim Hören auslöst und warum er die Version von sich, die funktioniert hat, immer wieder verweigert.",
            "es": "Los videoensayos toman a un artista y miran su obra de cerca a lo largo de varios episodios. El primero trata sobre Julian Casablancas, de The Strokes y The Voidz: qué hace realmente su voz, qué provoca en quien escucha y por qué sigue rechazando la versión de sí mismo que funcionó.",
        },
    },
    "director-series": {
        "name": {"en": "Director Series", "de": "Director Series", "es": "Director Series"},
        "short": {
            "en": "The directors who decided what music looks like. Chris Cunningham, Diane Martel, Mary Lambert, Joseph Kahn, Dave Meyers and more.",
            "de": "Die Regisseurinnen und Regisseure, die bestimmt haben, wie Musik aussieht. Chris Cunningham, Diane Martel, Mary Lambert, Joseph Kahn, Dave Meyers und mehr.",
            "es": "Los directores que decidieron cómo se ve la música. Chris Cunningham, Diane Martel, Mary Lambert, Joseph Kahn, Dave Meyers y más.",
        },
        "intro": {
            "en": "The Director Series is about the people behind the camera of the music video era. Each director gets a spotlight and a top 10 of their videos: Chris Cunningham, Diane Martel, Mary Lambert, Joseph Kahn and Dave Meyers, plus specials on film directors who made music videos, musicians who directed their own, and Spike Lee's music videos.",
            "de": "Die Director Series widmet sich den Menschen hinter der Kamera im Zeitalter des Musikvideos. Jede Regie bekommt ein Porträt und eine Top 10 ihrer Videos: Chris Cunningham, Diane Martel, Mary Lambert, Joseph Kahn und Dave Meyers, dazu Specials über Filmregisseure, die Musikvideos gedreht haben, über Musiker, die bei ihren eigenen Videos Regie führten, und über die Musikvideos von Spike Lee.",
            "es": "La Director Series trata sobre las personas detrás de la cámara en la era del videoclip. Cada director tiene un retrato y un top 10 de sus videos: Chris Cunningham, Diane Martel, Mary Lambert, Joseph Kahn y Dave Meyers, además de especiales sobre cineastas que dirigieron videoclips, músicos que dirigieron los suyos y los videoclips de Spike Lee.",
        },
    },
    "cover-atlas": {
        "name": {"en": "Cover Atlas", "de": "Cover Atlas", "es": "Cover Atlas"},
        "short": {
            "en": "One song, every language it travelled into.",
            "de": "Ein Song und alle Sprachen, in die er gereist ist.",
            "es": "Una canción y todos los idiomas a los que viajó.",
        },
        "intro": {
            "en": "Cover Atlas follows one song around the world. Each episode starts with the original and then plays the versions recorded in other countries and languages, from 1960s European pop to Japanese, Turkish, Korean and Hindi adaptations. Some covers became bigger than the original. Some songs are not from where you think. Every episode below has a full page with the complete list of versions.",
            "de": "Cover Atlas folgt einem Song um die Welt. Jede Folge beginnt mit dem Original und zeigt dann die Versionen aus anderen Ländern und Sprachen, vom europäischen Pop der 1960er bis zu japanischen, türkischen, koreanischen und Hindi-Fassungen. Manche Cover wurden größer als das Original. Manche Songs stammen nicht von dort, wo man denkt. Zu jeder Folge gibt es eine eigene Seite mit der vollständigen Liste der Versionen.",
            "es": "Cover Atlas sigue una canción por el mundo. Cada episodio empieza con el original y luego recorre las versiones grabadas en otros países e idiomas, del pop europeo de los 60 a adaptaciones en japonés, turco, coreano e hindi. Algunas versiones fueron más grandes que el original. Algunas canciones no son de donde crees. Cada episodio tiene su propia página con la lista completa de versiones.",
        },
    },
    "taking-it-off-the-shelf": {
        "name": {"en": "Taking It Off The Shelf", "de": "Taking It Off The Shelf", "es": "Taking It Off The Shelf"},
        "short": {
            "en": "One band, one song from every album. Under a minute.",
            "de": "Eine Band, ein Song von jedem Album. In unter einer Minute.",
            "es": "Una banda, una canción de cada álbum. En menos de un minuto.",
        },
        "intro": {
            "en": "Taking It Off The Shelf revisits 2000s British indie bands you might have stopped listening to. Each episode plays the most popular song from every studio album, in order, so you hear where the band went after the hit you remember. So far: The Fratellis, The Wombats, Kasabian, Kaiser Chiefs and Bloc Party.",
            "de": "Taking It Off The Shelf besucht britische Indie-Bands der 2000er, die man vielleicht nicht mehr hört. Jede Folge spielt den bekanntesten Song jedes Studioalbums in chronologischer Reihenfolge, damit man hört, wohin sich die Band nach dem Hit entwickelt hat. Bisher: The Fratellis, The Wombats, Kasabian, Kaiser Chiefs und Bloc Party.",
            "es": "Taking It Off The Shelf vuelve a las bandas indie británicas de los 2000 que quizá dejaste de escuchar. Cada episodio pone la canción más popular de cada álbum de estudio, en orden, para que oigas hacia dónde fue la banda después del éxito que recuerdas. Hasta ahora: The Fratellis, The Wombats, Kasabian, Kaiser Chiefs y Bloc Party.",
        },
    },
    "on-this-day": {
        "name": {"en": "On This Day in Music History", "de": "On This Day in Music History", "es": "On This Day in Music History"},
        "short": {
            "en": "Birthdays and moments that shaped music, one date at a time.",
            "de": "Geburtstage und Momente, die die Musik geprägt haben, ein Datum nach dem anderen.",
            "es": "Cumpleaños y momentos que marcaron la música, una fecha a la vez.",
        },
        "intro": {
            "en": "On This Day in Music History picks one date and one moment: an album release, a concert, a TV appearance, a birthday. From John Lennon's last concert appearance and the Thriller video premiere to Nirvana's MTV Unplugged, Beyoncé's surprise album and the first Rock and Roll Hall of Fame ceremony.",
            "de": "On This Day in Music History wählt ein Datum und einen Moment: eine Albumveröffentlichung, ein Konzert, einen TV-Auftritt, einen Geburtstag. Von John Lennons letztem Konzertauftritt und der Premiere des Thriller-Videos bis zu Nirvanas MTV Unplugged, Beyoncés Überraschungsalbum und der ersten Rock and Roll Hall of Fame Zeremonie.",
            "es": "On This Day in Music History elige una fecha y un momento: el lanzamiento de un álbum, un concierto, una aparición en televisión, un cumpleaños. Desde la última aparición en concierto de John Lennon y el estreno del video de Thriller hasta el MTV Unplugged de Nirvana, el álbum sorpresa de Beyoncé y la primera ceremonia del Rock and Roll Hall of Fame.",
        },
    },
    "strokes-week": {
        "name": {"en": "Strokes Week", "de": "Strokes Week", "es": "Strokes Week"},
        "short": {
            "en": "A week of Strokes trivia to celebrate seeing them live.",
            "de": "Eine Woche Strokes-Trivia zur Feier eines Konzerts.",
            "es": "Una semana de trivia de The Strokes para celebrar un concierto.",
        },
        "intro": {
            "en": "Strokes Week was a run of short quizzes and trivia about The Strokes and their side projects, posted in the week of their concert.",
            "de": "Die Strokes Week war eine Reihe kurzer Quizfragen und Trivia über The Strokes und ihre Nebenprojekte, veröffentlicht in der Woche ihres Konzerts.",
            "es": "Strokes Week fue una serie de preguntas y curiosidades cortas sobre The Strokes y sus proyectos paralelos, publicada la semana de su concierto.",
        },
    },
    "concert-diaries": {
        "name": {"en": "Concert Diaries", "de": "Concert Diaries", "es": "Concert Diaries"},
        "short": {
            "en": "What the night was actually like. Written after, posted after.",
            "de": "Wie der Abend wirklich war. Danach geschrieben, danach gepostet.",
            "es": "Cómo fue realmente la noche. Escrito después, publicado después.",
        },
        "intro": {
            "en": "Concert Diaries are short notes from the crowd, numbered by how many bands I have seen live this year, with one fact about the band and where the show sat on their tour.",
            "de": "Concert Diaries sind kurze Notizen aus dem Publikum, nummeriert danach, wie viele Bands ich dieses Jahr live gesehen habe, mit einem Fakt über die Band und dem Platz der Show auf ihrer Tour.",
            "es": "Concert Diaries son notas breves desde el público, numeradas según cuántas bandas he visto en vivo este año, con un dato sobre la banda y el lugar del concierto en su gira.",
        },
    },
}

HOME = {
    "title": {
        "en": "Bej Off The Record: Music History, Deep Dives and Cover Stories",
        "de": "Bej Off The Record: Musikgeschichte, Deep Dives und Cover-Geschichten",
        "es": "Bej Off The Record: historia de la música, análisis y versiones",
    },
    "description": {
        "en": "Short music history episodes with names, dates and an opinion. Deep dives, cover stories from around the world, and concert diaries.",
        "de": "Kurze Folgen zur Musikgeschichte mit Namen, Daten und einer Meinung. Deep Dives, Cover-Geschichten aus aller Welt und Konzerttagebücher.",
        "es": "Episodios breves de historia de la música con nombres, fechas y una opinión. Análisis, versiones de todo el mundo y diarios de conciertos.",
    },
    "badge": {"en": "OFF THE RECORD", "de": "OFF THE RECORD", "es": "OFF THE RECORD"},
    "subtitle": {
        "en": "Music deep dives for people who read the liner notes.",
        "de": "Musik-Deep-Dives für alle, die die Linernotes lesen.",
        "es": "Historias de la música para quienes leen las notas del disco.",
    },
    "tagline": {"en": "The B-side of music history.", "de": "Die B-Seite der Musikgeschichte.", "es": "La cara B de la historia de la música."},
    "what_title": {"en": "What is Bej Off The Record?", "de": "Was ist Bej Off The Record?", "es": "¿Qué es Bej Off The Record?"},
    "what_text": {
        "en": "Music history with names, dates and an opinion. The stories behind songs, the artists the algorithm forgot, and the covers you didn't know existed.",
        "de": "Musikgeschichte mit Namen, Daten und einer Meinung. Die Geschichten hinter Songs, die Künstler, die der Algorithmus vergessen hat, und Cover, von denen man nichts wusste.",
        "es": "Historia de la música con nombres, fechas y una opinión. Las historias detrás de las canciones, los artistas que el algoritmo olvidó y las versiones que no sabías que existían.",
    },
    "content_title": {"en": "The Content", "de": "Die Inhalte", "es": "El contenido"},
    "content_text": {
        "en": "Every episode starts with one question: what's the real story behind this song? Short, specific, no fan worship.",
        "de": "Jede Folge beginnt mit einer Frage: Was ist die wahre Geschichte hinter diesem Song? Kurz, konkret, ohne Fan-Verklärung.",
        "es": "Cada episodio empieza con una pregunta: ¿cuál es la verdadera historia detrás de esta canción? Corto, concreto y sin idolatría.",
    },
    "cards": [
        ({"en": "Music History", "de": "Musikgeschichte", "es": "Historia de la música"},
         {"en": "Eras, scenes and countries, told in order.", "de": "Epochen, Szenen und Länder, chronologisch erzählt.", "es": "Épocas, escenas y países, contados en orden."}),
        ({"en": "Deep Dives", "de": "Deep Dives", "es": "A fondo"},
         {"en": "One artist, taken apart properly.", "de": "Ein Künstler, gründlich betrachtet.", "es": "Un artista, analizado a fondo."}),
        ({"en": "Cover Stories", "de": "Cover-Geschichten", "es": "Versiones"},
         {"en": "One song, every language it travelled into.", "de": "Ein Song und alle Sprachen, in die er gereist ist.", "es": "Una canción y todos los idiomas a los que viajó."}),
        ({"en": "Live", "de": "Live", "es": "En vivo"},
         {"en": "Concert diaries from the crowd.", "de": "Konzerttagebücher aus dem Publikum.", "es": "Diarios de conciertos desde el público."}),
    ],
    "find_title": {"en": "Where to find me", "de": "Wo du mich findest", "es": "Dónde encontrarme"},
    "platforms": {
        "TikTok": {"en": "Full episodes. History, deep dives and ongoing series.", "de": "Ganze Folgen. Geschichte, Deep Dives und laufende Serien.", "es": "Episodios completos. Historia, análisis y series en curso."},
        "Instagram": {"en": "Carousels, reels and concert diaries.", "de": "Karussells, Reels und Konzerttagebücher.", "es": "Carruseles, reels y diarios de conciertos."},
        "YouTube": {"en": "Shorts and Cover Atlas.", "de": "Shorts und Cover Atlas.", "es": "Shorts y Cover Atlas."},
    },
    "collab_title": {"en": "Want to work together?", "de": "Zusammenarbeiten?", "es": "¿Trabajamos juntos?"},
    "collab_text": {
        "en": "Labels, venues, festivals and brands with a story worth telling. Let's talk.",
        "de": "Labels, Venues, Festivals und Marken mit einer Geschichte, die erzählt werden sollte. Lass uns reden.",
        "es": "Sellos, salas, festivales y marcas con una historia que merece contarse. Hablemos.",
    },
    "latest_title": {"en": "Latest Cover Atlas episodes", "de": "Neueste Cover-Atlas-Folgen", "es": "Últimos episodios de Cover Atlas"},
}

ABOUT = {
    "title": {"en": "About Bej, Bej Off The Record", "de": "Über Bej, Bej Off The Record", "es": "Sobre Bej, Bej Off The Record"},
    "description": {
        "en": "Critic, not fangirl. Who is behind Bej Off The Record and what the channel is about.",
        "de": "Kritikerin, kein Fangirl. Wer hinter Bej Off The Record steckt und worum es im Kanal geht.",
        "es": "Crítica, no fan. Quién está detrás de Bej Off The Record y de qué trata el canal.",
    },
    "h1": {"en": "Critic, not fangirl.", "de": "Kritikerin, kein Fangirl.", "es": "Crítica, no fan."},
    "p1": {
        "en": "I'm Bej. I talk about music with names, dates and an opinion.",
        "de": "Ich bin Bej. Ich spreche über Musik mit Namen, Daten und einer Meinung.",
        "es": "Soy Bej. Hablo de música con nombres, fechas y una opinión.",
    },
    "p2": {
        "en": "No \"this song is so powerful.\" I'll tell you what the song actually does, who made it that way, and why nobody talks about it anymore.",
        "de": "Kein \"dieser Song ist so stark\". Ich erzähle, was ein Song wirklich macht, wer ihn so gemacht hat und warum niemand mehr darüber spricht.",
        "es": "Nada de \"esta canción es muy poderosa\". Te cuento qué hace realmente la canción, quién la hizo así y por qué ya nadie habla de ella.",
    },
    "make_title": {"en": "What I make", "de": "Was ich mache", "es": "Lo que hago"},
    "make_text": {
        "en": "Short episodes. One artist, one era or one song at a time. History, deep dives, cover stories and concert diaries, in English, with descriptions in Spanish for the Mexico series.",
        "de": "Kurze Folgen. Ein Künstler, eine Epoche oder ein Song nach dem anderen. Geschichte, Deep Dives, Cover-Geschichten und Konzerttagebücher, auf Englisch, mit spanischen Beschreibungen für die Mexiko-Serie.",
        "es": "Episodios cortos. Un artista, una época o una canción a la vez. Historia, análisis, versiones y diarios de conciertos, en inglés, con descripciones en español para la serie de México.",
    },
    "cta": {
        "en": "Know a song with a better backstory than its chorus?",
        "de": "Kennst du einen Song mit einer besseren Geschichte als sein Refrain?",
        "es": "¿Conoces una canción con una historia mejor que su estribillo?",
    },
    "cta_btn": {"en": "Tell me", "de": "Erzähl es mir", "es": "Cuéntamelo"},
}

SERIES_PAGE = {
    "title": {"en": "All Series, Bej Off The Record", "de": "Alle Serien, Bej Off The Record", "es": "Todas las series, Bej Off The Record"},
    "h1": {"en": "The Series", "de": "Die Serien", "es": "Las series"},
    "lead": {
        "en": "Every series has one rule. Here they are.",
        "de": "Jede Serie hat eine Regel. Hier sind sie.",
        "es": "Cada serie tiene una regla. Aquí están.",
    },
}

COLLABS = {
    "title": {"en": "Work With Bej Off The Record", "de": "Zusammenarbeit mit Bej Off The Record", "es": "Colabora con Bej Off The Record"},
    "description": {
        "en": "Artist features, live coverage and series sponsorships for labels, venues, festivals and brands.",
        "de": "Künstlerporträts, Live-Berichte und Serien-Sponsoring für Labels, Venues, Festivals und Marken.",
        "es": "Perfiles de artistas, cobertura en vivo y patrocinio de series para sellos, salas, festivales y marcas.",
    },
    "h1": {"en": "Want to work together?", "de": "Zusammenarbeiten?", "es": "¿Trabajamos juntos?"},
    "lead": {
        "en": "I work with labels, venues, festivals and brands that have a story worth telling. If it's about music, I'm listening.",
        "de": "Ich arbeite mit Labels, Venues, Festivals und Marken, die eine Geschichte zu erzählen haben. Wenn es um Musik geht, höre ich zu.",
        "es": "Trabajo con sellos, salas, festivales y marcas que tienen una historia que contar. Si se trata de música, te escucho.",
    },
    "cards": [
        ({"en": "Artist and album features", "de": "Künstler- und Albumporträts", "es": "Perfiles de artistas y álbumes"},
         {"en": "A deep dive episode on an artist, release or catalogue.", "de": "Eine Deep-Dive-Folge über einen Künstler, eine Veröffentlichung oder einen Katalog.", "es": "Un episodio a fondo sobre un artista, un lanzamiento o un catálogo."}),
        ({"en": "Live coverage", "de": "Live-Berichte", "es": "Cobertura en vivo"},
         {"en": "Concert and festival diaries in Berlin and beyond.", "de": "Konzert- und Festivaltagebücher in Berlin und darüber hinaus.", "es": "Diarios de conciertos y festivales en Berlín y más allá."}),
        ({"en": "Series sponsorship", "de": "Serien-Sponsoring", "es": "Patrocinio de series"},
         {"en": "Support a running series like Cover Atlas or World Music History.", "de": "Unterstütze eine laufende Serie wie Cover Atlas oder World Music History.", "es": "Apoya una serie en curso como Cover Atlas o World Music History."}),
        ({"en": "Research and storytelling", "de": "Recherche und Storytelling", "es": "Investigación y narrativa"},
         {"en": "The backstory behind a song, scene or archive.", "de": "Die Geschichte hinter einem Song, einer Szene oder einem Archiv.", "es": "La historia detrás de una canción, una escena o un archivo."}),
    ],
    "contact_title": {"en": "Get in touch", "de": "Kontakt", "es": "Contacto"},
    "contact_text": {
        "en": "Send me a short note on what you have in mind.",
        "de": "Schick mir eine kurze Nachricht mit deiner Idee.",
        "es": "Envíame una nota breve con lo que tienes en mente.",
    },
    "dm_ig": {"en": "DM me on Instagram", "de": "Schreib mir auf Instagram", "es": "Escríbeme en Instagram"},
    "dm_tt": {"en": "Message me on TikTok", "de": "Schreib mir auf TikTok", "es": "Escríbeme en TikTok"},
}

# Country and language names used in episode version lists.
PLACES = {
    "USA": {"de": "USA", "es": "Estados Unidos"},
    "Italy": {"de": "Italien", "es": "Italia"},
    "France": {"de": "Frankreich", "es": "Francia"},
    "Yugoslavia": {"de": "Jugoslawien", "es": "Yugoslavia"},
    "Hong Kong": {"de": "Hongkong", "es": "Hong Kong"},
    "Romania": {"de": "Rumänien", "es": "Rumania"},
    "Czech Republic": {"de": "Tschechien", "es": "República Checa"},
    "Czechoslovakia": {"de": "Tschechoslowakei", "es": "Checoslovaquia"},
    "Germany": {"de": "Deutschland", "es": "Alemania"},
    "Japan": {"de": "Japan", "es": "Japón"},
    "Turkey": {"de": "Türkei", "es": "Turquía"},
    "Mexico": {"de": "Mexiko", "es": "México"},
    "USSR": {"de": "Sowjetunion", "es": "URSS"},
    "Belgium": {"de": "Belgien", "es": "Bélgica"},
    "South Korea": {"de": "Südkorea", "es": "Corea del Sur"},
    "Russia": {"de": "Russland", "es": "Rusia"},
    "UK": {"de": "Großbritannien", "es": "Reino Unido"},
    "Finland": {"de": "Finnland", "es": "Finlandia"},
    "Poland": {"de": "Polen", "es": "Polonia"},
    "Luxembourg": {"de": "Luxemburg", "es": "Luxemburgo"},
    "Denmark": {"de": "Dänemark", "es": "Dinamarca"},
    "Spain": {"de": "Spanien", "es": "España"},
    "Catalonia": {"de": "Katalonien", "es": "Cataluña"},
    "Brazil": {"de": "Brasilien", "es": "Brasil"},
    "Bolivia": {"de": "Bolivien", "es": "Bolivia"},
    "Peru": {"de": "Peru", "es": "Perú"},
    "Egypt": {"de": "Ägypten", "es": "Egipto"},
    "India": {"de": "Indien", "es": "India"},
    "Belgium / France": {"de": "Belgien / Frankreich", "es": "Bélgica / Francia"},
}

LANGUAGES = {
    "English": {"de": "Englisch", "es": "inglés"},
    "Italian": {"de": "Italienisch", "es": "italiano"},
    "French": {"de": "Französisch", "es": "francés"},
    "Serbo-Croatian": {"de": "Serbokroatisch", "es": "serbocroata"},
    "Cantonese": {"de": "Kantonesisch", "es": "cantonés"},
    "Romanian": {"de": "Rumänisch", "es": "rumano"},
    "Czech": {"de": "Tschechisch", "es": "checo"},
    "German": {"de": "Deutsch", "es": "alemán"},
    "Japanese": {"de": "Japanisch", "es": "japonés"},
    "Turkish": {"de": "Türkisch", "es": "turco"},
    "Spanish": {"de": "Spanisch", "es": "español"},
    "Russian": {"de": "Russisch", "es": "ruso"},
    "Korean": {"de": "Koreanisch", "es": "coreano"},
    "Finnish": {"de": "Finnisch", "es": "finés"},
    "Polish": {"de": "Polnisch", "es": "polaco"},
    "Danish": {"de": "Dänisch", "es": "danés"},
    "Catalan": {"de": "Katalanisch", "es": "catalán"},
    "Portuguese": {"de": "Portugiesisch", "es": "portugués"},
    "Arabic": {"de": "Arabisch", "es": "árabe"},
    "Hindi": {"de": "Hindi", "es": "hindi"},
}
