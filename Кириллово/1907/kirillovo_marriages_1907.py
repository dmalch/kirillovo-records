from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-298, альбом
# Photos «1907 (ГАПО 182-5-298)» (pk 1335), ч. 2 — л. 114 шмуцтитул, лл. 114об–121об, 32 брака (ноябрь 22), прочитана
# целиком 26.10.2026; импорта не было. Графы возраста невесты в бланке нет; бледные чернила. Венчали свящ. Александр
# Васильев Писарев и Павел Богословский.
kirillovo_marriages_1907 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "298",
    "Кириллово",
    "Казанская церковь",
    1907,
    *marriage_month(Month.NOVEMBER,
                    # поручители — Василий и Михаил Мальчиковы (без отчеств)
                    marriage(17, 2,
                             groom=person("Матвѣй", "Ивановъ", "Курановъ"), groom_marriage_num=1, groom_age=20,
                             bride=person("Ирина", "Тимоѳеева", "Шевлягина", comment="фамилия читается неуверенно"), bride_marriage_num=1,
                             witness1=person("Матвѣй", "Архиповъ", "Пармоновъ", side=Side.GROOM, comment="фамилия читается неуверенно"),
                             witness2=person("Василій", None, "Мальчиковъ", side=Side.GROOM, comment="отчество не записано"),
                             witness3=person("Алексѣй", "Архиповъ", "Пармоновъ", side=Side.BRIDE),
                             witness4=person("Михаилъ", None, "Мальчиковъ", side=Side.BRIDE, comment="отчество не записано"),
                             page="118об",
                             reviewed=False),
                    # Владимир Дмитриевич «Кистеневъ» (= «Стрекалинъ», сын Дмитрия Андреевича «Малахаева»)
                    marriage(19, 5,
                             groom=person("Владиміръ", "Димитріевъ", "Кистеневъ", comment="он же: «Стрекалинъ» 1904; сын Дмитрия Андреевича Малахаева?"),
                             groom_marriage_num=1, groom_age=18,
                             bride=person("Александра", "Аѳанасьева", "Лисова", comment="фамилия читается неуверенно"), bride_marriage_num=1,
                             witness1=person("Андрей", "Николаевъ", "Кистеневъ", side=Side.GROOM),
                             witness2=person("Иванъ", "Николаевъ", "Кистеневъ", side=Side.GROOM, comment="читается неуверенно"),
                             witness3=person("Гавріилъ", None, "Сафоновъ", side=Side.BRIDE, comment="отчество не дочитано"),
                             witness4=person("Яковъ", None, "Лисицынъ", side=Side.BRIDE, comment="отчество не записано, фамилия неуверенно"),
                             page="119об",
                             reviewed=False),
                    # поручитель по невесте — Василий Семенович? Мальчиков
                    marriage(28, 9,
                             groom=person("Владиміръ", "Андреевъ", "Семакинъ"), groom_marriage_num=1, groom_age=18,
                             bride=person("Анна", "Владимірова", "Пилатина", comment="фамилия читается неуверенно"), bride_marriage_num=1,
                             witness1=person("Матвѣй", "Кирилловъ", "Семакинъ", side=Side.GROOM, comment="отчество читается неуверенно"),
                             witness2=person("Леонтій", "Ивановъ", "Семакинъ", side=Side.GROOM),
                             witness3=person("Василій", "Семеновъ", "Мальчиковъ", side=Side.BRIDE, comment="отчество читается неуверенно («Се…овъ»)"),
                             witness4=person("Мамонтъ", "Трофимовъ", "Чиликинъ", side=Side.BRIDE),
                             page="120об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
