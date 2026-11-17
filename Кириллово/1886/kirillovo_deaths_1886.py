from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, MEASLES, OLD_AGE, PLEURISY, SCARLATINA
from verso.ru.dsl.statuses import (GOSUDARSTVENNYJ_PEASANT_FEMALE, GOSUDARSTVENNYJ_PEASANT_MALE,
                                   HIEREUS, PEASANT_DAUGHTER, PEASANT_SON, PRIEST, SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и дети их замужних дочерей). ГАПО 182-5-296,
# альбом Photos «1886 (ГАПО 182-5-296)» (pk 1356), ч. 3 — лл. 246об–284об (л. 244об–246 — чистый разворот), прочитана
# целиком 24.10.2026; импорта не было. Вся запись — на левой странице, причина — на правой. До октября погребал
# настоятель, свящ. Василий Иоаннов Ремезов, с конца октября — свящ. Покровской церкви Феодор Виноградов. Осенью — корь и
# скарлатина: в октябре трое сыновей Петра Иванова Юдина (Юдины, не «Юлины») за неделю. Листы 284а об и 284об
# переставлены при подшивке; конец декабря на рваном листе. Ведомость (л. 288): 64 + 62 = 126 рождений.
kirillovo_deaths_1886 = death_records(
    "ГАПО",
    "182",
    "5",
    "296",
    "Кириллово",
    "Казанская церковь",
    1886,
    *death_month(Month.MARCH,
                 # Константин Козьмич Мальчиков («Малахѣевъ» 1835–64, «Стрекалинъ» 1836)
                 death(7, Gender.MALE, 21, 22,
                       deceased=person("Константинъ", "Казминъ", "Стрекалинъ", comment="«Стрекалинъ» — так в подлиннике; = Константин Козьмич Мальчиков"),
                       age=70,
                       cause_of_death=OLD_AGE,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="возраст и причина у дыры листа («70», «отъ стар…»)",
                       page="251об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Анна, дочь Егора Аникеевича Зосимова и Марии Михайловны (Яниной?), р. 3.02.1886 (рожд. ж. №7)
                 death(25, Gender.FEMALE, 22, 23,
                       deceased=person("Анна", status=PEASANT_DAUGHTER), age="6 мес",
                       relatives=[relative(person("Егоръ", "Аникѣевъ", "Зосимовъ"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="возраст в подлиннике «½»",
                       page="257об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # Гавриил, сын Андрея Сергеевича Серкова (Ладыгина), р. 14.07.1886 (рожд. м. №36)
                 death(28, Gender.MALE, 1, 2,
                       deceased=person("Гавріилъ", status=PEASANT_SON), age="3 нед",
                       relatives=[relative(person("Андрей", "Сергѣевъ", "Серковъ", comment="= Андрей Сергеевич Ладыгин"), Relationship.FATHER)],
                       cause_of_death=PLEURISY,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="причина в подлиннике «отъ колотія»; возраст читается неуверенно",
                       page="262об",
                       reviewed=False),
                 # Василий, сын Степана Сергеевича Ладыгина, р. 30.07.1886 (рожд. м. №39)
                 death(30, Gender.MALE, 7, 8,
                       deceased=person("Василій", status=PEASANT_SON), age="2 нед",
                       relatives=[relative(person("Стефанъ", "Сергѣевъ", "Ладыгинъ", status=SOLDIER, comment="«запасный рядовой»"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="264об",
                       reviewed=False),
                 # Надежда, дочь Николая Петровича Мальчикова, р. 7.09.1885 (рожд. 1885 ж. №57)
                 death(37, Gender.FEMALE, 13, 14,
                       deceased=person("Надежда", status=PEASANT_DAUGHTER), age=1,
                       relatives=[relative(person("Николай", "Петровъ", "Мальчиковъ"), Relationship.FATHER)],
                       cause_of_death=SCARLATINA,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="причина в подлиннике «отъ скорлатины»",
                       page="264об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Матвей, сын Федора Самсоновича Янина
                 death(49, Gender.MALE, 10, 11,
                       deceased=person("Матвѣй", status=PEASANT_SON), age=10,
                       relatives=[relative(person("Ѳеодоръ", "Самсоновъ", "Янинъ"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       page="274об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Елена, дочь Михаила Васильевича Мальчикова («Юлинъ»), р. 20.05.1883 (рожд. 1883 ж. №26)
                 death(68, Gender.FEMALE, 22, 24,
                       deceased=person("Елена", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Михаилъ", "Васильевъ", "Юлинъ", comment="«Юлинъ» — так в подлиннике; = Михаил Васильевич Мальчиков"), Relationship.FATHER)],
                       cause_of_death=MEASLES,
                       priest=person("Ѳеодоръ", None, "Виноградовъ", status=PRIEST, comment="«Покровской церкви священникъ»"),
                       comment="графа возраста пуста (дыра листа); причина «отъ кори»",
                       page="280об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=GOSUDARSTVENNYJ_PEASANT_MALE,
                            status_female=GOSUDARSTVENNYJ_PEASANT_FEMALE),
)
