from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-293, альбом
# Photos «1904 (ГАПО 182-5-293)» (pk 1389), ч. 2 — лл. 118об–121об, 19 браков (январь 4, ноябрь 15), прочитана целиком
# 26.10.2026; л. 117об — пустой, л. 118 — шмуцтитул, л. 122об — пустой; импорта не было. Жених и невеста — на левой
# странице, поручители — на правой. Венчали свящ. Александр Васильев Писарев и Павел Богословский.
kirillovo_marriages_1904 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "293",
    "Кириллово",
    "Казанская церковь",
    1904,
    *marriage_month(Month.NOVEMBER,
                    # поручитель по невесте — Иван Михайлович Мальчиков?
                    marriage(7, 3,
                             groom=person("Иванъ", "Прокопіевъ", "Кистенинъ", comment="фамилия читается неуверенно"),
                             groom_marriage_num=1, groom_age=19,
                             bride=person("Александра", "Спиридонова", "Пчелкина", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=21,
                             witness1=person("Гавріилъ", "Стефановъ", "Филипповъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Иванъ", "Филипповъ", "Калинкинъ", side=Side.GROOM),
                             witness3=person("Иванъ", "Михайловъ", "Мальчиковъ", side=Side.BRIDE, comment="фамилия читается неуверенно («Малычиковъ»?)"),
                             witness4=person("Павелъ", None, "Зайцевъ", side=Side.BRIDE, comment="отчество не записано"),
                             page="119об",
                             reviewed=False),
                    # Федор Герасимович Мальчиков, сын Герасима Яковлевича
                    marriage(16, 10,
                             groom=person("Ѳеодоръ", "Герасимовъ", "Мальчиковъ"), groom_marriage_num=1, groom_age=19,
                             bride=person("Мавра", "Иванова", "Филинина", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=18,
                             witness1=person("Иванъ", "Антоновъ", "Исаринъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Яковъ", "Косминъ", "Чичеровъ", side=Side.GROOM),
                             witness3=person("Никифоръ", "Никитинъ", "Жильцовъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Димитрій", "Ивановъ", "Пурусевъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             page="121об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
