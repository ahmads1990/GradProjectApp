class Patient:
     def __init__(self,id,name,email,phone,age, gender):
         self.id = id
         self.name =  name
         self.email = email
         self.phone =  phone
         self.age = age  
         self.gender =gender
        
class Session:
      def __init__(self,patient_id, audio_path, pathology_id, doctor_diagnoses, letters, phrase):
         self.patient_id = patient_id
         self.audio_path = audio_path
         self.pathology_id =  pathology_id
         self.doctor_diagnoses = doctor_diagnoses
         self.letters = letters
         self.phrase = phrase
   