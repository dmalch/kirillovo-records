from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, CONSUMPTION, NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, HIEREUS,
                                   PEASANT_DAUGHTER, PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Альбом «1866 (ГАПО 182-5-710)», pk 1354,
# ч. 3 — лл. 239об–253об, прочитаны целиком 03.10.2026; импорта смертей не было. В графе дат этого года одно число;
# между концом июня и ноябрём листов нет.
kirillovo_deaths_1866 = death_records(
    "ГАПО",
    "182",
    "5",
    "710",
    "Кириллово",
    "Казанская церковь",
    1866,
    *page("?",
          *death_month(Month.APRIL,
                       # Иван — сын Игната Ивановича Ладыгина и Пелагии Несторовны Мальчиковой, род. 3.01.1865
                       death(16, Gender.MALE, 22, None,
                             deceased=person("Иванъ", status=PEASANT_SON), age=1,
                             relatives=[relative(person("Игнатъ", "Ивановъ", "Ладыгинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="л. 245об",
                             reviewed=False),
                       ),
          *death_month(Month.NOVEMBER,
                       # Матрона — дочь Игната Андреевича Тришина и Ѳеодосии Андреяновны Мальчиковой, род. 6.11.1866 (рожд. ж. №100)
                       death(64, Gender.FEMALE, 12, None,
                             deceased=person("Матрона", status=PEASANT_DAUGHTER, comment="в подлиннике «Митрона»"), age="1 нед",
                             relatives=[relative(person("Игнатъ", "Андреевъ", "Тришкинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             priest=person("Андрей", last_name_orig="Тихомировъ", status=HIEREUS),
                             comment="л. 250об",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (08.11.2026): Алексей Емельянович Пимкин — второй муж Февронии Герасимовны Мальчиковой
    # (брак 1844 №18; в 1844–1854 «Пишкинъ», «Лапшинъ», «Пимкинъ»)
    *page("240об",
          *death_month(Month.FEBRUARY,
                       death(4, Gender.MALE, 11, None,
                             deceased=person("Алексѣй", "Емельяновъ", "Пимкинъ"), age=40,
                             cause_of_death=CONSUMPTION,
                             priest=person("Іоаннъ", "Васильевъ", "Ремезовъ", status=HIEREUS),
                             comment="кадр 36 альбома; іерей Іоаннъ Ремезовъ, діаконъ Матѳей Рождественскій, дьячекъ Илья Петровъ",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE, cause_of_death=NATURAL),
)
