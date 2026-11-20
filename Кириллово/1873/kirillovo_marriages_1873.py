from verso.ru.dsl import (Month, RecordDefaults, Side, marriage, marriage_month, marriage_records,
                          person)
from verso.ru.dsl.statuses import (HIEREUS, KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MAIDEN,
                                   KAZENNYJ_PEASANT_MALE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. ГАПО 182-5-732, альбом Photos
# «1873 (ГАПО 182-5-732)» (pk 1270), ч. 2 — лл. 148об–155об, прочитана целиком 19.10.2026. Книга ведётся по двум
# штатам, у каждого свой счёт с № 1: штат свящ. Василия Иоаннова Ремезова — лл. 148об–151об, № 1–20; штат иерея
# Павла Феофанова Кроткова — лл. 152об–155об, № 1–12. Жених и невеста — на левой странице, поручители — на правой.
kirillovo_marriages_1873 = marriage_records(
    "ГАПО",
    "182",
    "5",
    "732",
    "Кириллово",
    "Казанская церковь",
    1873,
    *marriage_month(Month.NOVEMBER,
                    # штат Ремезова. Петр Михайлович Янин («Сырдцевъ»), сын Михаила Андреяновича
                    marriage(15, 9,
                             groom=person("Петръ", "Михайловъ", "Сырдцевъ", comment="«Сырдцевъ» — так в подлиннике; он же: Петр Михайлович Янин"),
                             groom_marriage_num=1, groom_age=19,
                             bride=person("Анна", "Михайлова", "Киселева", residence="Кирилловские Выселки", comment="в подлиннике «Кисилева»?; фамилия читается неуверенно"),
                             bride_marriage_num=1, bride_age=20,
                             witness1=person("Ѳедоръ", "Ивановъ", "Шевлягинъ", side=Side.GROOM),
                             witness2=person("Захаръ", "Фроловъ", "Воиковъ", side=Side.GROOM),
                             witness3=person("Казьма", "Герасимовъ", "Киселевъ", side=Side.BRIDE, residence="Кирилловские Выселки"),
                             witness4=person("Иванъ", "Никифоровъ", "Фильминъ", side=Side.BRIDE, residence="Кирилловские Выселки", comment="фамилия читается неуверенно"),
                             priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                             page="151об",
                             reviewed=False),
                    # штат Кроткова. Федор Самсонович Янин (в 1879 — отец с женой Февронией Дементьевной)
                    marriage(11, 9,
                             groom=person("Ѳеодоръ", "Самсоновъ", "Янинъ"), groom_marriage_num=1, groom_age="17 л 6 мес",
                             bride=person("Ѳевронія", "Дементіева", "Миронова", residence="Кирилловские Выселки", comment="«крестьянская дочь»"),
                             bride_marriage_num=1, bride_age=19,
                             witness1=person("Акимъ", "Филатовъ", "Жариковъ", side=Side.GROOM, comment="так в подлиннике; он же: Аким Филимонович Жариков?"),
                             witness2=person("Савостьянъ", "Ивановъ", side=Side.GROOM, comment="имя читается неуверенно; фамилии нет"),
                             witness3=person("Иванъ", "Пахомовъ", "Власковъ", side=Side.BRIDE, comment="отчество читается неуверенно"),
                             witness4=person("Игнатъ", None, "Стукановъ", side=Side.BRIDE, comment="отчества нет"),
                             priest=person("Павелъ", "Ѳеофановъ", "Кротковъ", status=HIEREUS),
                             comment="штат иерея Кроткова — не путать с браком № 11 штата Ремезова",
                             page="154об",
                             reviewed=False),
                    ),
    defaults=RecordDefaults(residence="Кириллово", status_male=KAZENNYJ_PEASANT_MALE, status_female=KAZENNYJ_PEASANT_FEMALE,
                            status_bride=KAZENNYJ_PEASANT_MAIDEN),
)
