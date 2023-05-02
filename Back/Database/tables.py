import sqlite3

# Create database and connect
db = sqlite3.connect("./GP.db")

# Setting cursor
cr = db.cursor()

def init():
    # Create patients Table
    db.execute('PRAGMA foreign_keys = ON')
    cr.execute(
        '''
        CREATE TABLE IF NOT EXISTS patients 
        (id INTEGER PRIMARY KEY , name TEXT,age INTEGER ,gender TEXT , phone_number TEXT , email TEXT)
        ''')

    # Create sessions Table
    cr.execute(
        """
        CREATE TABLE IF NOT EXISTS sessions 
        (patient_id INTEGER NOT NULL REFERENCES patients(id),
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        audio_path TEXT,
        pathology_id INTEGER,
        doctor_diagnoses TEXT,
        Letters TEXT,
        Phrase TEXT)
        """
    )

    # Create pathologies Table
    cr.execute(
        "CREATE TABLE IF NOT EXISTS pathologies (id INTEGER, description TEXT, name TEXT, type TEXT)"
    )


# Save and close data
def save_close():
    db = sqlite3.connect("./GP.db")
    db.commit()
    db.close()


def connection():
    db = sqlite3.connect("./GP.db")
    return db.cursor()


def save():
    return db.commit()
