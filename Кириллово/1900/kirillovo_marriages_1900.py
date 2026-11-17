from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-307, альбом
# Photos «1900 (ГАПО 182-5-307)» (pk 1196), ч. 2 — лл. 76об–87об, 37 браков (январь 7, февраль 8, апрель 1, октябрь 4,
# ноябрь 17), прочитана целиком 25.10.2026; л. 75об — пустой, л. 76 — шмуцтитул; импорта не было. Жених и невеста — на
# левой странице, поручители — на правой. Венчали свящ. Александр Васильев Писарев и Павел Богословский.
kirillovo_marriages_1900 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "307",
    "Кириллово",
    "Казанская церковь",
    1900,
    *marriage_month(Month.OCTOBER,
                    # поручитель по невесте — Клим Мальчиков (отчество не записано; отец Федора и Ивана Климовичей?)
                    marriage(18, 25,
                             groom=person("Яковъ", "Григорьевъ", "Бурдаевъ", comment="«по пріемному отцу Бурдаевъ»"),
                             groom_marriage_num=1, groom_age=22,
                             bride=person("Марія", "Егорова", "Бурдаева"), bride_marriage_num=2, bride_age=31,
                             witness1=person("Лука", "Никитинъ", "Сафроновъ", side=Side.GROOM, comment="отчество читается неуверенно"),
                             witness2=person("Никита", "Моисеевъ", "Бурдаевъ", side=Side.GROOM),
                             witness3=person("Климъ", None, "Мальчиковъ", side=Side.BRIDE, comment="отчество не записано"),
                             witness4=person("Стефанъ", "Моисеевъ", "Бурдаевъ", side=Side.BRIDE),
                             page="81об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # поручитель по жениху — Степан Степанович Мальчиков
                    marriage(36, 8,
                             groom=person("Кириллъ", "Ивановъ", "Курановъ"), groom_marriage_num=1, groom_age=20,
                             bride=person("Ксенія", "Лаврентіева", "Ордышкина", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=17,
                             witness1=person("Василій", "Ѳеодоровъ", "Шуковъ", status=SOLDIER, side=Side.GROOM, comment="«запасный рядовой»; фамилия читается неуверенно"),
                             witness2=person("Стефанъ", "Стефановъ", "Мальчиковъ", side=Side.GROOM),
                             witness3=person("Иванъ", "Герасимовъ", "Кадѣевъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Ѳеодоръ", "Гавриловъ", "Егоровъ", side=Side.BRIDE),
                             page="87об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
