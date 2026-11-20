from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-293, альбом
# Photos «1905 (ГАПО 182-5-293)» (pk 1328), ч. 3 — лл. 180об–181об (январь–февраль) и лл. 194об–206об (февраль–1 сентября),
# прочитана целиком 26.10.2026; импорта не было. Переплёт перепутан: страница октября стоит справа на л. 182, декабря — слева
# на л. 187об; лл. 182а–183об — вложенные листы ч. 3 другого причта (свящ. Алексей Антонов). Остальных записей сентября —
# декабря в деле нет (оно заверено в 206 листов). Вся запись — на левой странице, причина — на правой. Погребали свящ.
# Александр Васильев Писарев и Павел Богословский.
kirillovo_deaths_1905 = death_records(
    "ГАПО",
    "182",
    "5",
    "293",
    "Кириллово",
    "Казанская церковь",
    1905,
    *death_month(Month.FEBRUARY,
                 # Матфей, сын Степана Васильевича Мальчикова («Юлинъ»), р. 4.08.1903 (рожд. 1903 м. №38)
                 death(9, Gender.MALE, 28, 1, b_month=Month.MARCH,
                       deceased=person("Матѳей", status=PEASANT_SON), age="1 лет 6 мес",
                       relatives=[relative(person("Стефанъ", "Васильевъ", "Юлинъ", comment="он же: Степан Васильевич Мальчиков"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="в подлиннике «1½ г.»; умер 28 февраля, погребён 1 марта",
                       page="194об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Кирилл, сын Стефана Михайловича Мальчикова, р. 30.05.1905 (рожд. м. №31)
                 death(24, Gender.MALE, 8, 9,
                       deceased=person("Кириллъ", status=PEASANT_SON), age="1 нед",
                       relatives=[relative(person("Стефанъ", "Михайловъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       page="199об",
                       reviewed=False),
                 # Параскева, дочь Василия Андреевича Ладыгина («Сѣрковъ») и Дарьи Николаевны Шиловой (брак 1902 №14)
                 death(23, Gender.FEMALE, 16, 17,
                       deceased=person("Параскева", status=PEASANT_DAUGHTER), age="8 мес",
                       relatives=[relative(person("Василій", "Андреевъ", "Ладыгинъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="возраст читается неуверенно",
                       page="200об",
                       reviewed=False),
                 # Иаков, сын Ивана Михайловича Богачева и Марии Андреевны «Юлиной», р. 1.05.1905 (рожд. м. №26)
                 death(30, Gender.MALE, 24, 25,
                       deceased=person("Іаковъ", status=PEASANT_SON), age="2 мес",
                       relatives=[relative(person("Иванъ", "Михайловъ", "Богачевъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       page="201об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Ирина, дочь Петра Никитича Мальчикова, р. 14.04.1905 (рожд. ж. №21)
                 death(28, Gender.FEMALE, 7, 7,
                       deceased=person("Ирина", status=PEASANT_DAUGHTER), age="3 мес",
                       relatives=[relative(person("Петръ", "Никитинъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       comment="возраст читается неуверенно",
                       page="202об",
                       reviewed=False),
                 ),
    *death_month(Month.DECEMBER,
                 # Татьяна, дочь Матвея Матвеевича Янина («Сырцовъ») и Александры Сергеевны Ладыгиной (брак 1887)
                 death(53, Gender.FEMALE, 11, 12,
                       deceased=person("Татіана", status=PEASANT_DAUGHTER), age=3,
                       relatives=[relative(person("Матвѣй", "Матвѣевъ", "Сырцовъ", comment="он же: Матвей Матвеевич Янин"), Relationship.FATHER)],
                       comment="страница стоит слева на л. 187об, среди браков; причина на своей правой странице не найдена",
                       page="187об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
