import sqlite3
from pathlib import Path
_memory = {}
DB_PATH = Path(__file__).parent / "memory.db"
def add_memory(mem_type: str, content: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO memory (type, content) VALUES (?, ?)",
        (mem_type, content)
    )
    conn.commit()
    conn.close()

def get_recent_memories(limit: int = 5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT type, content FROM memory ORDER BY timestamp DESC LIMIT ?",
        (limit,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows

# STEP 2 memory API
def store(key, value):
    _memory[key] = value

def recall(key):
    return _memory.get(key)
