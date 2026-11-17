from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям, и дети их замужних
# дочерей). ГАПО 182-5-574, альбом Photos «1914 (ГАПО 182-5-574)» (pk 1182), ч. 3 — л. 141об пуст, л. 142 шмуцтитул, лл.
# 142об–171об (м. №1–72, ж. №1–69), прочитана целиком 26.10.2026; импорта не было. Погребали свящ. Николай Расказовский и
# Григорий Феодоровский.
kirillovo_deaths_1914 = death_records(
    "ГАПО",
    "182",
    "5",
    "574",
    "Кириллово",
    "Казанская церковь",
    1914,
    *death_month(Month.FEBRUARY,
                 # Пелагия, дочь Григория Степановича Мальчикова, близнец, р. 11.10.1908 (рожд. 1908 ж. №87)
                 death(9, Gender.FEMALE, 8, 9,
                       deceased=person("Пелагія", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Григорій", "Стефановъ", "Мальчиковъ"), Relationship.FATHER)],
                       age=5,
                       page="144об",
                       reviewed=False),
                 # Стефанида, дочь Николая Петровича Мальчикова
                 death(13, Gender.FEMALE, 27, 28,
                       deceased=person("Стефанида", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Николай", "Петровъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="возраст у края («2…»)",
                       page="146об",
                       reviewed=False),
                 ),
    *death_month(Month.MARCH,
                 # Алексей, сын Петра Герасимовича Мальчикова, р. 11.03.1914 (рожд. м. №21)
                 death(14, Gender.MALE, 15, 16,
                       deceased=person("Алексѣй", status=PEASANT_SON),
                       relatives=[relative(person("Петръ", "Герасимовъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="возраст у края",
                       page="148об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Павел, сын Игната Михайловича Мальчикова («Мамчиковъ»), р. 11.12.1912 (рожд. 1912 м. №104)
                 death(38, Gender.MALE, 5, 6,
                       deceased=person("Павелъ", status=PEASANT_SON),
                       relatives=[relative(person("Игнатъ", "Михайловъ", "Мамчиковъ", comment="= Игнат Михайлович Мальчиков"), Relationship.FATHER)],
                       age="1 г 6 мес",
                       page="158об",
                       reviewed=False),
                 # Иоанн, сын Петра Никитича Мальчикова, р. 1.01.1914 (рожд. м. №1)
                 death(40, Gender.MALE, 5, 6,
                       deceased=person("Іоаннъ", status=PEASANT_SON),
                       relatives=[relative(person("Петръ", "Никитинъ", "Мальчиковъ"), Relationship.FATHER)],
                       age="6 мес",
                       page="158об",
                       reviewed=False),
                 # Пелагия, дочь Алексея Михайловича «Юлина» (брак 1914 №7)
                 death(41, Gender.FEMALE, 15, 16,
                       deceased=person("Пелагія", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Алексѣй", "Михайловъ", "Юлинъ"), Relationship.FATHER)],
                       age=1,
                       comment="«1» — возраст так; отец женат 29.01.1914",
                       page="160об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Евфимий, сын Евфимия Ивановича Молоткова и Натальи Васильевны (урожд. Мальчиковой), р. 16.10.1914 (рожд.
                 # м. №84)
                 death(64, Gender.MALE, None, None,
                       deceased=person("Евфимій", status=PEASANT_SON),
                       relatives=[relative(person("Евфимій", "Ивановъ", "Молотковъ"), Relationship.FATHER)],
                       age="1 мес",
                       comment="даты смерти и погребения не вписаны (между 12 и 24 октября)",
                       page="166об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
