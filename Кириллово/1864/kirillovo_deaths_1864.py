from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, DIARRHEA, DROPSY, FEVER, THROAT
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS, MAIDEN,
                                   PEASANT_DAUGHTER, PEASANT_SON)

# SELECTIVE EXTRACT: Only Мальчиков-family related entries from 1864 metric book.
# Archive reference unknown for this period; using placeholder.
# No page numbers available in source extract.
# No clergy names recorded in source extract.
# Death #60 (female): relative is Андрей Васильев Мальчиков — relationship inferred as FATHER
# Death #73 (male): no relative listed.

kirillovo_deaths_1864 = death_records(
    "ГАПО",
    "182",
    "5",
    "710",
    "Кириллово",
    "Казанская церковь",
    1864,
    *death_month(
        Month.OCTOBER,
        # сверено по скану 12.10.2026: лист ГАПО-экземпляра книги 1864 г. подшит в дело 182-5-300 (альбом «1883 (ГАПО
        # 182-5-300)», pk 1292, кадр «л.334об.-335»): «Андрея Васильева Мальчикова дочь Евдокія», 18 л., от чахотки,
        # умерла 7, погребена 9 октября — совпадает
        death(
            60,
            Gender.FEMALE,
            7,
            9,
            deceased=person("Евдокия", "Андреева", last_name_orig="Мальчикова"),
            age=18,
            relatives=[relative(person("Андрей", "Васильев", last_name_orig="Мальчиков"), Relationship.FATHER)],
            cause_of_death=CONSUMPTION,
        ),
        death(73, Gender.MALE, 25, 27, deceased=person("Карп", "Васильев", last_name_orig="Мальчиков"), age=30, cause_of_death=FEVER),
    ),
    # Дописано при сплошном проходе (03.10.2026) по скану (альбом «1864 (ЦГАРМ 57-6-477)», pk 1344; кадры альбома
    # в comment) — записи первой волны, которых не было в импорте из таблицы
    *page("?",
          *death_month(Month.JANUARY,
                       # Пелагия Константиновна Мальчикова (брак 1859 №13 с Павлом Константиновичем, там «Ѳеодуловъ»)
                       death(13, Gender.FEMALE, 29, 31,
                             deceased=person("Пелагія", "Константинова"), age=25,
                             relatives=[relative(person("Павелъ", "Константиновъ", "Абаевъ"), Relationship.HUSBAND)],
                             cause_of_death=CONSUMPTION,
                             priest=person("Василій", "Іоакимовъ", "Бѣльскій", status=HIEREUS),
                             comment="кадр 57 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.JUNE,
                       # Матрена, дочь Константина Козьмича Мальчикова («Малахѣевъ»)
                       death(38, Gender.FEMALE, 1, 3,
                             deceased=person("Матрена", "Константинова", "Малахѣева", status=MAIDEN), age=16,
                             relatives=[relative(person("Константинъ", "Козьминъ", "Малахѣевъ"), Relationship.FATHER)],
                             cause_of_death=DROPSY,
                             priest=person("Андрей", last_name_orig="Глазуновъ", status=HIEREUS),
                             comment="кадр 64 альбома; в подлиннике «Казмина Малахѣева»",
                             reviewed=False),
                       # Иоанн — сын Сергея Карповича Янина («Сырцовъ»), род. 13.06.1864 (рожд. м. №62)
                       death(99, Gender.MALE, 17, 20,
                             deceased=person("Іоаннъ", status=PEASANT_SON), age="3 нед",
                             relatives=[relative(person("Сергѣй", "Карповъ", "Сырцовъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="кадр 64 альбома; возраст «3 нед.» — так в подлиннике (по записи о рождении — 4 дня)",
                             reviewed=False),
                       ),
          *death_month(Month.AUGUST,
                       # Семеон — сын Константина Яковлевича («Поздняковъ»), род. 27.04.1863 (рожд. 1863 м. №50)
                       death(61, Gender.MALE, 19, 20,
                             deceased=person("Симеонъ", status=PEASANT_SON), age="11 мес",
                             relatives=[relative(person("Константинъ", "Яковлевъ", "Поздняковъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             priest=person("Андрей", last_name_orig="Тихомировъ", status=HIEREUS),
                             comment="кадр 69 альбома; возраст читается «11 мес.» (по записи о рождении — год и четыре месяца)",
                             reviewed=False),
                       # дочь Петра Лаврентьевича Стрекалина и Варвары Несторовны Мальчиковой; 5 лет — Анастасия, род. 20.08.1859?
                       death(53, Gender.FEMALE, 22, 23,
                             deceased=person("Наталія", status=PEASANT_DAUGHTER, comment="имя читается неуверенно (или «Настасія» — тогда рожд. 1859 ж. №78)"),
                             age=5,
                             relatives=[relative(person("Петръ", "Лаврентьевъ", "Стрекалинъ"), Relationship.FATHER)],
                             cause_of_death=THROAT,
                             priest=person("Андрей", last_name_orig="Тихомировъ", status=HIEREUS),
                             comment="кадр 70 альбома",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
