import requests
from bs4 import BeautifulSoup



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


