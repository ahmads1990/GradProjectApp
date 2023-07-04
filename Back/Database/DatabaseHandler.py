from Database.tables import connection, getCursor, save_close, save, init
from Database.dtos import Patient, Session, Pathology

class DatabaseHandler():
    def __init__(self):
        # Setting cursor
        self.db = connection()
        init(self.db, getCursor(self.db))

    # -----------------------------------------
    # # Insert Data In Tables
    # -----------------------------------------

    # patient
    def insert_patient(self, patient):
        cr = getCursor(self.db)
        cr.execute(f"""
                    INSERT INTO patients(id, name, age, gender, phone_number, email)
                    VALUES(
                        {patient.id}, 
                        '{patient.name}',
                        {patient.age},
                        '{patient.gender}',
                        '{patient.phone}',
                        '{patient.email}')")
                    """)
        save(self.db)

    # session
    def insert_session(self, session):
        cr = getCursor(self.db)
        cr.execute(
        f"""
        INSERT INTO sessions (patient_id, audio_path, pathology_id, doctor_diagnoses, Letters, Phrase)
        VALUES (
            {session.patient_id},
            '{session.audio_path}',
            {session.pathology_id},
            '{session.doctor_diagnoses}',
            {int(session.letters)},
            {int(session.phrase)}
        );
        """)
        save(self.db)
        
        last_inserted_id = cr.lastrowid  # Retrieve the newly created primary key
        return last_inserted_id

    # pathology
    def insert_pathology(self, id, description, name, type):
        cr = getCursor(self.db)
        cr.execute(f"INSERT INTO pathologies VALUES({id}, '{description}', '{name}', '{type}')")
        save(self.db)

    # -----------------------------------------
    # Select All data
    # -----------------------------------------
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

    # -----------------------------------------
    # Select by ID
    # -----------------------------------------

    # patient
    def select_patient_by_id(self, patient_id):
        cr = getCursor(self.db)
        # Execute the SELECT query
        cr.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))    

        # Fetch the result
        result = cr.fetchone()
        # Map the result to Patient DTO object
        if result:
            patient = Patient(result[0], result[1], result[5], result[4], result[2], result[3])
            return patient
        else:
            return None
        
    # sessions
    def select_sessions_by_patient_id(self, patient_id):
        cr = getCursor(self.db)
        # Execute the SELECT query
        cr.execute("SELECT * FROM sessions WHERE patient_id = ?", (patient_id,))

        # Fetch all the results
        results = cr.fetchall()
        # Map the results to SessionDto objects
        sessions = []
        for result in results:
            session = Session(result[0], result[2], result[3], result[4], result[5], result[6])
            sessions.append(session)

        return sessions
    # pathology 
    def get_pathology_by_name(self, name):
        cr = getCursor(self.db)
        # Execute the SELECT query
        cr.execute("SELECT * FROM pathologies WHERE name = ?", (name,))
        # Fetch the result
        result = cr.fetchone()

        # If no result found, return None
        if result is None:
            return None

        # Create a Pathology object from the result
        pathology = Pathology(result[0], result[1], result[2], result[3])

        return pathology
    # -----------------------------------------
    # Delete by ID
    # -----------------------------------------
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

    # -----------------------------------------
    # Update
    # -----------------------------------------

    def update_session_pathology_id(self,session_id, pathology_id):
        cr = getCursor(self.db)
        # Execute the UPDATE query
        cr.execute("UPDATE sessions SET pathology_id = ? WHERE session_id = ?", (pathology_id, session_id))

        # Commit the changes
        save(self.db)

    def phrases_letters(self, session_id):
        cr = getCursor(self.db)
        query = f"UPDATE sessions SET Letters='DONE', Phrase='DONE' WHERE session_id={session_id}"
        cr.execute(query)
        save(self.db)
