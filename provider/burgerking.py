from provider.utils import get_dom

URL = "http://burgerking.hu/cikkek/friss-hirek/uj-hetkoznapi-burger-king-menu"

def getMenu(today):
    day = today.weekday()
    try:
        dom = get_dom(URL)
        weeklymenu = dom.xpath('//*[@id="tabs-0"]/div[7]/div/p[5]//text()')
        weeklymenu = [item.strip() for item in weeklymenu if not item.isspace()]
        add_separator = lambda s: "||" + s if ':' in s and not 'Hétfő' in s else s
        menu = ' '.join([add_separator(i) for i in weeklymenu]).split('||')[day]
    except:
        menu = ''

    return {
        'name': 'Burger King',
        'url': URL,
        'menu': menu
    }

if __name__ == "__main__":
    from datetime import datetime
    print(getMenu(datetime.today()))
