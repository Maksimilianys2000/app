from flask import Flask

app = Flask(__name__)

COUNTRIES = {

    # ================= EUROPA =================

    "poland": {
        "name": "Polska",
        "capital": "Warszawa",
        "population": "38 mln",
        "language": "Polski",
        "currency": "Złoty",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Polska"
    },

    "germany": {
        "name": "Niemcy",
        "capital": "Berlin",
        "population": "83 mln",
        "language": "Niemiecki",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Niemcy"
    },

    "france": {
        "name": "Francja",
        "capital": "Paryż",
        "population": "68 mln",
        "language": "Francuski",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Francja"
    },

    "spain": {
        "name": "Hiszpania",
        "capital": "Madryt",
        "population": "48 mln",
        "language": "Hiszpański",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Hiszpania"
    },

    "italy": {
        "name": "Włochy",
        "capital": "Rzym",
        "population": "59 mln",
        "language": "Włoski",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Włochy"
    },

    "portugal": {
        "name": "Portugalia",
        "capital": "Lizbona",
        "population": "10 mln",
        "language": "Portugalski",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Portugalia"
    },

    "belgium": {
        "name": "Belgia",
        "capital": "Bruksela",
        "population": "11 mln",
        "language": "Niderlandzki / Francuski",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Belgia"
    },

    "netherlands": {
        "name": "Holandia",
        "capital": "Amsterdam",
        "population": "17 mln",
        "language": "Niderlandzki",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Holandia"
    },

    "switzerland": {
        "name": "Szwajcaria",
        "capital": "Berno",
        "population": "8 mln",
        "language": "Niemiecki / Francuski / Włoski",
        "currency": "Frank szwajcarski",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Szwajcaria"
    },

    "austria": {
        "name": "Austria",
        "capital": "Wiedeń",
        "population": "9 mln",
        "language": "Niemiecki",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Austria"
    },

    "czechia": {
        "name": "Czechy",
        "capital": "Praga",
        "population": "10 mln",
        "language": "Czeski",
        "currency": "Korona czeska",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Czechy"
    },

    "slovakia": {
        "name": "Słowacja",
        "capital": "Bratysława",
        "population": "5 mln",
        "language": "Słowacki",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Słowacja"
    },

    "hungary": {
        "name": "Węgry",
        "capital": "Budapeszt",
        "population": "9 mln",
        "language": "Węgierski",
        "currency": "Forint",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Węgry"
    },

    "romania": {
        "name": "Rumunia",
        "capital": "Bukareszt",
        "population": "19 mln",
        "language": "Rumuński",
        "currency": "Lej",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Rumunia"
    },

    "ukraine": {
        "name": "Ukraina",
        "capital": "Kijów",
        "population": "37 mln",
        "language": "Ukraiński",
        "currency": "Hrywna",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Ukraina"
    },

    "norway": {
        "name": "Norwegia",
        "capital": "Oslo",
        "population": "5 mln",
        "language": "Norweski",
        "currency": "Korona norweska",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Norwegia"
    },

    "sweden": {
        "name": "Szwecja",
        "capital": "Sztokholm",
        "population": "10 mln",
        "language": "Szwedzki",
        "currency": "Korona szwedzka",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Szwecja"
    },

    "finland": {
        "name": "Finlandia",
        "capital": "Helsinki",
        "population": "5 mln",
        "language": "Fiński",
        "currency": "Euro",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Finlandia"
    },

    "uk": {
        "name": "Wielka Brytania",
        "capital": "Londyn",
        "population": "67 mln",
        "language": "Angielski",
        "currency": "Funt brytyjski",
        "continent": "Europa",
        "wiki": "https://pl.wikipedia.org/wiki/Wielka_Brytania"
    },

    # ================= ŚWIAT =================

    "usa": {
        "name": "USA",
        "capital": "Waszyngton",
        "population": "331 mln",
        "language": "Angielski",
        "currency": "Dolar",
        "continent": "Ameryka Północna",
        "wiki": "https://pl.wikipedia.org/wiki/Stany_Zjednoczone"
    },

    "brazil": {
        "name": "Brazylia",
        "capital": "Brasília",
        "population": "214 mln",
        "language": "Portugalski",
        "currency": "Real",
        "continent": "Ameryka Południowa",
        "wiki": "https://pl.wikipedia.org/wiki/Brazylia"
    },

    "china": {
        "name": "Chiny",
        "capital": "Pekin",
        "population": "1.4 mld",
        "language": "Chiński",
        "currency": "Juan",
        "continent": "Azja",
        "wiki": "https://pl.wikipedia.org/wiki/Chiny"
    },

    "japan": {
        "name": "Japonia",
        "capital": "Tokio",
        "population": "125 mln",
        "language": "Japoński",
        "currency": "Jen",
        "continent": "Azja",
        "wiki": "https://pl.wikipedia.org/wiki/Japonia"
    },

    "australia": {
        "name": "Australia",
        "capital": "Canberra",
        "population": "26 mln",
        "language": "Angielski",
        "currency": "Dolar australijski",
        "continent": "Australia i Oceania",
        "wiki": "https://pl.wikipedia.org/wiki/Australia"
    }
}
# ================= STYLE =================

STYLE = """
<style>

body{
    margin:0;
    font-family:Arial;
    background:#dfe6ec;
}

header{
    background:linear-gradient(90deg,#0077cc,#00bfff);
    color:white;
    text-align:center;
    padding:30px;
}

header h1{
    margin:0;
    font-size:50px;
}

nav{
    background:#005fa3;
    text-align:center;
    padding:15px;
}

nav a{
    color:white;
    text-decoration:none;
    margin:15px;
    font-size:18px;
}

nav a:hover{
    color:#ffee00;
}

.container{
    width:95%;
    margin:auto;
    padding:30px;
}

.card{
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0 0 20px rgba(0,0,0,0.15);
}

.btn{
    display:inline-block;
    background:#0077cc;
    color:white;
    text-decoration:none;
    padding:14px 22px;
    border-radius:12px;
    margin-top:10px;
}

.btn:hover{
    background:#005fa3;
}

/* ================= MAPA ================= */

.map-container{
    position:relative;
    width:100%;
    max-width:1400px;
    margin:auto;
}

.map-image{
    width:100%;
    border-radius:20px;
    box-shadow:0 0 20px rgba(0,0,0,0.2);
}

.country{
    position:absolute;
    color:white;
    font-weight:bold;
    text-decoration:none;
    font-size:13px;
    background:rgba(0,0,0,0.55);
    padding:3px 7px;
    border-radius:7px;
    transition:0.2s;
    backdrop-filter:blur(3px);
    white-space:nowrap;
}

.country:hover{
    background:#0077cc;
    transform:scale(1.05);
}

.small-country{
    font-size:7px;
    padding:2px 5px;
}

.big-country{
    font-size:18px;
    padding:8px 14px;
}

footer{
    text-align:center;
    background:#222;
    color:white;
    padding:20px;
    margin-top:40px;
}

</style>
"""

# ================= HOME =================

@app.route("/")
def home():

    return f"""
    <html>

    <head>
        <title>STOLIC</title>
        {STYLE}
    </head>

    <body>

    <header>
        <h1>🌍 STOLIC</h1>
        <p>Nowoczesna mapa świata Flask</p>
    </header>

    <nav>
        <a href="/">Start</a>
        <a href="/mapa">Mapa</a>
    </nav>

    <div class="container">

        <div class="card">

            <h2>Witaj 👋</h2>

            <p>
            Interaktywna mapa świata wykonana w Python Flask.
            </p>

            <a class="btn" href="/mapa">
                Otwórz mapę 🌍
            </a>

        </div>

    </div>

    <footer>
        © 2026 STOLIC
    </footer>

    </body>

    </html>
    """

# ================= MAPA =================

@app.route("/mapa")
def mapa():

    return f"""
    <html>

    <head>

    <title>Mapa świata</title>

    {STYLE}

    </head>

    <body>

    <header>
        <h1>🌍 INTERAKTYWNA MAPA</h1>
        <p>Kliknij kraj</p>
    </header>

    <nav>
        <a href="/">Start</a>
    </nav>

    <div class="container">

        <div class="map-container">

            <img class="map-image"
            src="https://3.allegroimg.com/original/03f2e4/15db59564e56b70eef3cda291253/Fototapeta-Mapa-Swiata-po-polsku-wybor-wzorow"
            alt="Mapa świata">

            <!-- USA -->
            <a class="country big-country"
               href="/kraj/usa"
               style="left:180px; top:320px;">
               USA
            </a>

            <!-- BRAZYLIA -->
            <a class="country big-country"
               href="/kraj/brazil"
               style="left:310px; top:620px;">
               Brazylia
            </a>

            <!-- AUSTRALIA -->
            <a class="country big-country"
               href="/kraj/australia"
               style="left:1100px; top:710px;">
               Australia
            </a>

            <!-- CHINY -->
            <a class="country big-country"
               href="/kraj/china"
               style="left:980px; top:360px;">
               Chiny
            </a>

            <!-- JAPONIA -->
            <a class="country"
               href="/kraj/japan"
               style="left:1130px; top:350px;">
               Japonia
            </a>

            <!-- POLSKA -->
            <a class="country small-country"
               href="/kraj/poland"
               style="left:670px; top:280px;">
               Polska
            </a>

            <!-- NIEMCY -->
            <a class="country small-country"
               href="/kraj/germany"
               style="left:640px; top:285px;">
               Niemcy
            </a>

            <!-- FRANCJA -->
            <a class="country small-country"
               href="/kraj/france"
               style="left:595px; top:310px;">
               Francja
            </a>

            <!-- HISZPANIA -->
            <a class="country small-country"
               href="/kraj/spain"
               style="left:566px; top:360px;">
               Hiszpania
            </a>

            <!-- WŁOCHY -->
            <a class="country small-country"
               href="/kraj/italy"
               style="left:650px; top:360px;">
               Włochy
            </a>

            <!-- PORTUGALIA -->
            <a class="country small-country"
               href="/kraj/portugal"
               style="left:549px; top:350px;">
               Portugalia
            </a>

            <!-- BELGIA -->
            <a class="country small-country"
               href="/kraj/belgium"
               style="left:585px; top:275px;">
               Belgia
            </a>


            <!-- SZWAJCARIA -->
            <a class="country small-country"
               href="/kraj/switzerland"
               style="left:610px; top:290px;">
               Szwajcaria
            </a>

            <!-- AUSTRIA -->
            <a class="country small-country"
               href="/kraj/austria"
               style="left:660px; top:315px;">
               Austria
            </a>

            <!-- CZECHY -->
            <a class="country small-country"
               href="/kraj/czechia"
               style="left:655px; top:298px;">
               Czechy
            </a>

            <!-- SŁOWACJA -->
            <a class="country small-country"
               href="/kraj/slovakia"
               style="left:665px; top:300px;">
               Słowacja
            </a>

    

            <!-- RUMUNIA -->
            <a class="country small-country"
               href="/kraj/romania"
               style="left:690px; top:325px;">
               Rumunia
            </a>

            <!-- UKRAINA -->
            <a class="country small-country"
               href="/kraj/ukraine"
               style="left:715px; top:300px;">
               Ukraina
            </a>

            <!-- NORWEGIA -->
            <a class="country small-country"
               href="/kraj/norway"
               style="left:640px; top:220px;">
               Norwegia
            </a>

            <!-- SZWECJA -->
            <a class="country small-country"
               href="/kraj/sweden"
               style="left:660px; top:230px;">
               Szwecja
            </a>

            <!-- FINLANDIA -->
            <a class="country small-country"
               href="/kraj/finland"
               style="left:697px; top:220px;">
               Finlandia
            </a>

            <!-- UK -->
            <a class="country small-country"
               href="/kraj/uk"
               style="left:605px; top:280px;">
               UK
            </a>

        </div>

    </div>

    </body>

    </html>
    """

# ================= KRAJ =================
@app.route("/kraj/<name>")
def kraj(name):

    if name not in COUNTRIES:
        return "<h1>Nie znaleziono kraju</h1>"

    country = COUNTRIES[name]

    return f"""
    <html>

    <head>

    <title>{country['name']}</title>

    {STYLE}

    </head>

    <body>

    <header>
        <h1>{country['name']}</h1>
    </header>

    <nav>
        <a href="/">Start</a>
        <a href="/mapa">Mapa</a>
    </nav>

    <div class="container">

        <div class="card">

            <h2>🌍 Informacje o kraju</h2>

            <p><b>Stolica:</b> {country['capital']}</p>

            <p><b>Liczba ludności:</b> {country['population']}</p>

            <p><b>Język:</b> {country['language']}</p>

            <p><b>Waluta:</b> {country['currency']}</p>

            <a class="btn"
               href="{country['wiki']}"
               target="_blank">

               Otwórz Wikipedia 🌍

            </a>

        </div>

    </div>

    </body>

    </html>
    """
# ================= START =================

if __name__ == "__main__":
    app.run(debug=True)
