from Database.tables import connection, getCursor, save_close, save, init
from Database.dtos import Patient, Session

class DatabaseHandler():
    def __init__(self):
        # Setting cursor
        self.db = connection()
        init(self.db, getCursor(self.db))

    # Insert Data In Tables
    def insert_patient(self, patient):
        cr = getCursor(self.db)
        cr.execute(f"INSERT INTO patients(id, name, age, gender, phone_number, email) \
                VALUES({patient.id}, '{patient.name}', {patient.age}, '{patient.gender}', '{patient.phone}', '{patient.email}')")
        save(self.db)


    def insert_session(self, session):
        cr = getCursor(self.db)
        cr.execute(f"INSERT INTO sessions (patient_id, audio_path, pathology_id, doctor_diagnoses, Letters, Phrase)\
                VALUES ({session.patient_id}, '{session.audio_path}', '{session.pathology_id}', '{session.doctor_diagnoses}', '{session.letters}', '{session.phrase}')")
        save(self.db)


    def insert_pathology(self, id, description, name, type):
        cr = getCursor(self.db)
        cr.execute(f"INSERT INTO pathologies VALUES({id}, '{description}', '{name}', '{type}')")
        save(self.db)


    # Select All data
    def all_data_patients(self):
        cr = getCursor(self.db)
        cr.execute(f"SELECT * FROM patients")
        data = cr.fetchall()
        return data


    def all_data_sessions(self):
        cr = getCursor(self.db)
        cr.execute(f"SELECT * FROM sessions")
        data = cr.fetchall()
        return data


    def all_data_pathologies(self):
        cr = getCursor(self.db)
        cr.execute(f"SELECT * FROM pathologies")
        data = cr.fetchall()
        return data


    # Delete row from Id
    def delete_patient(self, id):
        cr = getCursor(self.db)
        cr.execute(f"DELETE FROM patients WHERE id={id}")
        save(self.db)


    def delete_session(self, session_id):
        cr = getCursor(self.db)
        cr.execute(f"DELETE FROM sessions WHERE session_id={session_id}")
        save(self.db)


    def delete_pathology(self, id):
        cr = getCursor(self.db)
        cr.execute(f"DELETE FROM pathologies WHERE id={id}")
        save(self.db)


    def phrases_letters(self, session_id):
        cr = getCursor(self.db)
        query = f"UPDATE sessions SET Letters='DONE', Phrase='DONE' WHERE session_id={session_id}"
        cr.execute(query)
        save(self.db)
