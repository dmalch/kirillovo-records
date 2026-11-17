from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, OLD_AGE
from verso.ru.dsl.statuses import (DEACON, ECON_PEASANT_FEMALE, ECON_PEASANT_MALE,
                                   GOSUDARSTVENNYJ_PEASANT_MALE, HIEREUS, PEASANT_DAUGHTER,
                                   PEASANT_SON, WIDOW)

# SELECTIVE EXTRACT: Only Мальчиков-family related entries from 1879 metric book.
# Archive reference unknown for this period; using placeholder.
# No page numbers available in source extract.
# No clergy names recorded in source extract.
# Death #20 (female, Марфа): relative — солдат Прокофий Иванов Мальчиков.
# Relationship inferred as FATHER (infant 1 week old, father would be the reporting relative).

kirillovo_deaths_1879 = death_records(
    "ГАПО",
    "182",
    "5",
    "734",
    "Кириллово",
    "Казанская церковь",
    1879,
    *death_month(
        Month.JULY,
        # сверено по скану 05.10.2026 (альбом «1879 (ГАПО 182-5-734)», pk 1320, л. 166об): совпадает — «солдата Прокофія
        # Иванова Мальчикова дочь Марѳа», 1 недѣля, отъ колики, умерла 11, погребена 12 июля; р. 3.07.1879 (рожд. ж. №38)
        death(
            20,
            Gender.FEMALE,
            11,
            12,
            deceased=person("Марфа", "Прокофьева", last_name_orig="Мальчикова"),
            age=1 / 52,
            relatives=[relative(person("Прокофий", "Иванов", last_name_orig="Мальчиков"), Relationship.FATHER)],
            cause_of_death=COLIC,
            comment="Возраст умершей — 1 неделя; родственник — солдат; дата (под вопросом в источнике)",
        ),
    ),
    # Дописано при сплошном проходе (05.10.2026) по скану (альбом «1879 (ГАПО 182-5-734)», pk 1320) — записи первой
    # волны, которых не было в импорте. Ч. 3 — лл. 157об–175об, 44 муж. и 42 жен., прочитана целиком. Книга пишет
    # «государственный крестьянинъ» (умолчания файла остались от импорта — статусы записаны у каждого). Погребал
    # настоятель, священник Василий Иоаннов Ремезов, с псаломщиком диаконом Матфеем Рождественским.
    *death_month(Month.JANUARY,
                 # Илья, сын Никиты Козьмича Мальчикова, р. 14.07.1878 (рожд. 1878 м. №46)
                 death(6, Gender.MALE, 16, 17,
                       deceased=person("Илія", status=PEASANT_SON, comment="в подлиннике «Илья»"), age="6 мес",
                       relatives=[relative(person("Никита", "Козьминъ", "Мальчиковъ", status=GOSUDARSTVENNYJ_PEASANT_MALE), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       page="158об",
                       reviewed=False),
                 ),
    *death_month(Month.FEBRUARY,
                 # вдова Феврония Ивановна «Сырдцева» — вдова кого-то из Яниных-Сырцевых (кого — не установлено)
                 death(3, Gender.FEMALE, 2, 3,
                       deceased=person("Февронія", "Иванова", "Сырцева", status=WIDOW, comment="в подлиннике «Сырдцева»"), age=65,
                       cause_of_death=OLD_AGE,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       page="159об",
                       reviewed=False),
                 ),
    *death_month(Month.APRIL,
                 # Татьяна, дочь Семена Родионовича «Алешина» (= Янина?), р. 14.01.1879 (рожд. ж. №3)
                 death(11, Gender.FEMALE, 18, 19,
                       deceased=person("Татіана", status=PEASANT_DAUGHTER, residence="Гоголев Бор"), age="3 мес",
                       relatives=[relative(person("Семенъ", "Родіоновъ", "Алешинъ", status=GOSUDARSTVENNYJ_PEASANT_MALE, comment="«Алешинъ» — так в подлиннике; = Янин?"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       page="162об",
                       reviewed=False),
                 ),
    *death_month(Month.MAY,
                 # Тимофей, сын Матвея Егоровича Янина («Сырдцевъ»), р. 1.05.1878 (близнец, рожд. 1878 м. №26)
                 death(24, Gender.MALE, 18, 19,
                       deceased=person("Тимоѳей", status=PEASANT_SON), age=1,
                       relatives=[relative(person("Матвѣй", "Егоровъ", "Сырцевъ", status=GOSUDARSTVENNYJ_PEASANT_MALE, comment="в подлиннике «Сырдцевъ»; = Матвей Егорович Янин"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       page="163об",
                       reviewed=False),
                 ),
    *death_month(Month.JULY,
                 # Иоанн, сын Михаила Васильевича Мальчикова («Юлинъ»), р. 5.07.1879 (рожд. м. №53)
                 death(32, Gender.MALE, 27, 28,
                       deceased=person("Іоаннъ", status=PEASANT_SON), age="3 нед",
                       relatives=[relative(person("Михаилъ", "Васильевъ", "Юлинъ", status=GOSUDARSTVENNYJ_PEASANT_MALE, comment="= Михаил Васильевич Мальчиков"), Relationship.FATHER)],
                       cause_of_death=COLIC,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       page="167об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # вдова Екатерина Петровна «Сырдцева» — вдова кого-то из Яниных-Сырцевых; кандидат — Степан Денисович Янин,
                 # женившийся в 1837 (брак №22) на Екатерине Петровне Горбуновой (Денисовичи пишутся и «Сырцовыми»)
                 death(39, Gender.FEMALE, 10, 12,
                       deceased=person("Екатерина", "Петрова", "Сырцева", status=WIDOW, comment="в подлиннике «Сырдцева»"), age=75,
                       cause_of_death=OLD_AGE,
                       priest=person("Василій", "Іоанновъ", "Ремезовъ", status=HIEREUS),
                       deacon=person("Матѳей", last_name_orig="Рождественскій", status=DEACON),
                       page="174об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
