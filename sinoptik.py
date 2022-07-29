import requests
from bs4 import BeautifulSoup
import psycopg2


async def lazyjob(massage):

    # добавить модуль ОпенВПН, чтобы бот сам коннектился к  БД  https://pypi.org/project/openvpn-api/

    opperator = massage.lower()
    name = ''

    if opperator in ('влад', 'владик', 'владислав', 'владосик', 'марков', 'vlad'):
        name = 'Влад'
    elif opperator in ('дед', 'дедушка', 'максим', 'султанов', 'maksim'):
        name = 'Максим'
    elif opperator in ('слава', 'славик', 'дьяченко', 'вячеслав', 'slavik', 'slava'):
        name = 'Слава'
    else:
        return ('Кто? Давай еще раз.\n❗Выбери Влада/Славу/Максима❗')

    who = {'Влад': 2874036,
              'Максим': 10508346,
              'Слава': 5550347
              }

    worker = who[name]
    print(worker)

    connection = psycopg2.connect(user='nikita_evsyukov',
                                  password='TJcj8pFtYrbIbzVuusXa',
                                  host='pgsql-crm-customer-support-repl.skyeng.link',
                                  port='5432',
                                  database='crm_customer_support')

    alljob = []

    cursor = connection.cursor()
    cursor.execute(f'select t.operator_id, t.user_id as taskUser, age((now() - interval \'3 hour\'), t.selected_at) as inTask, td.extra::jsonb->\'comment\' as comment from public.task t join public."operator" o on o.user_id = t.operator_id join public.task_details td on td.id = t.task_details_id where t.operator_group_id = 22 and t.status = \'processing\'')
    record = cursor.fetchmany()

    for row in cursor:
        alljob.append(row)
        print(row)

    print(alljob)
    print(len(alljob))

    cursor.close()
    connection.close()


async def pogoda(massage):

    massage = massage.lower()
    city = massage.title()

    response = requests.get(f'https://sinoptik.ua/погода-{massage}')

    if response:
        print('город найден')
    else:
        return 'Ерунда какая-то, не могу найти, попробуй еще раз\nP.S напиши по-русски город на планете Земля'

    soup = BeautifulSoup(response.text, "html.parser")

    p3=soup.select('.temperature .p3')
    pogoda1=p3[0].getText()
    p4=soup.select('.temperature .p4')
    pogoda2=p4[0].getText()
    p5=soup.select('.temperature .p5')
    pogoda3=p5[0].getText()
    p6=soup.select('.temperature .p6')
    pogoda4=p6[0].getText()

    p=soup.select('.rSide .description')
    pogoda=p[0].getText()
    x = pogoda.strip()

    name = (f'{city} сегодня:')
    report=(f'{x}\nУтром : {pogoda1} {pogoda2}\nДнём : {pogoda3} {pogoda4}')

    return (name, report)


