from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import DIARRHEA, NATURAL
from verso.ru.dsl.statuses import (DEACON, HIEREUS, KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   PEASANT_DAUGHTER, PEASANT_WIFE)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их замужние дочери). ГАПО 182-5-732,
# альбом Photos «1871 (ГАПО 182-5-732)» (pk 3616), ч. 3 — лл. 43об–66, 134 погребения; прочитана целиком
# 05.10.2026. С конца июля по сентябрь — холера.
kirillovo_deaths_1871 = death_records(
    "ГАПО",
    "182",
    "5",
    "732",
    "Кириллово",
    "Казанская церковь",
    1871,
    *death_month(Month.JANUARY,
                 # = Матрена Андреяновна Мальчикова, жена Ермолая Афанасьевича Егорова (брак 1857); вдовец женился
                 # вторым браком 9.02.1871 (брак №14)
                 death(7, Gender.FEMALE, 28, 30,
                       deceased=person("Матрена", status=PEASANT_WIFE), age=35,
                       relatives=[relative(person("Ермолай", "Аѳанасьевъ", "Егоровъ"), Relationship.HUSBAND)],
                       cause_of_death="от по…ри",
                       priest=person("Павелъ", "Ѳеофановъ", "Кротковъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       comment="причина смерти не разобрана («отъ по…ри»)",
                       page="45об",
                       reviewed=False),
                 ),
    *death_month(Month.JUNE,
                 # Елена, дочь Алексея Данииловича Янина («Прокофіевъ» — по отчиму?), р. 7.05.1871 (рожд. ж. №18); её погребение записано
                 # дважды — №25 (29/30 июня, 7 нед., причина не написана) и №26 (3/4 июля, 9 нед., от поноса); у обеих
                 # записей на полях крестик
                 death(25, Gender.FEMALE, 29, 30,
                       deceased=person("Елена", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age="7 нед",
                       relatives=[relative(person("Алексѣй", "Прокофіевъ", "Янинъ", comment="так в подлиннике; = Алексей Даниилович Янин? (в Гоголевом Бору есть и Алексей Прокофьевич Слѣповъ — восприемник 1878)"), Relationship.FATHER)],
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       comment="причина смерти не написана; та же Елена записана ещё раз под №26 (3 июля)",
                       page="52об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # повтор записи №25 (см. выше)
                 death(26, Gender.FEMALE, 3, 4,
                       deceased=person("Елена", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age="9 нед",
                       relatives=[relative(person("Алексѣй", "Прокофіевъ", "Янинъ", comment="так в подлиннике; = Алексей Даниилович Янин? (в Гоголевом Бору есть и Алексей Прокофьевич Слѣповъ — восприемник 1878)"), Relationship.FATHER)],
                       cause_of_death=DIARRHEA,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       comment="та же Елена, что в №25 (29 июня): погребение записано дважды",
                       page="53об",
                       reviewed=False),
                 # «Села Кирилова крестьянка Ирина Петрова Янина» — в корпусе не встречалась
                 death(30, Gender.FEMALE, 26, 26,
                       deceased=person("Ирина", "Петрова", "Янина"), age=65,
                       cause_of_death=NATURAL,
                       priest=person("Павелъ", "Ѳеофановъ", "Кротковъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       comment="в подлиннике записана в МУЖСКОЙ счёт под №30 (женский №30 — Параскева Шачкина, 24 июля)",
                       page="54об",
                       reviewed=False),
                 # Иван Петрович Мальчиков — поручитель 1837, 1861 и 1868 гг.; чей сын — не установлено
                 death(32, Gender.MALE, 29, 29,
                       deceased=person("Иванъ", "Петровъ", "Мальчиковъ"), age=55,
                       cause_of_death="холера",
                       priest=person("Павелъ", "Ѳеофановъ", "Кротковъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       page="55об",
                       reviewed=False),
                 ),
    *death_month(Month.AUGUST,
                 # дочь Константина Мальчикова — которого (Яковлевича или Козьмича), не установлено
                 death(63, Gender.FEMALE, 31, 31,
                       deceased=person("Екатерина", status=PEASANT_DAUGHTER), age=15,
                       relatives=[relative(person("Константинъ", None, "Мальчиковъ", comment="отчества нет"), Relationship.FATHER)],
                       cause_of_death="холера",
                       priest=person("Павелъ", "Ѳеофановъ", "Кротковъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       page="62об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=KAZENNYJ_PEASANT_MALE, status_female=KAZENNYJ_PEASANT_FEMALE),
)
