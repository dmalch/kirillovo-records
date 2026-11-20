from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-307, альбом
# Photos «1901 (ГАПО 182-5-307)» (pk 1185), ч. 2 — лл. 157об–163об, 23 брака (январь 5, апрель 2, июль 1, август 1,
# сентябрь 1, октябрь 1, ноябрь 12), прочитана целиком 25.10.2026; л. 156об — пустой, л. 157 — шмуцтитул; импорта не было.
# Жених и невеста — на левой странице, поручители — на правой. Венчали свящ. Александр Васильев Писарев и Павел
# Богословский.
kirillovo_marriages_1901 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "307",
    "Кириллово",
    "Казанская церковь",
    1901,
    *marriage_month(Month.AUGUST,
                    # невеста — Матрона Семеновна, вдова Гавриила Васильевича Мальчикова («Юлина», ум. 29.12.1900)
                    marriage(9, 27,
                             groom=person("Ѳеодоръ", "Тимоѳеевъ", "Шерденинъ", status=SOLDIER, comment="«запасный рядовой»; фамилия читается неуверенно"),
                             groom_marriage_num=2, groom_age=31,
                             bride=person("Матрона", "Семенова", "Юлина", comment="она же: вдова Гавриила Васильевича Мальчикова"),
                             bride_marriage_num=2, bride_age=33,
                             witness1=person("Михаилъ", "Васильевъ", "Юлинъ", side=Side.GROOM, comment="он же: Михаил Васильевич Мальчиков"),
                             witness2=person("Михаилъ", "Тимоѳеевъ", "Шевлягинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness3=person("Андрей", "Сергѣевъ", "Сѣрковъ", side=Side.BRIDE, comment="он же: Андрей Сергеевич Ладыгин"),
                             witness4=person("Леонтій", "Антоновъ", "Абашевъ", side=Side.BRIDE),
                             page="159об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # Василий Андреевич Ладыгин («Сѣрковъ») и Ирина Матвеевна Янина («Сырцова»); Ирина умерла 24.11.1901 (смерть ж.
                    # №48)
                    marriage(12, 2,
                             groom=person("Василій", "Андреевъ", "Сѣрковъ", comment="он же: Василий Андреевич Ладыгин"),
                             groom_marriage_num=1, groom_age=18,
                             bride=person("Ирина", "Матвѣева", "Сырцова"), bride_marriage_num=1, bride_age=21,
                             witness1=person("Иванъ", "Акимовъ", "Жариковъ", side=Side.GROOM),
                             witness2=person("Василій", "Сергѣевъ", "Сѣрковъ", side=Side.GROOM, comment="он же: Василий Сергеевич Ладыгин"),
                             witness3=person("Илья", "Леонтьевъ", "Станкинъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Петръ", "Павловъ", "Шарикинъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             page="160об",
                             reviewed=False),
                    # поручитель по невесте — Василий Степанович Мальчиков
                    marriage(18, 9,
                             groom=person("Андрей", "Фалалеевъ", "Сенинъ", comment="отчество и фамилия читаются неуверенно"),
                             groom_marriage_num=1, groom_age=19,
                             bride=person("Наталія", "Сергѣева", "Курасова", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=19,
                             witness1=person("Илья", "Леонтьевъ", "Станкинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Лаврентій", "Андреевъ", "Чекмуринъ", side=Side.GROOM),
                             witness3=person("Кириллъ", "Ивановъ", "Курановъ", side=Side.BRIDE),
                             witness4=person("Василій", "Стефановъ", "Мальчиковъ", side=Side.BRIDE),
                             page="161об",
                             reviewed=False),
                    # поручитель по невесте — Илья Петрович Мальчиков
                    marriage(19, 9,
                             groom=person("Михаилъ", "Прокопіевъ", "Егоровъ"), groom_marriage_num=1, groom_age=22,
                             bride=person("Татіана", "Гаврилова", "Сафронова"), bride_marriage_num=1, bride_age=20,
                             witness1=person("Григорій", "Козминъ", "Кочеткинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Семенъ", "Ивановъ", "Липатовъ", side=Side.GROOM),
                             witness3=person("Матвѣй", "Васильевъ", "Бровкинъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Илья", "Петровъ", "Мальчиковъ", side=Side.BRIDE),
                             page="162об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
