import sqlite3

def connection():
    # Create database and connect
    import os
    print(os.getcwd())
    db = sqlite3.connect("Database/GP.db")
    return db

def getCursor(db):
    return db.cursor()

# Save and close data
def save_close(db):
    db.commit()
    db.close()

def save(db):
    return db.commit()

def init(db, cr):
    # Create patients Table
    db.execute('PRAGMA foreign_keys = ON')
    cr.execute(
        """
        CREATE TABLE IF NOT EXISTS patients 
        (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            phone_number TEXT,
            email TEXT
        );
        """
    )
    # Create sessions Table
    cr.execute(
        """
        CREATE TABLE IF NOT EXISTS sessions 
        (
            patient_id INTEGER NOT NULL REFERENCES patients(id),
            session_id INTEGER PRIMARY KEY AUTOINCREMENT,
            audio_path TEXT,
            pathology_id INTEGER,
            doctor_diagnoses TEXT,
            Letters INTEGER,
            Phrase INTEGER
        );
        """
    )
    # Create pathologies Table
    cr.execute(
        """
        CREATE TABLE IF NOT EXISTS pathologies 
        (
            id INTEGER,
            description TEXT,
            name TEXT,
            type TEXT
        );
        """
    )



