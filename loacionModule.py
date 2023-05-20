'''from math import sin, cos, sqrt, atan2, radians # approximate radius of earth in km 
R = 6373.0 

def distanceBWlocations(lati1,long1,lati2,long2):
    lat1 = radians(lati1) 
    lon1 = radians(long1) 
    lat2 = radians(lati2) 
    lon2 = radians(long2) 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2 
    c = 2 * atan2(sqrt(a), sqrt(1 - a)) 
    distance = R * c *1000 
    return distance
data_set={
    'users':[{'id':1,'logitude':31.63545781744966,'latitude':74.82576083527395},
    {'id':2,'logitude':31.6352981744966,'latitude':74.82576083687395},
    {'id':5,'logitude':31.6352981244966,'latitude':74.82576083687395},
    {'id':8,'logitude':31.6352981725966,'latitude':74.82576083645395},
    {'id':10,'logitude':31.6353321744966,'latitude':74.82578083687395}],
}#from db
lat1=74.82576083687395#from user
long1=31.6352981744966#from user
sorted_lst = []
for user_data_set in data_set['users']:
    
    x = distanceBWlocations(lat1,long1,user_data_set.get('latitude'),user_data_set.get('logitude'))
    sorted_lst.append({'dist':x,'id':user_data_set.get('id')})
sorted_data = sorted(sorted_lst , key = lambda i: i['dist'])

#31.6352981744966, 74.82576083687395
#31.63518275611522, 74.82585333824244
'''
