from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-298, альбом
# Photos «1908 (ГАПО 182-5-298)» (pk 1255), ч. 2 — л. 170 шмуцтитул, лл. 170об–177об, 33 брака, прочитана целиком
# 26.10.2026; импорта не было. Венчали свящ. Александр Васильев Писарев и Павел Богословский.
kirillovo_marriages_1908 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "298",
    "Кириллово",
    "Казанская церковь",
    1908,
    *marriage_month(Month.JUNE,
                    # поручитель по невесте — Николай Петрович Мальчиков
                    marriage(9, 13,
                             groom=person("Сергѣй", "Гавриловъ", "Чекмуринъ"), groom_marriage_num=1, groom_age=19,
                             bride=person("Мавра", "Никитина", comment="«села … Керенскаго уѣзда Пензенской губерніи»; село и фамилия не дочитаны"),
                             bride_marriage_num=1,
                             witness1=person("Тимоѳей", "Ефимовъ", "Исайкинъ", side=Side.GROOM),
                             witness2=person("Михаилъ", "Яковлевъ", "Лукьяновъ", side=Side.GROOM),
                             witness3=person("Александръ", "Тимоѳеевъ", "Исайкинъ", side=Side.BRIDE),
                             witness4=person("Николай", "Петровъ", "Мальчиковъ", side=Side.BRIDE),
                             page="172об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # Никифор Максимович «Дунаевъ» — Максимовичи «Дунаевы» = Мальчиковы
                    marriage(16, 3,
                             groom=person("Никифоръ", "Максимовъ", "Дунаевъ", comment="Максимовичи «Дунаевы» — Мальчиковы (см. рожд. ж. №109)"),
                             groom_marriage_num=2, groom_age=23,
                             bride=person("Александра", "Аѳанасьева", "Егорова"), bride_marriage_num=1, bride_age=18,
                             witness1=person("Ѳеодоръ", "Семеновъ", side=Side.GROOM, comment="фамилия не дочитана («Ма…ичевъ»)"),
                             witness2=person("Иванъ", "Ильинъ", side=Side.GROOM, comment="фамилия не дочитана"),
                             witness3=person("Сергѣй", "Спиридоновъ", side=Side.BRIDE, comment="фамилия не дочитана"),
                             witness4=person("Петръ", "Павловъ", "Сафроновъ", side=Side.BRIDE),
                             page="174об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
