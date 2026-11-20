from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-303, альбом
# Photos «1899 (ГАПО 182-5-303)» (pk 1238), ч. 2 — лл. 184об–193об, 36 браков, прочитана целиком 25.10.2026; л. 184 —
# шмуцтитул; импорта не было. Книга пишет «крестьянинъ села Кириллова». Жених и невеста — на левой странице, поручители —
# на правой. Венчали свящ. Александр Васильев Писарев и Павел Богословский.
kirillovo_marriages_1899 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "303",
    "Кириллово",
    "Казанская церковь",
    1899,
    *marriage_month(Month.FEBRUARY,
                    # Михаил Константинович Мальчиков — вдовец Варвары Трофимовны (ум. 18.06.1898)
                    marriage(9, 17,
                             groom=person("Михаилъ", "Константиновъ", "Мальчиковъ"), groom_marriage_num=2, groom_age=29,
                             bride=person("Марѳа", "Ѳеодорова", "Хрусталева", residence="Сядемка", comment="«крестьянка села Сядемки Спасскаго уѣзда»"),
                             bride_marriage_num=1, bride_age=20,
                             witness1=person("Василій", "Моисеевъ", "Поздняковъ", side=Side.GROOM),
                             witness2=person("Николай", "Ильинъ", "Ковалевъ", side=Side.GROOM),
                             witness3=person("Аѳанасій", "Яковлевъ", "Кобыльковъ", side=Side.BRIDE),
                             witness4=person("Димитрій", "Ѳеодоровъ", "Вядиновъ", side=Side.BRIDE, residence="Сядемка", comment="фамилия читается неуверенно"),
                             page="186об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # Григорий Степанович Мальчиков — сын Степана … ? не установлено
                    marriage(24, 5,
                             groom=person("Григорій", "Стефановъ", "Мальчиковъ"), groom_marriage_num=1, groom_age=19,
                             bride=person("Марія", "Леонтіева", "Абашева"), bride_marriage_num=1, bride_age=18,
                             witness1=person("Евдокимъ", "Ивановъ", "Бурлинъ", side=Side.GROOM),
                             witness2=person("Петръ", "Никитинъ", "Фетисовъ", side=Side.GROOM),
                             witness3=person("Алексѣй", "Антоновъ", "Абашевъ", side=Side.BRIDE),
                             witness4=person("Василій", "Антоновъ", "Абашевъ", side=Side.BRIDE),
                             page="190об",
                             reviewed=False),
                    # поручитель по невесте — Стефан Михайлович Мальчиков (кто — не установлено)
                    marriage(26, 5,
                             groom=person("Семенъ", "Терентьевъ", "Горбатовъ"), groom_marriage_num=1, groom_age=25,
                             bride=person("Анастасія", "Филиппова", "Галеева", residence="Сядемка", comment="«крестьянка села Сядемки»; фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=17,
                             witness1=person("Иванъ", "Ивановъ", "Барабановъ", side=Side.GROOM),
                             witness2=person("Андрей", "Ивановъ", "Верховъ", side=Side.GROOM),
                             witness3=person("Василій", "Григорьевъ", "Сорокинъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Стефанъ", "Михайловъ", "Мальчиковъ", side=Side.BRIDE),
                             page="190об",
                             reviewed=False),
                    # поручитель по жениху — Михаил Васильевич Мальчиков («Юлинъ»)
                    marriage(29, 8,
                             groom=person("Ѳеодоръ", "Егоровъ", "Красиковъ"), groom_marriage_num=1, groom_age=20,
                             bride=person("Дарія", "Егорова", "Дыркина"), bride_marriage_num=1, bride_age=19,
                             witness1=person("Михаилъ", "Васильевъ", "Юлинъ", side=Side.GROOM, comment="он же: Михаил Васильевич Мальчиков"),
                             witness2=person("Семенъ", "Ивановъ", "Красиковъ", side=Side.GROOM),
                             witness3=person("Петръ", "Ивановъ", "Щетининъ", side=Side.BRIDE),
                             witness4=person("Михаилъ", "Григорьевъ", None, side=Side.BRIDE, comment="фамилия у края («Ку…инъ»)"),
                             page="191об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
