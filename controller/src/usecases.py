usecases = {
    {
        "name": "briefing",
        "questions": [
            {
                "route": "/briefing",
                "keywords": ["willkommen", "guten morgen", "briefing"],
                "example_questions": ["Gib mir ein Briefing für den Tag", "Zeig mir den Guten Morgen Dialog"]
            },
            {
                "route": "/wetter",
                "keywords": ["wetter"],
                "example_questions": ["Wie wird das Wetter heute ?"]
            },
            {
                "route": "/todo",
                "keywords": ["todo", "zu tun"],
                "example_questions": ["Was steht auf meiner Todo Liste?", "Was gibt es heute zu tun?"]
            },
            {
                "route": "/calendar",
                "keywords": ["kalender", "termin", "termine"],
                "example_questions": ["Was steht heute im Kalender?", "Welche Termine habe ich heute?"]
            },
        ]
    },
}

if __name__ == "__main__":
    pass
