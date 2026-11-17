from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, COUGH, PARALYSIS, WEAKNESS
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON,
                                   PEASANT_WIFE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-307, альбом
# Photos «1901 (ГАПО 182-5-307)» (pk 1185), ч. 3 — лл. 165об–190об, 64 муж. / 51 жен. (по ведомости на л. 191), прочитана
# целиком 25.10.2026; л. 164об — пустой, л. 165 — шмуцтитул; импорта не было. Вся запись — на левой странице, причина — на
# правой. Погребали свящ. Александр Васильев Писарев и Павел Богословский. Вложены лист Московского губернатора (л. 179),
# справка пристава 2 стана Спасского уезда (№964) и телеграмма Тамбовской консистории (лл. 181об–184) — о чужих.
kirillovo_deaths_1901 = death_records(
    "ГАПО",
    "182",
    "5",
    "307",
    "Кириллово",
    "Казанская церковь",
    1901,
    *death_month(Month.JANUARY,
                 # Гавриил, сын Михаила Васильевича Мальчикова («Юлинъ»), р. 9.07.1900 (рожд. 1900 м. №60)
                 death(1, Gender.MALE, 2, 2,
                       deceased=person("Гавріилъ", status=PEASANT_SON), age="6 мес",
                       relatives=[relative(person("Михаилъ", "Васильевъ", "Юлинъ"), Relationship.FATHER)],
                       cause_of_death=COUGH,
                       page="165об",
                       reviewed=False),
                 ),
    *death_month(Month.MARCH,
                 # Василий, сын Ильи Петровича Мальчикова, р. 24.02.1901 (рожд. м. №18)
                 death(14, Gender.MALE, 2, 3,
                       deceased=person("Василій", status=PEASANT_SON), age="1 нед",
                       relatives=[relative(person("Илья", "Петровъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=WEAKNESS,
                       page="169об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Сергей Дементьевич Ладыгин («Сѣрковъ»), муж Пелагии Семеновны Мальчиковой
                 death(23, Gender.MALE, 26, 27,
                       deceased=person("Сергѣй", "Дементьевъ", "Сѣрковъ", comment="= Сергей Дементьевич Ладыгин"), age=73,
                       comment="причина закрыта зажимом",
                       page="173",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Иван, сын Егора Михайловича Янина («Сырцовъ»), р. 4.05.1901 (рожд. м. №35)
                 death(31, Gender.MALE, 22, 23,
                       deceased=person("Іоаннъ", status=PEASANT_SON), age="7 нед",
                       relatives=[relative(person("Егоръ", "Михайловъ", "Сырцовъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       comment="возраст читается неуверенно («1 нед.» или «7 нед.»)",
                       page="176об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Евфросиния, дочь Василия Степановича Мальчикова, р. 20.06.1901 (рожд. ж. №38, отец «Бурлинъ»)
                 death(29, Gender.FEMALE, 5, 6,
                       deceased=person("Евфросинія", status=PEASANT_DAUGHTER), age="2 нед",
                       relatives=[relative(person("Василій", "Стефановъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       page="177об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Ирина Матвеевна Янина («Сырцова»), жена Василия Андреевича Ладыгина (брак 1901 №12)
                 death(48, Gender.FEMALE, 24, 25,
                       deceased=person("Ирина", "Матѳеева", status=PEASANT_WIFE, comment="= Ирина Матвеевна Сырцова (Янина)"), age=20,
                       relatives=[relative(person("Василій", "Андреевъ", "Сѣрковъ", comment="= Василий Андреевич Ладыгин"), Relationship.HUSBAND)],
                       cause_of_death=PARALYSIS,
                       page="189об",
                       reviewed=False),
                 ),
    *death_month(Month.DECEMBER,
                 # Иван, сын Ивана Михайловича Мальчикова (рожд. м. №89, крещен повивальной бабкой)
                 death(61, Gender.MALE, 14, 15,
                       deceased=person("Іоаннъ", status=PEASANT_SON), age="1 дн",
                       relatives=[relative(person("Иванъ", "Михайловъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="возраст читается неуверенно; причина на оторванном крае листа",
                       page="190об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
