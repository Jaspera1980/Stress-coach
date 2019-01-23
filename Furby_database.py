import Data_encryption as crypt
import pymongo

#Set up database
#Set database variables
def startup():
    #Create MongoDB client
    client = pymongo.MongoClient('localhost', 27017)
    #Print result
    print("client started:")
    print(client)
    #Create database
    db = client['Furby']
    #Create collections/tables
    user_info = db['user_info']
    interv_stats = db['intervention_statistics']
    interv_db = db['intervention_database']
    #Encryption of data
    #Get stored key
    key = crypt.secure_key().decrypt_key('encryption_key.json')
    #Create encryption object
    Encrypt = crypt.encryption(key)
    #Check security level
    Encrypt.security_level()
    return user_info, interv_stats, interv_db, Encrypt

#Initiate variables
user_info, interv_stats, interv_db, Encrypt = startup()

#Function to add data encrypted to the database
def user_info_data(user_id, age, gender, sports = None, heart_rate_at_rest = None, voice_pattern_at_rest = None):
    data = {
        'user_id': Encrypt.encrypt(str(user_id)),
        'age': Encrypt.encrypt(str(age)),
        #0=male / 1=female
        'gender': Encrypt.encrypt(str(gender)),
        #0=no sport / 1=sports
        'sports': Encrypt.encrypt(str(sports)),
        'heart_rate_at_rest': Encrypt.encrypt(str(heart_rate_at_rest)),
        'voice_pattern_at_rest': Encrypt.encrypt(str(voice_pattern_at_rest))
    }
    return data

def interv_stats_data(event_id, age_range = None, gender = None, intervention_id = None, time_of_intervention = None, intervention_skipped = None, bpm_before_inv = None, bpm_after_inv = None, voice_pattern_variance = None, inv_successful = None):
    data = {
        'event_id': event_id,
        'age_range': age_range,
        'gender': gender,
        'intervention_id': intervention_id,
        'time_of_intervention': time_of_intervention,
        #0=no / 1=yes
        'intervention_skipped': intervention_skipped,
        'bpm_before_inv': bpm_before_inv,
        'bpm_after_inv': bpm_after_inv,
        'voice_pattern_variance': voice_pattern_variance,
        #0=no / 1=yes
        'inv_successful': inv_successful    
    }
    return data

def interv_db_data(intervention_id, intervention_text, intervention_ranking = None, success_rate = None, best_time_for_intervention = None):
    data = {
        'intervention_id': intervention_id,
        'intervention_text': intervention_text,
        'intervention_ranking': intervention_ranking,
        'success_rate': success_rate,
        'best_time_for_intervention': best_time_for_intervention
    }
    return data

#Function to retrieve and decrypt data
def get_entry(column):
    search = user_info.find_one()
    x = search[column]
    x = Encrypt.decrypt(x)
    x = int(x)
    return x

#Anonymize heart rate deviation
def bpm_dev(heart_rate):
    bpm_at_rest = get_entry('heart_rate_at_rest')
    anon_bpm = round((heart_rate/bpm_at_rest)-1, 4)
    return anon_bpm

#Age anonymizer
def age_range():
    age = get_entry('age')
    if age <20:
        return '0-19'
    if (age >= 20) and (age <30):
        return '20-29'
    if (age >=30) and (age <40):
        return '30-39'
    if (age >=40) and (age <50):
        return '40-49'
    if (age >=50) and (age <60):
        return '50-59'
    if (age >=60) and (age <70):
        return '60-79'
    if (age >=80):
        return '80+'
    else:
        return None

#Function to get intervention text
def get_inv_text(intervention_id):
    search = interv_db.find_one({'intervention_id': intervention_id})
    text = search['intervention_text']
    scen_dict = eval(text)
    return scen_dict

def new_entry_user_info(data):
    user_info.insert_one(data)
    
def new_entry_interv_stats_data(data):
    interv_stats.insert_one(data)

#pymongo.MIN_SUPPORTED_WIRE_VERSION = 0
#x = pymongo.MIN_SUPPORTED_WIRE_VERSION
#print(x)

#data = user_info_data(user_id=1, age=38, gender=0) #, sports=0, heart_rate_at_rest=60)
#data_ = interv_stats_data(12354)
#new_entry_interv_stats_data(data_)
print(user_info)

