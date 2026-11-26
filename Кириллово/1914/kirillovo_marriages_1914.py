from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-574, альбом
# Photos «1914 (ГАПО 182-5-574)» (pk 1182), ч. 2 — л. 130 шмуцтитул, лл. 130об–138об, 28 браков, прочитана целиком
# 26.10.2026; импорта не было.
kirillovo_marriages_1914 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "574",
    "Кириллово",
    "Казанская церковь",
    1914,
    *marriage_month(Month.JANUARY,
                    # жених — Алексей Михайлович «Юлинъ» (сын Михаила Васильевича)
                    marriage(7, 29,
                             groom=person("Алексѣй", "Михайловъ", "Юлинъ"), groom_marriage_num=1, groom_age=21,
                             bride=person("Пелагія", "Герасимова", "Гусева", comment="фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=16,
                             witness1=person("Стефанъ", "Андреевъ", "Калининъ", side=Side.GROOM),
                             witness2=person("Іона", "Игнатовъ", "Мироновъ", side=Side.GROOM),
                             witness3=person("Егоръ", "Тимоѳеевъ", "Крысановъ", side=Side.BRIDE),
                             witness4=person("Михаилъ", None, "Кузинъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             page="132об",
                             reviewed=False),
                    ),
    *marriage_month(Month.APRIL,
                    # невеста — Наталья Васильевна Мальчикова
                    marriage(12, 18,
                             groom=person("Евфимій", "Ивановъ", "Молотковъ"), groom_marriage_num=1, groom_age=26,
                             bride=person("Наталья", "Васильева", "Мальчикова"), bride_marriage_num=1, bride_age=21,
                             witness1=person("Стефанъ", "Ивановъ", "Кубышкинъ", side=Side.GROOM),
                             witness2=person("Петръ", "Ивановъ", "Молотковъ", side=Side.GROOM),
                             witness3=person("Стефанъ", "Андреевъ", "Лакутовъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             witness4=person("Василій", "Герасимовъ", "Кадіевъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             page="134об",
                             reviewed=False),
                    ),
    *marriage_month(Month.NOVEMBER,
                    # невеста — Акилина Андреевна Мальчикова
                    marriage(28, 12,
                             groom=person("Иванъ", "Алексѣевъ", "Калининъ"), groom_marriage_num=1, groom_age=21,
                             bride=person("Акилина", "Андреева", "Мальчикова"), bride_marriage_num=1, bride_age=17,
                             witness1=person("Павелъ", "Васильевъ", "Кавикинъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Александръ", None, "Дешинъ", side=Side.GROOM, comment="«помощникъ писаря»; фамилия читается неуверенно"),
                             witness3=person("Іона", "Игнатовъ", "Мироновъ", side=Side.BRIDE),
                             witness4=person("Александръ", "Павловъ", "Кавикинъ", side=Side.BRIDE, comment="фамилия читается неуверенно"),
                             page="138об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
    # --- Автоматически распознано (Batch OCR ЗАГС, reviewed=False) ---
    *marriage_month(Month.FEBRUARY,
                    marriage(None, 2,
                             groom=person(None, comment="Кирсанов Михаил Павлович"), groom_marriage_num=1,
                             bride=person(None, comment="Солдатова Анна Михайловна"), bride_marriage_num=1,
                             case="д.14", page="л.81", reviewed=False),
                 ),
)
