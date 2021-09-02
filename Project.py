import csv
import random
from datetime import datetime, timedelta
from datetime import date

class GameSchedule():
    def __init__(self,noOfGames):
        self.noOfGames=noOfGames

    def generate_date(self):
        played_date = []
        while len(played_date) < 5:
            start_date = date(2021, 8, 1)
            end_date = date(2021, 8, 31)
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + timedelta(days=random_number_of_days)
            if random_date.weekday() == 1:
                pass
                print("date is tuesday")
            else:
                played_date.append(random_date)
        return played_date


    def generate_game_id(self):
        game_id = []
        while len(game_id) < 5:
            game = random.randint(1, 5)
            if game not in game_id:
                game_id.append(game)
        return game_id


    def create_schedule(self):
        game_schedule = {}
        game_id = []
        no_of_players = []
        played_date = []
        player_id = {}
        for i in range(self.noOfGames):
            player = random.randint(75, 125)
            no_of_players.append(player)
        game_id = self.generate_game_id()
        played_date = self.generate_date()
        print(game_id)
        print(no_of_players)
        print(played_date)

        for i in range(len(game_id)):
            player_id.setdefault(i, {})["game_id"] = game_id[i]
            player_id.setdefault(i, {})["played_date"] = played_date[i]
            player_id.setdefault(i, {})["player_id"] = []
            player_id.setdefault(i, {})["points"] = []

            tempPlayersList = []
            tempPointList = []
            while len(tempPlayersList) < no_of_players[i]:
                player = random.randint(1, 125)
                if player not in tempPlayersList:
                    tempPlayersList.append(player)
            player_id.setdefault(i, {})["player_id"] = tempPlayersList
            while len(tempPointList) < no_of_players[i]:
                point = random.randint(75, 200)
                tempPointList.append(point)
            player_id.setdefault(i, {})["points"] = tempPointList

        print(player_id)

        return player_id


    def store_csv(self):
        dataFormat={}
        dataToWrite=[]
        data = self.create_schedule()
        field_names = ['game_id', 'player_id', 'played_date', 'points']

        with open('Playerdfsd.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            j=0
            for value in data.values():
                j=j+1
                game_id = value['game_id']
                player_id = value['player_id']
                played_date = value['played_date']
                points = value['points']
                print(type(points))
                print("first loop: {}".format(j))
                for i in range(len(player_id)):
                    print("yes")
                    dataFormat["game_id"]=game_id
                    dataFormat["played_date"]=played_date
                    dataFormat["player_id"]=player_id[i]
                    dataFormat["points"]=points[i]
                    if dataFormat not in dataToWrite:
                        dataToWrite.append(dataFormat)
                    writer.writerows(dataToWrite)
                    print("in second loop: {}, {}".format(j,i))



obj=GameSchedule(5)
obj.store_csv()



lis1 = []
with open('Playerdfsd.csv') as f1:
    csvrow = csv.reader(f1, delimiter=",")
    next(csvrow)
    lis =[]
    for row in csvrow:
        lis.append(row)

    for row in lis:
        sam = []
        if row == sam:
            pass
        else :
            lis1.append(row)

lis2 = []
for i in range(len(lis1)):
     lis2.append(int(lis1[i][3]))

lis2.sort()
max_points = lis2[-5:]
min_points = lis2[:5]









