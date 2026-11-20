from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-302, альбом
# Photos «1910 (ГАПО 182-5-302)» (pk 1199), ч. 2 — л. 115 шмуцтитул, лл. 115об–121об, 24 брака, прочитана целиком
# 26.10.2026; импорта не было. Возраст невест у корешка не виден.
kirillovo_marriages_1910 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "302",
    "Кириллово",
    "Казанская церковь",
    1910,
    *marriage_month(Month.JANUARY,
                    # поручитель по невесте — Николай Максимович «Мальчиков» (Максимович «Дунаев»?)
                    marriage(3, 20,
                             groom=person("Никита", "Ермолаевъ", "Сапуновъ", comment="фамилия читается неуверенно"),
                             groom_marriage_num=1, groom_age=19,
                             bride=person("Елена", "Михайлова", "Сипунова", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1,
                             witness1=person("Герасимъ", "Стефановъ", "Сапуновъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Тимоѳей", None, side=Side.GROOM, comment="отчество и фамилия не дочитаны («Бо…овъ»)"),
                             witness3=person("Иванъ", "Никифоровъ", "Степанчиковъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Николай", "Максимовъ", "Мальчиковъ", side=Side.BRIDE, comment="он же: Николай Максимович «Дунаев» (восприемник 1910 м. №20)?"),
                             page="115об",
                             reviewed=False),
                    # жених — Иоанн Иоаннович Мальчиков; поручитель — Василий Мальчиков
                    marriage(4, 22,
                             groom=person("Іоаннъ", "Іоанновъ", "Мальчиковъ"), groom_marriage_num=1, groom_age=18,
                             bride=person("Александра", "Семенова", "Лапшина", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1,
                             witness1=person("Григорій", "Никоновъ", "Шабановъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Василій", None, "Мальчиковъ", side=Side.GROOM, comment="отчество не записано"),
                             witness3=person("Василій", "Семеновъ", side=Side.BRIDE, comment="фамилия не дочитана («…нинъ»)"),
                             witness4=person("Филиппъ", "Герасимовъ", "Макаровъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             page="115об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # жених — Яков Васильевич Мальчиков; поручитель по невесте — Игнат Михайлович Мальчиков
                    marriage(13, 5,
                             groom=person("Іаковъ", "Васильевъ", "Мальчиковъ"), groom_marriage_num=1, groom_age=18,
                             bride=person("Параскева", "Иванова", "Егорова"), bride_marriage_num=1,
                             witness1=person("Макаръ", "Стефановъ", "Кисилевъ", side=Side.GROOM),
                             witness2=person("Ѳеодоръ", "Гавриловъ", "Даркинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness3=person("Игнатъ", "Михайловъ", "Мальчиковъ", side=Side.BRIDE),
                             witness4=person("Іаковъ", "Никитинъ", "Фетисовъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             page="118об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
