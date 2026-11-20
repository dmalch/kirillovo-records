from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, SOLDIER

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-293, альбом
# Photos «1905 (ГАПО 182-5-293)» (pk 1328), ч. 2 — л. 184 шмуцтитул, лл. 184об–192об, 42 брака (январь 5, февраль 5, май 2,
# июль 1, сентябрь 1, октябрь 2, ноябрь 24), прочитана целиком 26.10.2026; импорта не было. Браков №6–10 в наборе нет (между
# лл. 184об и 185об). С л. 186об листы переплетены вперемешку: левая и правая страницы разворота часто из разных частей.
# Венчали свящ. Александр Васильев Писарев и Павел Богословский.
kirillovo_marriages_1905 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "293",
    "Кириллово",
    "Казанская церковь",
    1905,
    *marriage_month(Month.JANUARY,
                    # поручитель по жениху — Андрей Николаевич «Кистеневъ» (= «Малахаевъ»)
                    marriage(4, 18,
                             groom=person("Василій", "Ивановъ", "Вавилкинъ"), groom_marriage_num=1, groom_age=21,
                             bride=person("Дарія", "Григорьева", "Царева"), bride_marriage_num=1, bride_age=26,
                             witness1=person("Андрей", "Николаевъ", "Кистеневъ", side=Side.GROOM, comment="он же: Андрей Николаевич Малахаев"),
                             witness2=person("Василій", "Платоновъ", "Бубенчиковъ", side=Side.GROOM),
                             witness3=person("Илья", "Матвѣевъ", "Гуськовъ", side=Side.BRIDE),
                             witness4=person("Иванъ", "Ивановъ", "Бубенчиковъ", side=Side.BRIDE),
                             page="184об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # невеста — Мария Васильевна «Сѣркова», дочь Василия Сергеевича Ладыгина; поручитель — её дядя Андрей Сергеевич
                    marriage(20, 2,
                             groom=person("Иванъ", "Семеновъ", "Лукьяновъ", status=SOLDIER, comment="«запасный рядовой»"),
                             groom_marriage_num=1, groom_age=27,
                             bride=person("Марія", "Васильева", "Сѣркова", comment="она же: Мария Васильевна Ладыгина"),
                             bride_marriage_num=1, bride_age=20,
                             witness1=person("Ѳеодоръ", "Кузьминъ", "Галичниковъ", side=Side.GROOM, comment="отчество читается неуверенно («Кузьмичъ»?)"),
                             witness2=person("Гавріилъ", "Яковлевъ", "Лукьяновъ", side=Side.GROOM),
                             witness3=person("Андрей", "Сергѣевъ", "Сѣрковъ", side=Side.BRIDE, comment="он же: Андрей Сергеевич Ладыгин"),
                             witness4=person("Михаилъ", "Кирилловъ", "Галичниковъ", side=Side.BRIDE, comment="отчество читается неуверенно"),
                             page="188об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
