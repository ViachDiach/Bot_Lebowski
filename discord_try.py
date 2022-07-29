import requests
import random

database, equel = [], []
id, iam = [], []



def trade(who, whom):
    equel[database.index(who)], equel[database.index(whom)] = equel[database.index(whom)], equel[database.index(who)]
    iam[id.index(who)], iam[id.index(whom)] = iam[id.index(whom)], iam[id.index(who)]

def check(teg):
    if teg in database:
        return(equel[database.index(teg)])
    else:
        return('нужно провериться')


def dushnila(teg):
    procent = random.randrange(0, 100)

    if teg in database:
        return('Уже взвешен')
    else:
        equel.append(procent)
        if teg in database:
            print()
        else:
            database.append(teg)

        return procent


def total():
    step, answer = [], ('')

    for i in range(len(database)):
        step.append(f'{database[i]} душный на {equel[i]} %')
    for j in step:
        answer += str(j)
        answer += '\n'

    return answer


def cut_str(open_resp):
    answer = list(i[:i.find('.') + 3] for i in open_resp)  # находим точку и округляем(срезаем строку)
    return answer


async def try_bot():
    response = requests.get('https://www.cbr-xml-daily.ru/latest.js')
    response = response.json()  # парсим json
    open_resp = [str(1 / response["rates"]["USD"]), str(1 / response["rates"]["EUR"]),
                 str(1 / response["rates"]["UAH"]), str(1 / response["rates"]["KZT"])]

    # выводим из словаря нужные значени по его ключу

    return cut_str(open_resp)



def mat(review):

    low = ['лучик солнца', 'милашка', 'прелесть', 'снежинка', 'умничка', 'пушок', 'лапочка', 'крошка', 'ягодка',
            'персик', 'конфетка', 'ангелочек', 'светлячок', 'птенчик', 'мурлыка', 'котенок', 'киса', 'умница']

    mid = ['хвойда', 'шльондра', 'курва', 'курвенний', 'шльодравий', 'хвойдяний', 'курвар', 'шльондер', 'хвойдник',
            'курварство', 'піхва', 'потка', 'піхвяний', 'піхвистий', 'спіхварити', 'вигнанець', 'грайня', 'алкомэн',
            'гейропеец', 'довбограник', 'награйка', 'прутень',  'прутня', 'прутнелиз', 'прутнявий',
           'three hundred bucks', 'cum ', 'dungeon master', 'boss of this gym', 'fucking slave', 'suck some dick',
           'чешский разбойник', 'балабоk', 'рохля', 'пузырь', 'любопытный', 'вошь', 'бісова ковінька', 'булька з носа',
           'пришелепкуватий', 'шмаркач', 'тюхтій', 'нездара', 'дурепа', 'йолоп', 'боров', 'быдло',  'пустобрех', 'вшивота',
           'трутень', 'лепешка', 'обалдуй', 'погань', 'профурсетка', 'хабалка', 'хмырь', 'shit',  'bastard', 'cunt',
           'motherfucker', 'fucking ass', 'slut', 'dumbass', 'бикукле', 'бикуля', 'рередикт']

    high = ['фуфло', 'душный козел', 'свиняче рило', 'підорко', 'обезьяна', 'шушера', 'sucker', 'son of a bitch',
             'желчный', 'бобик', 'loser', 'конь педальный', 'геморрой', 'шелупонь', 'пердун']

    if review in range(0, 41):
        lst = low
    elif review in range(41, 71):
        lst = mid
    else:
        lst = high

    today = lst[random.randint(0, len(lst))]

    return today


async def codwars(massage):

    response = requests.get(f'https://www.codewars.com/api/v1/users/{massage}')
    response = response.json()
    print(response)
    who = ('Не нахожу такого')
    if len(response) < 3:
        return (who)

    else:
        count = 1
        progress = []

        progress.append(f'**Ник**: {response["username"]}\n')
        progress.append(f'**Общий счет**: {response["honor"]}\n')
        if response["leaderboardPosition"] != None:
            progress.append(f'**Лидерборд**: {response["leaderboardPosition"]}\n')
        # progress.append(f' \n')
        progress.append(f'**Языки**:\n')
        for i in (response['ranks']['languages']):
            progress.append(f'{count}) {i}:\n\tРанг: {response["ranks"]["languages"][i]["name"]}\n\tСчет: {response["ranks"]["languages"][i]["score"]}\n')
            count += 1
        if response["skills"] != None:
            count = 1
            # progress.append(f' \n')
            progress.append(f'**Навыки**:\n')
            for j in (response["skills"]):
                progress.append(f"{count}) {j}\n")
                count += 1

        progress = ''.join(progress)
        print(progress)

        return (progress)







