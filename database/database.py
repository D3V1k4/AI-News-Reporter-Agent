import sqlite3

DB_NAME = "database/news.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        summary TEXT,
        source TEXT,
        published TEXT,
        link TEXT UNIQUE,
        category TEXT,
        companies TEXT,
        score INTEGER,
        emailed INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_articles(news):
    conn = get_connection()
    cursor = conn.cursor()

    for article in news:
        try:
            cursor.execute("""
            INSERT INTO news(
                title,
                summary,
                source,
                published,
                link,
                category,
                companies,
                score
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                article["title"],
                article["summary"],
                article["source"],
                article["published"],
                article["link"],
                article["category"],
                ",".join(article["companies"]),
                article["score"]
            ))

        except sqlite3.IntegrityError:
            # Skip duplicate links
            pass

    conn.commit()
    conn.close()
def get_articles():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM news
        ORDER BY score DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows