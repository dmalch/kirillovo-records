from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS, PEASANT_DAUGHTER,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Альбом «1862 (ЦГАРМ 57-6-457)», pk 1338,
# ч. 3 — кадры 57–82, прочитаны целиком 02.10.2026; импорта смертей не было.
kirillovo_deaths_1862 = death_records(
    "ЦГАРМ",
    "57",
    "6",
    "457",
    "Кириллово",
    "Казанская церковь",
    1862,
    *page("?",
          *death_month(Month.AUGUST,
                       # Алексей — сын Григория Меркурьевича Чекмурина и Вассы Ионовны Мальчиковой, род. 15.03.1862 (рожд. м. №17)
                       death(52, Gender.MALE, 1, 3,
                             deceased=person("Алексѣй", status=PEASANT_SON), age="5 мес",
                             relatives=[relative(person("Григорій", "Меркурьевъ", "Чекмуринъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Василій", "Іоакимовъ", "Бѣльскій", status=HIEREUS),
                             comment="кадр 74 альбома",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены чтением книги по скану (альбом pk 1338)
    *page("?",
          *death_month(Month.JANUARY,
                       # Александр — сын Павла Константиновича Федулова и Пелагии Константиновны Мальчиковой, род. 14.11.1859
                       death(3, Gender.MALE, 4, 6,
                             deceased=person("Александръ", status=PEASANT_SON), age=2,
                             relatives=[relative(person("Павелъ", "Константиновъ", "Ѳедуловъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             priest=person("Андрей", last_name_orig="Глазуновъ", status=HIEREUS),
                             comment="кадр 57 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.AUGUST,
                       # Ольга — дочь Романа Павловича Сенаторова и Марии Васильевны Мальчиковой, близнец, род. 11.06.1860
                       death(54, Gender.FEMALE, 28, 30,
                             deceased=person("Ольга", status=PEASANT_DAUGHTER), age="1 год 6 мес",
                             relatives=[relative(person("Романъ", "Павловъ", "Сенаторовъ"), Relationship.FATHER)],
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="кадр 75 альбома; в графе лѣтъ «1½» (по рождению ей 2 г. 2½ мес); причина обрезана краем кадра («отъ гор…»)",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE, cause_of_death=NATURAL),
)
