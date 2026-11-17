from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-305, альбом
# Photos «1889 (ГАПО 182-5-305)» (pk 1268), ч. 2 — лл. 237об–242об, 16 браков (январь 1, февраль 4, апрель 3, май 2,
# ноябрь 6); л. 235об — пустой бланк ч. 1, л. 237 — шмуцтитул, л. 243об — пустой; прочитана целиком 24.10.2026; импорта
# не было. Жених и невеста — на левой странице, поручители — на правой. Венчал свящ. Александр Васильев Писарев.
kirillovo_marriages_1889 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "305",
    "Кириллово",
    "Казанская церковь",
    1889,
    *marriage_month(Month.FEBRUARY,
                    # Иван Андреевич Мальчиков («Юлинъ»), сын Андрея Григорьевича; поручитель по жениху — Михаил Васильевич
                    # «Юлинъ»
                    marriage(2, 3,
                             groom=person("Іоаннъ", "Андреевъ", "Юлинъ", comment="= Иван Андреевич Мальчиков"),
                             groom_marriage_num=1, groom_age="17 лет 11 мес",
                             bride=person("Анна", "Иванова", "Каргова", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=19,
                             witness1=person("Михаилъ", "Васильевъ", "Юлинъ", side=Side.GROOM, comment="= Михаил Васильевич Мальчиков"),
                             witness2=person("Иванъ", "Васильевъ", "Решетовъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness3=person("Николай", "Ильинъ", "Ковальковъ", side=Side.BRIDE),
                             witness4=person("Василій", None, "Бѣловъ", side=Side.BRIDE, comment="фамилия у дыры листа"),
                             priest=person("Александръ", "Васильевъ", "Писаревъ", status=HIEREUS),
                             page="237об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
