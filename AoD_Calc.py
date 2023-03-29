import os

SIZE = int(os.get_terminal_size().columns)

def result(h, health, tick, regen, heal):
    if h > 0:
        remaining = ((health - h) / health) * 100
        print('~' * SIZE)
        print('~' * round((SIZE / 2 - 8)) + ' AoD sustained! ' + '~' * (round(SIZE / 2 - 8)))
        print('~' * SIZE)
        print(f'Percent of Health Remaining: {round(remaining)}%'.center(SIZE))
    else:
        print('~' * round((SIZE / 2 - 11)) + 'AoD failed to sustain!' + '~' * round((SIZE / 2 - 11)))
    
    print(f'Total Health: {health}'.center(SIZE))
    print(f'Healing: {heal + regen}'.center(SIZE))
    print(f'Damage Taken Per Tick of Poison: {round(tick)}'.center(SIZE))


def calc(poison, health, regen, eff, dotr, x):
    base_poison = 28
    e = 1 + eff / 100
    h = health
    poison = base_poison * (1 + (poison / 100))

    if x == True:
        dr = dotr / 100 + (0.05 * x)
    else:
        dr = dotr / 100
    
    tick = (poison - (poison * dr))
    heal = round((tick * 0.08) * e)
    
    z = 0
    while h > 0:
        if h > health: 
            h = health
        if heal + regen > tick:
            break
        if h - tick < 0:
            h = 0
            break   
        h = h - tick + heal + regen
        heal = round(((health - h) * 0.08) * e)
        z += 1
        if z == 10:
            break

    result(h, health, tick, regen, heal)

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
    