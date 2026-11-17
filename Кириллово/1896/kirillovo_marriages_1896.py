from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-306, альбом
# Photos «1896 (ГАПО 182-5-306)» (pk 1207), ч. 2 — лл. 191об–198об, 19 браков (январь 2, июль 1, август 1, сентябрь 1,
# ноябрь 14); л. 191 — шмуцтитул; прочитана целиком 25.10.2026; импорта не было. Книга пишет «государственный
# крестьянинъ». Жених и невеста — на левой странице, поручители — на правой. Венчали свящ. Александр Васильев Писарев и
# Василий Георгиевич Кутин. 10.11.1896 (№10) Селиверст Яковлевич Миронов венчался с Надеждой Ивановной Стюхиной (19) —
# чья она дочь, не установлено; не выписан.
kirillovo_marriages_1896 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "306",
    "Кириллово",
    "Казанская церковь",
    1896,
    *marriage_month(Month.JANUARY,
                    # поручитель по невесте — Федор Самсонович Янин
                    marriage(1, 15,
                             groom=person("Александръ", "Ивановъ", "Липатовъ"), groom_marriage_num=1, groom_age=19,
                             bride=person("Евдокія", "Никитина", "Позднякова"), bride_marriage_num=1, bride_age=21,
                             witness1=person("Семенъ", "Ивановъ", "Красиковъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Иванъ", "Исидоровъ", None, side=Side.GROOM, comment="фамилия не записана"),
                             witness3=person("Петръ", "Павловъ", "Онтиковъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Ѳеодоръ", "Самсоновъ", "Янинъ", side=Side.BRIDE),
                             page="191об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # поручитель по невесте — Герасим Яковлевич Мальчиков; жених — восприемник импортной рожд. ж. №68
                    # (8.10.1896, дочь Василия Степановича Мальчикова)
                    marriage(13, 6,
                             groom=person("Даніилъ", "Никитинъ", "Фетисовъ", status=SOLDIER, comment="«солдатъ 3-й роты осаднаго артиллерійскаго въ г. Кіевѣ баталіона»"),
                             groom_marriage_num=1, groom_age=25,
                             bride=person("Марія", "Михайлова", "Гамзонина", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=21,
                             witness1=person("Петръ", "Никитинъ", "Фетисовъ", side=Side.GROOM),
                             witness2=person("Петръ", "Алексѣевъ", "Назаровъ", side=Side.GROOM),
                             witness3=person("Стефанъ", "Тимоѳеевъ", "Куринъ", side=Side.BRIDE),
                             witness4=person("Герасимъ", "Яковлевъ", "Мальчиковъ", side=Side.BRIDE),
                             page="196об",
                             reviewed=False),
                    # Павел Прокопьевич Мальчиков («Юлинъ»); поручитель по жениху — Михаил Васильевич «Юлинъ»
                    marriage(14, 8,
                             groom=person("Павелъ", "Прокопіевъ", "Юлинъ", comment="= Павел Прокопьевич Мальчиков"),
                             groom_marriage_num=1, groom_age=18,
                             bride=person("Акилина", "Ефремова", "Пялкина"), bride_marriage_num=1, bride_age=19,
                             witness1=person("Михаилъ", "Васильевъ", "Юлинъ", side=Side.GROOM, comment="= Михаил Васильевич Мальчиков"),
                             witness2=person("Василій", "Алексѣевъ", "Кочегинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness3=person("Алексѣй", "Прокофьевъ", "Пялкинъ", side=Side.BRIDE),
                             witness4=person("Ѳеодоръ", None, None, side=Side.BRIDE, comment="отчество и фамилия ушли под край листа"),
                             page="196об",
                             reviewed=False),
                    # Илья Петрович Мальчиков (поручитель 1893 №22); поручитель по невесте — Петр Мальчиков (отчество не
                    # записано)
                    marriage(19, 17,
                             groom=person("Илія", "Петровъ", "Мальчиковъ"), groom_marriage_num=1, groom_age=22,
                             bride=person("Ѳеврония", "Андреева", "Левина"), bride_marriage_num=1, bride_age=17,
                             witness1=person("Матвѣй", "Елисѣевъ", "Лисковъ", side=Side.GROOM),
                             witness2=person("Иванъ", "Ѳеодоровъ", "Афонинъ", side=Side.GROOM),
                             witness3=person("Павелъ", "Никитинъ", "Афонинъ", side=Side.BRIDE),
                             witness4=person("Петръ", None, "Мальчиковъ", side=Side.BRIDE, comment="отчество не записано"),
                             page="198об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
