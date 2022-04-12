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
                keywords=["Marktsituation", "Finanzübersicht"],
                example_questions=["Wie ist die aktuelle Marktsituation?", "Gib mir eine FInzanzübersicht"]
            ),
            Question(
                route="/crypto",
                keywords=["Krypto", "crypto", "Wallet", "coin"],
                example_questions=["Wie stehen meine Kryptowährungen?"]
            ),
            Question(
                route="/favourites",
                keywords=["Favoriten", "Aktien", "Portfolio"],
                example_questions=["Wie stehen meine Aktien?"]
            ),
            Question(
                route="/leading",
                keywords=["Index", "DAX"],
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
    )
]

no_answer = [
    "Das habe ich leider nicht verstanden!",
    "Kannst du das nochmal wiederholen?",
    "Ich habe dich leider nicht verstanden."
]
