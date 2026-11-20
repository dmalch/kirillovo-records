from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, NATURAL
from verso.ru.dsl.statuses import (HIEREUS, KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE,
                                   PEASANT_DAUGHTER, PEASANT_SON, SOLDIER)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. ЦГАРМ 57-6-449, Яндекс.Архив 292645c8-…,
# ч. 3 Кириллова — сканы 767–796.
kirillovo_deaths_1861 = death_records(
    "ЦГАРМ", "57", "6", "449", "Кириллово", "Казанская",
    1861,
    *page("?",
          *death_month(Month.JULY,
                       # Василий — сын Самсона Наумовича Янина, род. 22.03.1861 (рожд. м. №31): по дате ему около 4 мес
                       death(50, Gender.MALE, 17, 19,
                             deceased=person("Василій", status=PEASANT_SON), age="2 мес",
                             relatives=[relative(person("Самсонъ", "Наумовъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Андрей", last_name_orig="Глазуновъ", status=HIEREUS),
                             comment="скан 785; возраст «2х мцевъ» — так в подлиннике",
                             reviewed=False),
                       # Иоанн — сын Андрея Ивлиевича Романова и Татианы Несторовны Мальчиковой, род. 4.05.1861 (рожд. м. №42)
                       death(53, Gender.MALE, 28, 30,
                             deceased=person("Іоаннъ", status=PEASANT_SON), age="3 мес 2 нед",
                             relatives=[relative(person("Андрей", "Ивліевъ", "Романовъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Василій", "Іоакимовъ", "Бѣльскій", status=HIEREUS),
                             comment="скан 786; возраст в подлиннике «3½ мцевъ»",
                             reviewed=False),
                       ),
          *death_month(Month.NOVEMBER,
                       # Антон Иванович — отец Яниных-Антоновичей (Карп, Ѳедор, Ульяна, Ксения), книга пишет их «Хрипуновы»
                       death(73, Gender.MALE, 4, 6,
                             deceased=person("Антонъ", "Ивановъ", "Хрипуновъ", comment="он же: Антон Иванович Янин"), age=60,
                             priest=person("Андрей", last_name_orig="Глазуновъ", status=HIEREUS),
                             comment="скан 793",
                             reviewed=False),
                       # Семен Яковлевич — сын Якова Максимовича; жених 1859 №15 («Мальчиковъ»)
                       death(78, Gender.MALE, 23, 25,
                             deceased=person("Семенъ", "Яковлевъ", "Позняковъ", comment="он же: Семен Яковлевич Мальчиков (брак 1859 №15)"), age=22,
                             cause_of_death=DIARRHEA,
                             priest=person("Андрей", last_name_orig="Глазуновъ", status=HIEREUS),
                             comment="скан 794",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены поиском фамилий мужей по OCR Яндекс.Архива и
    # прочитаны по оригиналам
    *page("?",
          *death_month(Month.AUGUST,
                       # Мария — дочь Михаила Денисовича Стюхина и Александры Андреевны Мальчиковой, род. 28.03.1861
                       death(64, Gender.FEMALE, 14, 19,
                             deceased=person("Марія", status=PEASANT_DAUGHTER), age="4 мес",
                             relatives=[relative(person("Михаилъ", "Денисовъ", "Стюхинъ", status=SOLDIER, comment="«уволенный въ безсрочный отпускъ по билету»"),
                                                 Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="скан 788; возрастъ «4-хъ мцевъ»",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=KAZENNYJ_PEASANT_MALE,
        status_female=KAZENNYJ_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
