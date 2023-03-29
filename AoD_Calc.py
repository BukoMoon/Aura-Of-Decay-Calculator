import os

SIZE = int(os.get_terminal_size().columns)

def result(current_health, total_health, damage_tick, health_regen, heal_amount):
    if current_health > 0:
        remaining_health = ((total_health - current_health) / total_health) * 100
        print('~' * SIZE)
        print('~' * round((SIZE / 2 - 8)) + ' AoD sustained! ' + '~' * (round(SIZE / 2 - 8)))
        print('~' * SIZE)
        print(f'Percent of Health Remaining: {round(remaining_health)}%'.center(SIZE))
    else:
        print('~' * round((SIZE / 2 - 11)) + 'AoD failed to sustain!' + '~' * round((SIZE / 2 - 11)))
    
    print(f'Total Health: {total_health}'.center(SIZE))
    print(f'Healing: {heal_amount + health_regen}'.center(SIZE))
    print(f'Damage Taken Per Tick of Poison: {round(damage_tick)}'.center(SIZE))


def calc(total_damage, total_health, health_regen, healing_effectiveness, dot_reduction, points):
    base_poison = 28
    effect = 1 + healing_effectiveness / 100
    current_health = total_health
    total_damage = base_poison * (1 + (total_damage / 100))

    if points == True:
        dr = dot_reduction / 100 + (0.05 * points)
    else:
        dr = dot_reduction / 100
    
    damage_tick = (total_damage - (total_damage * dr))
    heal = round((damage_tick * 0.08) * effect)
    
    z = 0
    while current_health > 0:
        if current_health > total_health: 
            current_health = total_health
        if heal + health_regen > damage_tick:
            break
        if current_health - damage_tick < 0:
            current_health = 0
            break   
        current_health = current_health - damage_tick + heal + health_regen
        heal = round(((total_health - current_health) * 0.08) * points)
        z += 1
        if z == 10:
            break

    result(current_health, total_health, damage_tick, health_regen, heal)

def error():
    print('Invalid Input. Try again.')

def main():
    questionaire = {
        'Poison Damage': "How much poison damage do you have? ",
        'DoT': "How much DoT damage do you have? ",
        'Health': "How much health do you have? ",
        'Health Regen': "How much regen do you have? ",
        'Health Effectiveness': "How much healing effectiveness do you have? ",
        'DoT Reduction': "How much less damage over time do you have? "
    }

    input_values = {
        'Poison Damage': -1,
        'DoT': -1,
        'Health': -1,
        'Health Regen': -1,
        'Health Effectiveness': -1,
        'DoT Reduction': -1
    }

    for i in questionaire:
        try:
            input_values[i] = int(input(questionaire[i]))
        except ValueError:
            error()

    while True:
        try:
            points = int(input("How many points in Innoculation do you have? "))
        except ValueError:
            error()
        if points >= 0 and points <= 4:
            print()
            break
        else:
            error()
    
    damage = input_values['Poison Damage'] + input_values['DoT'] 
 
    calc(damage, input_values['Health'], input_values['Health Regen'], input_values['Health Effectiveness'], input_values['DoT Reduction'], points)


if __name__ == "__main__":
    main()
    