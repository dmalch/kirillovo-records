from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import FEVER
from verso.ru.dsl.statuses import PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-302, альбом
# Photos «1910 (ГАПО 182-5-302)» (pk 1199), ч. 3 — л. 123 шмуцтитул, лл. 123об–151об (м. №1–68, ж. №1–67), прочитана
# 26.10.2026 до 16 ноября; дальше в альбоме листов нет — погребений 17 ноября — 31 декабря 1910 в наборе нет. Импорта не
# было. Возраст и причина у сгиба, почти не читаются. Погребали свящ. Александр Васильев Писарев, Павел Богословский, с
# сентября и Николай Раскаровский?. 29.08 (м. №61) погребён «Никифоръ Максимовъ Мокоусовъ?» — И.О. как у Никифора
# Максимовича «Дунаева» (брак 1908 №16), фамилия иная; не взят.
kirillovo_deaths_1910 = death_records(
    "ГАПО",
    "182",
    "5",
    "302",
    "Кириллово",
    "Казанская церковь",
    1910,
    *death_month(Month.MARCH,
                 # Михаил, сын Михаила Константиновича Мальчикова, р. 20.03.1910 (рожд. м. №21)
                 death(12, Gender.MALE, 23, 24,
                       deceased=person("Михаилъ", status=PEASANT_SON),
                       relatives=[relative(person("Михаилъ", "Константиновъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="возраст и причина в сгибе",
                       page="127об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # Николай, сын Павла Егоровича «Сырцова»? (как 1907 м. №1)
                 death(21, Gender.MALE, 18, 19,
                       deceased=person("Николай", status=PEASANT_SON),
                       relatives=[relative(person("Павелъ", "Егоровъ", "Сырцовъ", comment="фамилия читается неуверенно («Св…цовъ»); он же: Янин?"), Relationship.FATHER)],
                       age="2 нед",
                       comment="возраст у сгиба читается неуверенно; причина в сгибе",
                       page="132об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Александр, сын Владимира Дмитриевича «Кистенева» (рожд. м. №41 — 11.06)
                 death(24, Gender.MALE, 10, 11,
                       deceased=person("Александръ", status=PEASANT_SON),
                       relatives=[relative(person("Владиміръ", "Димитріевъ", "Кистеневъ"), Relationship.FATHER)],
                       comment="возраст и причина в сгибе",
                       source_date_error="умер 10, погребён 11 июня, а в рожд. (м. №41) рождён и крещён 11 июня — так в подлиннике",
                       page="133об",
                       reviewed=False),
                 # Федор, сын Василия Андреевича Ладыгина («Сѣрковъ»)
                 death(28, Gender.MALE, 18, 19,
                       deceased=person("Ѳеодоръ", status=PEASANT_SON),
                       relatives=[relative(person("Василій", "Андреевъ", "Ладыгинъ"), Relationship.FATHER)],
                       comment="возраст и причина в сгибе",
                       page="134об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Леонтий, сын Ильи Андреевича «Кистенева», р. 13.06.1910 (рожд. м. №42)
                 death(34, Gender.MALE, 5, 6,
                       deceased=person("Леонтій", status=PEASANT_SON),
                       relatives=[relative(person("Илья", "Андреевъ", "Кистеневъ", comment="он же: Илья Андреевич Молохаев"), Relationship.FATHER)],
                       comment="возраст и причина в сгибе",
                       page="136об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Василий, сын Тимофея Михайловича «Юлина», р. 29.01.1910 (рожд. м. №10)
                 death(55, Gender.MALE, 19, 20,
                       deceased=person("Василій", status=PEASANT_SON),
                       relatives=[relative(person("Тимоѳей", "Михайловъ", "Юлинъ", comment="фамилия у корешка («Ю…ина»)"), Relationship.FATHER)],
                       comment="возраст и причина в сгибе",
                       page="145об",
                       reviewed=False),
                 ),
    # Вторая волна (08.11.2026): мужья замужних дочерей Мальчиковых и Яниных
    *death_month(Month.MARCH,
                 # Федор Денисович Паршин — муж Татьяны Федоровны Мальчиковой (брак 1898); она вдовой вышла
                 # вторым браком в 1911 (брак №10)
                 death(13, Gender.MALE, 24, 25,
                       deceased=person("Ѳеодоръ", "Діонисіевъ", "Паршинъ"), age=30,
                       cause_of_death=FEVER,
                       comment="возраст у сгиба («30»?) читается неуверенно; «отъ горячки»; погребалъ свящ. Павелъ Богословскій",
                       page="128об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
