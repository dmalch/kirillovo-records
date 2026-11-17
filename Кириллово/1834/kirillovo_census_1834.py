from verso.ru.dsl import (CensusRole, Month, RecordDefaults, census_records, household, member,
                          page, person)
from verso.ru.dsl.marital_status import WIDOWER
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE

# РС 8 (Восьмая ревизия) 1834 года, с. Кириллово
# Архив: ГАТО, ф. 12 оп. 1 д. 1377 — «Ревизские сказки Спасского уезда за 1834 год»
# (то же дело содержит РС 8 по Гоголеву Бору; в каталоге КАИСА дд. 1377–1386+
#  имеют одинаковый обобщённый заголовок, привязка к с. Кириллово — по ARCHIVES.md)
census = census_records(
    "ГАТО",
    "12",
    "1",
    "1377",
    "Кириллово",
    1834,
    # Семья № 188 — Стрекалины (не Мальчиковы; в документе на с. Кириллово)
    # Глава Казма Гаврилов Стрекалин умер в 1820; зять и пасынок тоже выбыли.
    # Из живых — только сын Константин (возраст 21).
    *page("71",
    household("188",
              member(1, person("Казма", "Гавриловъ", "Стрекалинъ"), CensusRole.HEAD, previous_age=63, departure_year=1820, departure_reason="умер"),
              member(2, person("Константинъ"), CensusRole.SON, age=21, previous_age=3),
              member(3, person("Лукьянъ", "Федоровъ", "Бугровъ"), CensusRole.SON_IN_LAW, previous_age=52, departure_year=1819, departure_reason="умер"),
              member(4, person("Матвей", "Васильевъ", "Пыхтинъ"), CensusRole.STEPSON, previous_age=17, departure_year=1832, departure_reason="умер"),
              ),
          ),
    # Семья № 301 — Трифоновы (л. 114об.–114)
    # Двор записан на Лазаря Григорьева, выбывшего в Саратовскую губернию в 1830;
    # фактически в хозяйстве остался его дядя Тимофей Трифонов с сыновьями —
    # единственная ветвь рода, не ушедшая в Саратов (ср. семью № 302).
    # Пётр Тимофеев — тот же человек, что и в МК Кириллово, рожд. 15.08.1810 № 63.
    # Год рекрутства в подлиннике правлен; читается «1833». «1823» невозможно:
    # Петру было бы 12 лет, а в 1831 у него родилась дочь Ирина.
    *page("114",
    household("301",
              member(1, person("Лазарь", "Григорьевъ"), CensusRole.HEAD, previous_age=23,
                     departure_year=1830, departure_reason="выбыл", destination="Саратовская губерния"),
              member(2, person("Тимофей", "Трифоновъ"), CensusRole.UNCLE, age=59, previous_age=41,
                     marital_status=WIDOWER, comment="в документе «Лазаря Григорьева дядя»"),
              member(3, person("Петръ"), CensusRole.SON, ref_member=2, previous_age=5,
                     departure_year=1833, departure_reason="отдан в рекруты", comment="в документе «отдан в рекруты в 1823», но ему было бы 12 лет; исправлено на 1833"),
              member(4, person("Денисъ"), CensusRole.SON, ref_member=3, age=7),
              member(5, person("Тимофей"), CensusRole.SON, ref_member=2, age=21, previous_age=3,
                     comment="в документе «Тимофея Трифонова другой сын Тимофей»"),
              member(6, person("Катерина"), CensusRole.WIFE, ref_member=3, age=25),
              member(7, person("Ефросинья"), CensusRole.DAUGHTER, ref_member=3, age=8),
              member(8, person("Ирина"), CensusRole.DAUGHTER, ref_member=3, age=3),
              member(9, person("Аксинья"), CensusRole.WIFE, ref_member=5, age=25),
              member(10, person("Аксинья"), CensusRole.DAUGHTER, ref_member=5, age="2 мес")),
    # Семья № 302 — Трифоновы (л. 114об., низ) — родные братья Тимофея Трифонова
    # из семьи № 301; всем двором выбыли в Саратовскую губернию в 1831 году.
    # ВНИМАНИЕ: нижний край листа обрезан на нашей фотографии — двор может быть
    # записан не полностью; женская половина пуста (все выбыли).
    household("302",
              member(1, person("Никита", "Трифоновъ"), CensusRole.HEAD, previous_age=37,
                     departure_year=1831, departure_reason="выбыл", destination="Саратовская губерния"),
              member(2, person("Лаврентій", "Трифоновъ"), CensusRole.BROTHER, previous_age=28,
                     departure_year=1831, departure_reason="выбыл", destination="Саратовская губерния"),
              member(3, person("Петръ"), CensusRole.SON, ref_member=2, previous_age="1 мес",
                     departure_year=1831, departure_reason="выбыл", destination="Саратовская губерния")),
          ),
    *page("199",
    # Семья № 523 — Мальчиковы (Дмитрий Давыдов)
    household("523",
              member(1, person("Димитрій", "Давыдовъ", "Мальчиковъ"), CensusRole.HEAD,
                     age=61, previous_age=43, marital_status=WIDOWER),
              member(2, person("Василій"), CensusRole.SON, age=32, previous_age=14),
              member(3, person("Григорій"), CensusRole.SON, ref_member=2, age=10),
              member(4, person("Нестер"), CensusRole.SON, age=35, previous_age=17),
              member(5, person("Марфа"), CensusRole.WIFE, ref_member=2, age=35),
              member(6, person("Анна"), CensusRole.DAUGHTER, ref_member=2, age=12),
              member(7, person("Аксинья"), CensusRole.DAUGHTER, ref_member=2, age=6),
              member(8, person("Василиса"), CensusRole.WIFE, ref_member=4, age=43),
              member(9, person("Варвара"), CensusRole.DAUGHTER, ref_member=4, age=16),
              member(10, person("Татьяна"), CensusRole.DAUGHTER, ref_member=4, age=12),
              member(11, person("Ирина"), CensusRole.DAUGHTER, ref_member=4, age=10),
              member(12, person("Варвара", comment="Варвара меньшая"), CensusRole.DAUGHTER, ref_member=4, age=5),
              member(13, person("Татьяна", comment="Татьяна меньшая"), CensusRole.DAUGHTER, ref_member=4, age=2)),
    # Семья № 524 — Мальчиковы (Павел Давыдов)
    # Архип Павлов отдан в рекруты в 1828 — в список не включён.
    household("524",
              member(1, person("Павелъ", "Давыдовъ", "Мальчиковъ"), CensusRole.HEAD, age=59, previous_age=41),
              member(2, person("Михаилъ"), CensusRole.SON, age=34, previous_age=16),
              member(3, person("Архипъ"), CensusRole.SON, previous_age=8, departure_year=1828, departure_reason="отдан в рекруты"),
              member(4, person("Федор"), CensusRole.SON, age=21, previous_age=3),
              member(5, person("Илья"), CensusRole.SON, age=13),
              member(6, person("Николай"), CensusRole.SON, age=10),
              member(7, person("Прасковья"), CensusRole.WIFE, age=58),
              member(8, person("Акулина"), CensusRole.DAUGHTER, age=20),
              member(9, person("Устинья"), CensusRole.WIFE, ref_member=2, age=35)),
          ),
    # Семья № 525 — Мальчиковы (Иван Федосеев)
    # Дмитрий Андреев умер в 1830 — не включён.
    # Яков Максимов Позняков/Мальчиков — живёт в хозяйстве (сын «Ивановой снохи солдатки»,
    # ИР 1828);
    *page("200",
    household("525",
              member(1, person("Иванъ", "Федосеевъ", "Мальчиковъ"), CensusRole.HEAD,
                     age=78, previous_age=60),
              member(2, person("Андрей"), CensusRole.SON, age=52, previous_age=34),
              member(3, person("Дмитрій"), CensusRole.SON, ref_member=2, previous_age=6, departure_year=1830, departure_reason="умер"),
              member(4, person("Иван"), CensusRole.SON, age=38, previous_age=20),
              member(5, person("Григорій"), CensusRole.SON, ref_member=4, age=21, previous_age=3),
              member(6, person("Андрей"), CensusRole.SON, ref_member=5, age=5),
              member(7, person("Никита"), CensusRole.SON, ref_member=5, age=3),
              member(8, person( "Яковъ", "Максимовъ"), CensusRole.STEPSON, ref_member=4, age=21, previous_age=3),
              member(9, person("Костентинъ"), CensusRole.SON, ref_member=8, age=1),
              member(10, person("Степанъ"), CensusRole.SON, ref_member=4, age=11),
              member(11, person("Костентинъ"), CensusRole.SON, ref_member=4, age=2),
              member(12, person("Екатерина"), CensusRole.WIFE, ref_member=2, age=53),
              member(13, person("Александра"), CensusRole.DAUGHTER, ref_member=2, age=11),
              member(14, person("Ирина"), CensusRole.WIFE, ref_member=4, age=48),
              member(15, person("Ирина", comment="дочь Ивана Иванова"), CensusRole.DAUGHTER, ref_member=4, age=16),
              member(16, person("Гликерія"), CensusRole.DAUGHTER, ref_member=4, age=6),
              member(17, person("Прасковья"), CensusRole.WIFE, ref_member=5, age=25),
              member(18, person("Елена"), CensusRole.WIFE, ref_member=8, age=22)),
          ),
    # Семья № 532 — Мальчиковы (Григорий Иванов)
    *page("202",
    household("532",
              member(1, person("Григорій", "Ивановъ", "Мальчиковъ"), CensusRole.HEAD,
                     age=55, previous_age=37),
              member(2, person("Емельянъ"), CensusRole.SON, age=39, previous_age=21),
              member(3, person("Емельянъ"), CensusRole.SON, ref_member=2, age=13),
              member(4, person("Димитрій"), CensusRole.SON, ref_member=2, age=10),
              member(5, person("Семенъ"), CensusRole.SON, ref_member=2, age=8),
              member(6, person("Евдокимъ"), CensusRole.SON, ref_member=2, age=1),
              member(7, person("Анисья"), CensusRole.WIFE, age=58),
              member(8, person("Агрипина"), CensusRole.WIFE, ref_member=2, age=40),
              member(9, person("Феодора"), CensusRole.DAUGHTER, ref_member=2, age=15)),
          ),
    # Семья № 533 — Мальчиковы (Андриан Григорьев)
    # Казьма Андрианов (1й) и Казьма другой (2й) — два разных сына с одинаковым именем.
    *page("203",
    household("533",
              member(1, person("Андреянъ", "Григорьевъ", "Мальчиковъ"), CensusRole.HEAD,
                     age=32, previous_age=14),
              member(2, person("Казма"), CensusRole.SON, age=11),
              member(3, person("Казма", comment="2й (другой)"), CensusRole.SON, age=9),
              member(4, person("Михаилъ"), CensusRole.SON, age="полгода"),
              member(5, person("Варвара"), CensusRole.WIFE, age=35),
              member(6, person("Устинья"), CensusRole.DAUGHTER, age=6),
              member(7, person("Феодосья"), CensusRole.DAUGHTER, age=3)),
    # Семья № 534 — Мальчиковы (Аким Григорьев)
    household("534",
              member(1, person("Акимъ", "Григорьевъ", "Мальчиковъ"), CensusRole.HEAD, age=27, previous_age=9),
              member(2, person("Петръ"), CensusRole.SON, age="2 мес"),
              member(3, person("Петръ", "Григорьевъ", "Мальчиковъ"), CensusRole.BROTHER, age=23, previous_age=5),
              member(4, person("Катерина"), CensusRole.WIFE, age=28),
              member(5, person("Аксинья"), CensusRole.WIFE, ref_member=3, age=25)),
          ),
    # Семья № 553 — Мальчиковы (Герасим Сидоров Федоров/Мальчиков)
    # Семен Герасимов отдан в рекруты в 1833.
    # Марья (жена Семена) и её дочери остались в хозяйстве (солдатка).
    # Евсей Федоров с сыновьями выбыли в Саратовскую губ в 1831 — не включены.
    # Марья Иванова — мать Герасима (78 лет);
    # л. 208об–209 (альбом «1834 РС 8 (ГАТО 12-1-1377)», кадр210 — сверено по скану 23.09.2026).
    *page("209",
    household("553",
              member(1, person("Герасимъ", "Сидоровъ", "Мальчиковъ", comment="отчество в МК также Федоров"),
                     CensusRole.HEAD, age=48, previous_age=30),
              member(2, person("Василій"), CensusRole.SON, age=31, previous_age=13),
              member(3, person("Андрей"), CensusRole.SON, ref_member=2, age=15),
              member(4, person("Карпъ"), CensusRole.SON, ref_member=2, age=4),
              member(5, person("Семенъ"), CensusRole.SON, previous_age=7, departure_year=1833, departure_reason="отдан в рекруты"),
              member(6, person("Іона"), CensusRole.SON, age=19, previous_age=1),
              member(7, person("Евсей", "Федоровъ"), CensusRole.BROTHER,
                     previous_age=25, departure_year=1831, departure_reason="выбыл", destination="Саратовская губерния"),
              member(8, person("Евсигней"), CensusRole.SON, ref_member=7,
                     previous_age=6, departure_year=1831, departure_reason="выбыл", destination="Саратовская губерния"),
              member(9, person("Архипъ"), CensusRole.SON, ref_member=7,
                     previous_age=2, departure_year=1831, departure_reason="выбыл", destination="Саратовская губерния"),
              member(10, person("Марья", "Иванова", comment="мать Герасима Сидорова, 78 лет"), CensusRole.MOTHER, age=78),
              member(11, person("Катерина"), CensusRole.WIFE, age=58),
              member(12, person("Ирина"), CensusRole.DAUGHTER, age=22),
              member(13, person("Февронія"), CensusRole.DAUGHTER, age=15),
              member(14, person("Устинья"), CensusRole.WIFE, ref_member=2, age=35),
              member(15, person("Лукерья", comment="дочь Василия"), CensusRole.DAUGHTER, ref_member=2, age=12),
              member(16, person("Катерина", comment="дочь Василия"), CensusRole.DAUGHTER, ref_member=2, age=6),
              member(17, person("Марья", comment="дочь Василия"), CensusRole.DAUGHTER, ref_member=2, age=5),
              member(18, person("Марья"), CensusRole.WIFE, ref_member=5, age=30),
              member(19, person("Авдотья"), CensusRole.DAUGHTER, ref_member=5, age=5),
              member(20, person("Пелагея"), CensusRole.DAUGHTER, ref_member=5, age=3)),
            ),
    defaults=RecordDefaults(
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE,
    ),
    prev_revision_year=1816,
    record_day=28,
    record_month=Month.FEBRUARY,
)
