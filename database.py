import Furby_database as fdb
import pymongo
import pprint

#fdb.get_entry('user_id')
data = fdb.user_info_data(user_id=1, age=38, gender=0, sports=0, heart_rate_at_rest=60)

pprint.pprint(data)
fdb.new_entry_user_info(data)


