import json
import sqlite3

def save_to_json(data, filename="output.json"):
    def convert(item):
        return {
            "text": item["word"],
            "label": item["entity_group"],
            "score": float(item["score"])  
        }

    cleaned_data = [convert(item) for item in data]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, indent=4)


def save_to_db(data, db_name="entities.db"):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS entities (
            entity TEXT,
            score REAL,
            label TEXT
        )
    """)
    for ent in data:
        c.execute("INSERT INTO entities VALUES (?, ?, ?)", 
                  (ent['word'], ent['score'], ent['entity_group']))
    conn.commit()
    conn.close()
