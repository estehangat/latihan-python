import datetime

player1 = {
    'Name':'Erling Haaland',
    'Date':datetime.datetime(2000,7,21),
    'Goals':51,
    'Teams':'Manchester City',
    'Height':194
}

player2 = {
    'Name':'Kevin De Bruyne',
    'Date':datetime.datetime(1991,6,28),
    'Goals':93,
    'Teams':'Manchester City',
    'Height':181
}

player3 = {
    'Name':'Kylian Mbappé',
    'Date':datetime.datetime(1998,12,20),
    'Goals':164,
    'Teams':'Real Madrid',
    'Height':178
}

dataPlayer = {
    'key1':player1, # Output : 'key1': {'Name': 'Erling Haaland', 'Date': datetime.datetime(2000, 7, 21, 0, 0), 'Goals': 51, 'Teams': 'Manchester City', 'Height': 194}
    'key2':player2, # Output : 'key2': {'Name': 'Kevin De Bruyne', 'Date': datetime.datetime(1991, 6, 28, 0, 0), 'Goals': 93, 'Teams': 'Manchester City', 'Height': 181}
    'key3':player3  # Output : 'key3': {'Name': 'Kylian Mbappé', 'Date': datetime.datetime(1998, 12, 20, 0, 0), 'Goals': 164, 'Teams': 'Real Madrid', 'Height': 178}
}

print(f"| {'KEY':^6} | {'Name':^18} | {'Date':^10} | {'Goals':^5} | {'Teams':^18} | {'Height':^8} |") # Output : |  KEY   |        Name        |    Date    |       Teams        |  Height  |
print("="*85)

for key in dataPlayer:
    KEY = key
    NAME = dataPlayer[KEY]['Name'] # Output : Erling Haaland, Kevin De Bruyne, Kylian Mbappé
    DATE = dataPlayer[KEY]['Date'].strftime("%x") # Output : 07/21/00, 06/28/91, 12/20/98
    GOALS = dataPlayer[KEY]['Goals'] # Output : 51, 93, 164
    TEAMS = dataPlayer[KEY]['Teams'] # Output : Manchester City, Manchester City, Real Madrid
    HEIGHT = dataPlayer[KEY]['Height'] # Output : 194, 181, 178
    print(f"| {KEY:<6} | {NAME:<18} | {DATE:<10} | {GOALS:<5} | {TEAMS:<18} | {HEIGHT:<8} |")