# building up a coffee machine
# TODO: print the report

def total_coint(penny, nickel, cent, quarter):
    return penny + nickel + cent + quarter


def collect_coins():
    penny = eval(input('enter amount of penny:  $'))
    penny = 0.01 * penny
    nickel = eval(input('enter amount of nickel:  $'))
    nickel = 0.05 * nickel
    cent = eval(input('enter amount of cent:  $'))
    cent = 0.1 * cent
    quarter = eval(input('enter amount of quarter:  $'))
    quarter = 0.25 * quarter
    total1 = total_coint(penny, nickel, cent, quarter)
    return total1


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def choice1(decision):
    test = MENU[decision]
    test1 = test['ingredients']
    test2 = test1['water']
    test3 = test1['coffee']
    return test2


def choice2(decision):
    test = MENU[decision]
    test1 = test['ingredients']
    test2 = test1['water']
    test3 = test1['milk']
    return test3


def choice3(decision):
    test = MENU[decision]
    test1 = test['ingredients']
    test4 = test1['coffee']
    return test4


def report1(get1):
    water = choice1(get)
    resources['water'] = resources['water'] - water
    return resources['water']


def report2(get2):
    water = choice2(get)
    resources['milk'] = resources['milk'] - water
    return resources['milk']


def report3(get3):
    water = choice3(get)
    resources['coffee'] = resources['coffee'] - water
    return resources['coffee']


def getting(a):
    test = MENU[a]
    store = test['cost']
    return store


a1 = 0
a2 = 0
a3 = 0
i = 0
money = 0
total = 0
damn = True
while damn:
    print('these are the various prices:   espresso :$1.5  latte :$2.5 cappuccino:$3.0 ')
    if resources['water'] < 50:
        print('the machine is out of resources')
        print('thank-you for using our service')

    print("do you want (espresso/latte/cappuccino:  ")
    get = input('').lower()
    # print(choice1(get))
    if get == 'report'  and a1 != 0:
        resources['water'] = a1
        resources['milk'] = a2
        resources['coffee'] = a3
        print(f'water: {resources["water"]} g \nmilk: {resources["milk"]} g \ncoffee: {resources["coffee"]} g')
    elif get == 'report':
        print(f'water:{resources["water"]} g \n milk:{resources["milk"]} g \n coffee:{resources["coffee"]} g')
    elif get == 'money':
        print(f"total balance:  ${money}")
    else:
        if choice1(get) > resources['water'] and i != 0:
            print("the machine doesn't have sufficient funds")
        else:
            if get == 'espresso':
                share = collect_coins()
                store = getting(get)
                if share < store:
                    print('insufficient funds')
                    print('thank-you for using our service')
                    break
                else:
                    print(f"this is your change : ${round(share - store, 2)}")
                    print('enjoy your espresso')

                    a1 = report1(get)
                    # a2 = report2(get)
                    a3 = report3(get)
                    # print(a2)
                    money += store
            elif get == 'latte':
                share = collect_coins()
                store = getting(get)
                if share < store:
                    print('insufficient funds')
                else:
                    print(f"this is your change : ${round(share - store, 2)}")
                    print('enjoy your latte')
                    a1 = report1(get)
                    a2 = report2(get)
                    a3 = report3(get)
                    money +=store

            elif get == 'cappuccino':
                share = collect_coins()
                store = getting(get)
                if share < store:
                    print('insufficient funds')
                else:
                    print(f"this is your change : ${round(share - store, 2)}")
                    print('enjoy your cappuccino')
                    a1 = report1(get)
                    a2 = report2(get)
                    a3 = report3(get)
                    money += store

            else:
                print('wrong input')
    if get == 'espresso':
        a2 = resources['milk']

    i += 1
