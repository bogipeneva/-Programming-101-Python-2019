from CodingSkills import read_json
import sys
import random
import json

class Car():

    def __init__(self, car, model, max_speed):

        self.validate_income_data(car, model, max_speed)

        self.car = car
        self.model = model
        self.max_speed = max_speed

    def validate_income_data(self, car, model, max_speed):
        if not isinstance(car, str):
            raise TypeError('invalid type of data')
        if not isinstance(model, str):
            raise TypeError('invalid type of data')
        if not isinstance(max_speed, int):
            raise TypeError('invalid type of data')
        if max_speed < 0:
            raise ValueError('Invalid max_speed, it must be positive value')

    def __str__(self):
        return ('Car:'+' '+self.car+'\n'+'Model:'+' '+self.model+'\n'+'Max_speed:'+' '+str(self.max_speed))

    def __eq__(self, other):
        return self.car == other.car and self.model == other.model and self.max_speed == other.max_speed


class Driver():

    def __init__(self, name, car):

        self.validate_driver_data(name, car)

        self.name = name
        self.car = car

    def validate_driver_data(self, name, car):
        if not isinstance(name, str):
            raise TypeError('invalid type of data')
        if not isinstance(car, Car):
            raise TypeError('invalid type of data')

    def __str__(self):
        string = 'Driver name:' +' '+self.name+'\n'+str(self.car)
        return string

    def __eq__(self, other):
        return self.name == other.name

class Race:
    def __init__(self, drivers, crash_chance):
        self.drivers = drivers
        self.crash_chance = crash_chance

    def validate_race_data(self, drivers, crash_chance):
        pass

    def result(self):
        crashed_drivers = []
        standings_after_the_race = {}
        drivers_for_cur_race = {}

        for index in range(len(self.crash_chance)):
            if self.crash_chance[index] > 0.7:
                self.crash_chance[index] = 0
            driver_speed = self.drivers[index].car.max_speed * self.crash_chance[index]
            drivers_for_cur_race.update({self.drivers[index].name: driver_speed})

        drivers_for_cur_race = sorted(drivers_for_cur_race.items(), key=lambda x: x[1], reverse = True)
        i = 0

        for key, value in drivers_for_cur_race:
            if value == 0:
                standings_after_the_race.update({key:'crashed'})
                crashed_drivers.append('Unfortunately, '+key+' has crashed.')
                i += 1
            elif i < 3:
                if i == 0:
                    standings_after_the_race.update({key:'8'})
                    crashed_drivers.append(key +' '+'8')
                    i += 1
                elif i == 1:
                    standings_after_the_race.update({key:'6'})
                    crashed_drivers.append(key +' '+'6')
                    i += 1
                else:
                    standings_after_the_race.update({key:'4'})

                    crashed_drivers.append(key +' '+'4')
                    i += 1

        return standings_after_the_race





class Championship:
    def __init__(self, name, races_count):
        self.name = name
        self.races_count = races_count

    def top3(self):
        pass

def main():
    cars_data = read_json('cars.json')

    drivers = []

    for person in cars_data['people']:
        car = Car(person['car'], person['model'], person['max_speed'])
        driver = Driver(person['name'], car)
        drivers.append(driver)

    points = {driver.name:0 for driver in drivers}
    chances = []
    drivers_for_cur_race = {}
    championship = Championship('panda', 1)
    for race in range(2):
        print('Race'+' #'+ str(race + 1) +'\n'+'###### START ######')
        for driver in cars_data['people']:
            chances.append(random.random())
        crashed_drivers = []
        curr_race = Race(drivers, chances)
        race_standings = curr_race.result()
        race_stand = sorted(race_standings.items(), key=lambda x: x[1], reverse = True)
        for tuples in race_stand:
            if tuples[1] != 'crashed':
                points[tuples[0]] += int(tuples[1])
                print(tuples[0]+'-'+tuples[1])
            else:
                crashed_drivers.append('Unfortunately, '+tuples[0]+' has crashed.')
        for drv in crashed_drivers:
            print(drv)
        print('\n')
        with open('result.json', 'a') as outfile:  
            json.dump(race_standings, outfile)
        chances = []

    
    print('Total championship standings:')
    points = sorted(points.items(), key=lambda x: x[1], reverse = True)
    for point in points:
        print(point[0]+'-'+str(point[1]))

    with open('result.json', 'a') as outfile:  
            json.dump(points, outfile)
'''
            driver.update({'chance':chance_to_crash})
            driver_speed = driver['max_speed'] * driver['chance']
            drivers_for_cur_race.update({driver['name']: driver_speed})

        drivers_for_cur_race = sorted(drivers_for_cur_race.items(), key=lambda x: x[1], reverse = True)
        i = 0

        for key, value in drivers_for_cur_race:
            if value == 0:
                print('Unfortunately, '+key+' has crashed.')
                i += 1
            elif i < 3:
                if i == 0:
                    points[key] += 8
                    print(key+' '+'8')
                    i += 1
                elif i == 1:
                    points[key] += 6
                    print(key+' '+'6')
                    i += 1
                else:
                    points[key] += 4
                    print(key+' '+'4')
                    i += 1

        print(drivers_for_cur_race)

    
    
'''
if __name__ == '__main__':
    main()