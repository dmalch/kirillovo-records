from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-303, альбом
# Photos «1898 (ГАПО 182-5-303)» (pk 1230), ч. 2 — лл. 104об–112об, 29 браков, прочитана целиком 25.10.2026; л. 103 —
# шмуцтитул; импорта не было. Книга пишет «государственный крестьянинъ». Жених и невеста — на левой странице, поручители —
# на правой. Венчали свящ. Александр Васильев Писарев и Павел Богословский. Между лл. 112об и 113 подшита копия (1919 г.)
# записи о браке №15 Красно-Дубравской церкви от 22.11.1898 (Григорий Иванович Кожинов × Мария Тимофеевна Каверина;
# поручитель по невесте Герасим Яковлевич «Поздняковъ») — запись чужого прихода, не выписана.
kirillovo_marriages_1898 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "303",
    "Кириллово",
    "Казанская церковь",
    1898,
    *marriage_month(Month.JANUARY,
                    # невеста — Татьяна Федоровна Мальчикова (восприемница 1897 рожд. ж. №19 и №22 штата Кутина); чья дочь —
                    # не установлено
                    marriage(1, 11,
                             groom=person("Ѳеодоръ", "Денисовъ", "Паршинъ"), groom_marriage_num=1, groom_age="18 лет 6 мес",
                             bride=person("Татіана", "Ѳеодорова", "Мальчикова"), bride_marriage_num=1, bride_age=16,
                             witness1=person("Ѳеодоръ", "Семеновъ", "Онтиковъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Михаилъ", "Яковлевъ", "Паршинъ", side=Side.GROOM),
                             witness3=person("Аѳанасій", "Степановъ", "Сигачевъ", side=Side.BRIDE),
                             witness4=person("Трифонъ", None, "Калининъ", side=Side.BRIDE),
                             comment="возраст жениха «18½»",
                             page="104об",
                             reviewed=False),
                    ),
    *marriage_month(Month.FEBRUARY,
                    # поручитель по невесте — Петр Федорович «Сырцовъ» (Янин?)
                    marriage(5, 4,
                             groom=person("Ѳеодоръ", "Тимоѳеевъ", "Шевлягинъ"), groom_marriage_num=1, groom_age=26,
                             bride=person("Іустинія", "Иванова", "Бочкова"), bride_marriage_num=1, bride_age=18,
                             witness1=person("Ѳеодоръ", "Ивановъ", "Шевлягинъ", side=Side.GROOM),
                             witness2=person("Степанъ", "Леонтьевъ", "Трошинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness3=person("Петръ", "Ѳеодоровъ", "Сырцовъ", side=Side.BRIDE),
                             witness4=person("Иванъ", "Тимоѳеевъ", "Шевлягинъ", side=Side.BRIDE),
                             page="105об",
                             reviewed=False),
                    ),
    *marriage_month(Month.MAY,
                    # поручитель по жениху — Петр Ильич Мальчиков
                    marriage(7, 11,
                             groom=person("Василій", "Ѳеодоровъ", "Шуковъ", status=SOLDIER, comment="«запасный рядовой»; фамилия читается неуверенно"),
                             groom_marriage_num=2, groom_age=35,
                             bride=person("Елена", "Семенова", "Утина", residence="Ширингуши", comment="«государственная крестьянка села Ширингуши»; фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=20,
                             witness1=person("Гавріилъ", "Яковлевъ", "Чекмуринъ", side=Side.GROOM),
                             witness2=person("Петръ", "Ильинъ", "Мальчиковъ", side=Side.GROOM, comment="в подлиннике «Ильичъ»"),
                             witness3=person("Аѳанасій", "Степановъ", "Сигачевъ", side=Side.BRIDE),
                             witness4=person("Николай", "Григорьевъ", "Брунчуковъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             page="106об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
