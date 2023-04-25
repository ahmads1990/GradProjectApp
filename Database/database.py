from Database.tables import connection , save_close , save


#setting cursor
cr = connection()

################################## Insert Data In Tables ##################################

def insert_patient(id , name , gender , phone , email):
    cr.execute(f"INSERT INTO patients(id , name , gender , phone_number , email) VALUES( {id} , '{name}' , '{gender}' , '{phone}','{email}')")
    save_close()
def insert_session(patient_id , session_id ,audio_path, pathology_id , doctor_diagnoses , Letters , Phrase ):
    cr.execute(
        f"INSERT INTO sessions VALUES ({patient_id} , '{session_id}','{audio_path}' ,'{pathology_id}' , '{doctor_diagnoses}','{Letters}' , '{Phrase}') ")
    save_close()
def insert_pathologie(id , description , name , type):
    cr.execute(
        f"INSERT INTO pathologies VALUES({id} , '{description}' , '{name}','{type}')")
    save_close()

############################# select All data ########################################
def all_data_patients():
    cr.execute(f"SELECT * FROM patients")
    data = cr.fetchall()
    save_close
    return data
def all_data_sessions():
    cr.execute(f"SELECT * FROM sessions")
    data = cr.fetchall()
    save_close
    return data
def all_data_pathologies():
    cr.execute(f"SELECT * FROM pathologies")
    data = cr.fetchall()
    save_close
    return data

############################### delete row from Id ####################################

def delete_patient(id):
    cr.execute(f"DELETE FROM patients WHERE id={id}")
    save_close()

def delete_session(session_id):
    cr.execute(f"DELETE FROM sessions WHERE session_id={session_id}")
    save_close()

def delete_pathologie(id):
    cr.execute(f"DELETE FROM pathologies WHERE id={id}")
    save_close()

