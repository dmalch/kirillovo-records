from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-303, альбом
# Photos «1897 (ГАПО 182-5-303)» (pk 1210), ч. 2 — лл. 33об–45об, прочитана целиком 25.10.2026; импорта не было. Счёт браков
# общий у трёх священников (Писарев, Кутин, Павел Богословский). Книга пишет «государственный крестьянинъ». Жених и невеста
# — на левой странице, поручители — на правой. Левой страницы л. 33об (январские браки штата Писарева) на своём месте нет:
# её оборванный обрывок вшит в ч. 3 (кадр «л.62об.-63») — №2 (12.01, Григорий Яковлевич Егоров × Пелагия Ивановна Верхова),
# №3 (19.01, Евдоким Иванович Бурлин × Феодора Федоровна Б…) и №5 (ниже). Их поручители — на л. 34: у №3 по жениху
# Василий Степанович Мальчиков (Бурлин — «Мальчиковъ тожъ»? не установлено; не выписан). 5.11.1897 (№23) вдовцом венчался
# Василий Васильевич Аболмасов (жена Мария Васильевна, брак №6, ум. 13.08.1897).
kirillovo_marriages_1897 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "303",
    "Кириллово",
    "Казанская церковь",
    1897,
    *marriage_month(Month.JANUARY,
                    # невеста — «…ія Маль[чикова]» (обрывок); поручитель по невесте — Михаил Константинович Мальчиков. Левая
                    # страница — обрывок, вшитый на л. 62об; поручители — на л. 34 (третья группа, по жениху Абрамцев)
                    marriage(5, 22,
                             groom=person("Михаилъ", "Ѳеодоровъ", "Абрамцевъ"), groom_marriage_num=1, groom_age=19,
                             bride=person("?", None, "Мальчикова", comment="обрывок: «…ія Маль…»; имя, отчество и возраст оборваны"),
                             bride_marriage_num=1,
                             witness1=person("Иванъ", "Евфимовъ", "Абрамцевъ", side=Side.GROOM),
                             witness2=person("Димитрій", "Васильевъ", "Маргуновъ", side=Side.GROOM),
                             witness3=person("Михаилъ", "Константиновъ", "Мальчиковъ", side=Side.BRIDE),
                             witness4=person("Гавріилъ", "Васильевъ", "Киселевъ", side=Side.BRIDE),
                             comment="обрывок левой страницы вшит на л. 62об; поручители — на л. 34",
                             page="62об",
                             reviewed=False),
                    # поручитель по невесте — Андрей Сергеевич Ладыгин (сын Пелагии Семеновны Мальчиковой)
                    marriage(6, 31,
                             groom=person("Василій", "Васильевъ", "Абдулмясовъ", comment="= Аболмасов"), groom_marriage_num=1, groom_age=20,
                             bride=person("Марія", "Васильева", "Марычова", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=19,
                             witness1=person("Андрей", "Ивановъ", "Щетининъ", side=Side.GROOM),
                             witness2=person("Иванъ", "Петровъ", "Ванюковъ", side=Side.GROOM, comment="крестьянин другого села; фамилия читается неуверенно"),
                             witness3=person("Андрей", "Сергѣевъ", "Ладыгинъ", side=Side.BRIDE),
                             witness4=person("Иванъ", "Яковлевъ", "Аболмасовъ", side=Side.BRIDE),
                             page="34об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # поручитель по жениху — Василий Степанович Мальчиков
                    marriage(21, 3,
                             groom=person("Андрей", "Егоровъ", "Дыркинъ"), groom_marriage_num=1, groom_age=22,
                             bride=person("Анна", "Петрова", "Спиряева"), bride_marriage_num=1, bride_age=21,
                             witness1=person("Василій", "Степановъ", "Мальчиковъ", side=Side.GROOM),
                             witness2=person("Михаилъ", "Ивановъ", "Бѣсовъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness3=person("Андрей", "Ивановъ", "Дыркинъ", side=Side.BRIDE),
                             witness4=person("Иванъ", "Даниловъ", "Барановъ", side=Side.BRIDE),
                             page="36об",
                             reviewed=False),
                    # поручитель по невесте — Федор Климович Мальчиков
                    marriage(36, 10,
                             groom=person("Макаръ", "Кирилловъ", "Курковъ", comment="фамилия читается неуверенно"),
                             groom_marriage_num=1, groom_age=19,
                             bride=person("Александра", "Нестерова"), bride_marriage_num=1, bride_age=20,
                             witness1=person("Иванъ", None, "Садковъ", side=Side.GROOM, comment="отчество и фамилия читаются неуверенно"),
                             witness2=person("Ѳеодоръ", "Семеновъ", "Онтиковъ", side=Side.GROOM),
                             witness3=person("Ѳеодоръ", "Климовъ", "Мальчиковъ", side=Side.BRIDE),
                             witness4=person("Павелъ", "Павловъ", "Макаревъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             page="45об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
