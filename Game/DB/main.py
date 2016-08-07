from sqlite3 import connect


def get_widgets_text(menu_id, widgets_type):
    con = connect("DB/ru-ru.db")
    cur = con.cursor()
    for i in cur.execute(
                         'SELECT text '
                         'FROM menu '
                         'WHERE '
                            'id = {} '
                            'AND '
                            'widget_type = {} '
                         'ORDER BY widget_id'.format(menu_id, widgets_type)):
        yield i[0]


class DataBaseIdEnum:
    MainMenu = 0
    NotMainMenu = 1


class DataBaseWidgetTypeEnum:
    Button = 0
    Labels = 1
    Widget = 2