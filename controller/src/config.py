from .ControllerDefinitions import Usecase, Question

# configuration of Usecases and questions. This determines, which usecase should handle the request depending on
# the keywords

usecases = [
    Usecase(
        name="welcome",
        questions=[
            Question(
                route="/welcome",
                keywords=["willkommen", "guten morgen", "briefing"],
                example_questions=["Gib mir ein Briefing für den Tag", "Zeig mir den guten Morgen Dialog"]
            ),
            Question(
                route="/wetter",
                keywords=["wetter"],
                example_questions=["Wie wird das Wetter heute ?"]
            ),
            Question(
                route="/todo",
                keywords=["todo", "zu tun"],
                example_questions=["Was steht auf meiner Todo Liste?", "Was gibt es heute zu tun?"]
            ),
            Question(
                route="/termine",
                keywords=["kalender", "termin"],
                example_questions=["Was steht heute im Kalender?", "Welche Termine habe ich heute?"]
            ),
            Question(
                route="/stundenplan",
                keywords=["stundenplan", "rapla", "vorlesungen", "vorlesung"],
                example_questions=["Wann habe ich heute Vorlesung?", "Was steht im Stundenplan?"]
            )
        ]
    ),
    Usecase(
        name="finances",
        questions=[
            Question(
                route="/briefing",
                keywords=["marktsituation", "finanzübersicht"],
                example_questions=["Wie ist die aktuelle Marktsituation?", "Gib mir eine Finzanzübersicht"]
            ),
            Question(
                route="/crypto",
                keywords=["krypto", "crypto", "wallet", "coin"],
                example_questions=["Wie stehen meine Kryptowährungen?"]
            ),
            Question(
                route="/favourites",
                keywords=["favoriten", "aktien", "portfolio"],
                example_questions=["Wie stehen meine Aktien?"]
            ),
            Question(
                route="/leading",
                keywords=["index", "dax"],
                example_questions=["Wie steht mein favorisierter Leitindex?"]
            ),
            Question(
                route="/wallstreetbets",
                keywords=["wallstreetbets", "trend", "reddit", "Stimmung", "GME"],
                example_questions=["Wie ist die Stimmung auf Reddit?"]
            ),
            Question(
                route="/nft",
                keywords=["nft"],
                example_questions=["Was passiert auf dem NFT Markt?"]
            )
        ]
    ),
    Usecase(
        name="journey",
        questions=[
            Question(
                route="/gasStations",
                keywords=["Tankstelle", "Tanken"], 
                example_questions=["Wo kann ich hier tanken?"]
            ),
            Question(
                route="/distance",
                keywords=["Weit", "Entfernung", "Weg", "entfernt"],
                example_questions=["Wie weit ist meine Arbeit weg?", "Wie weit ist meine Arbeit entfernt?"]
            ),
            Question(
                route="/route",
                keywords=["Route", "Strecke", "Wegbeschreibung"],
                example_questions=["Gib mir die Wegbeschreibung zu meiner Arbeit.", "Wie ist die Route zu meiner Arbeit?"]
            )
        ]
    ),
    Usecase(
        name="entertainment",
        questions=[
            Question(
                route="/briefing",
                keywords=["Entertainment", "Unterhaltung", "Abend", "unterhalten"],
                example_questions=["Was könnte ich heute Abend schauen?", "Schlage mir ein Abendprogramm vor"]
            ),
            Question(
                route="/movies",
                keywords=["Film"],
                example_questions=["Schlage mir einen Film vor.", "Welchen Film könnte ich heute Abend schauen?"]
            ),
            Question(
                route="/series",
                keywords=["Serie"],
                example_questions=["Schlage mir eine Serie vor.", "Welche Serie könnte ich heute Abend schauen?"]
            ),
            Question(
                route="/football",
                keywords=["Fußball", "Spiel", "Verein", "Bundesliga"],
                example_questions=["Was steht in der Bundesliga an?", "Wann spielt mein Lieblingsverein wieder?"]
            ),
            Question(
                route="/formulaOne",
                keywords=["Formel", "Rennen", "Circuit"],
                example_questions=["Welche Rennen stehen an?", "Was passiert in der Formel 1?"]
            ),
            Question(
                route="/comedy",
                keywords=["Witz", "lustig", "funny", "joke", "lach"],
                example_questions=["Erzähle mir einen Witz", "Sag etwas lustiges", "Bringe mich zum Lachen"]
            )

    ]
)
]

no_answer = [
    "Das habe ich leider nicht verstanden!",
    "Kannst du das nochmal wiederholen?",
    "Ich habe dich leider nicht verstanden."
]
