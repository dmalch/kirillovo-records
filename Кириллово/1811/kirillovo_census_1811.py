from verso.ru.dsl import (CensusRole, Month, RecordDefaults, census_records, household, member,
                          page, person)
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE

# РС 6 (Шестая ревизия) 1811 года, с. Успенское (Кириллово)
# Архив: ГАТО, ф. 12 оп. 1 д. 439 — «Ревизские сказки Спасского уезда за 1811 год, ч. 2»;
# с. Успенское (Кириллово) занимает лл. 171–222 (по машинописному реестру дела).
# Ревизия мужская: женщин в форме нет. Левая цифра — возраст по ревизии 1795 года,
# правая — налицо в 1811; разница ровно 16 лет.
census = census_records(
    "ГАТО",
    "12",
    "1",
    "439",
    "Кириллово",
    1811,
    # Двор № 139 (лл. 185–185об.) — Трифоновы, предки линии Дениса Петрова.
    # Глава Трифон Агапов умер в 1810 — совпадает с МК Кириллово, смерть № 25 от
    # 16.11.1810 («Трифонъ Агаповъ, 73 года»), и по метрикам он же восприемник
    # с 1760 и отец в 1784/1786/1789.
    # Двор прослеживается дальше: в РС 8 1834 Тимофей — семья № 301, Никита и
    # Лаврентий — семья № 302 (оба выбыли в Саратовскую губернию в 1831),
    # Лазарь Григорьев записан главой семьи № 301 и выбыл туда же в 1830.
    *page("185",
    household("139",
              member(1, person("Трифонъ", "Агаповъ"), CensusRole.HEAD,
                     previous_age=50, departure_year=1810, departure_reason="умер"),
              member(2, person("Григорій"), CensusRole.SON, age=48, previous_age=32),
              member(3, person("Тимофей"), CensusRole.SON, age=37, previous_age=21),
              member(4, person("Никита"), CensusRole.SON, age=33, previous_age=17),
              member(5, person("Лаврентей"), CensusRole.SON, age=24, previous_age=8),
              member(6, person("Лазарь"), CensusRole.SON, ref_member=2, age=19, previous_age=3),
              member(7, person("Петръ"), CensusRole.SON, ref_member=3, age="году"),
              member(8, person("Иван"), CensusRole.SON, ref_member=4, age="году")),
          ),
    # Дворы 439 и 440 (л. 216) — Мальчиковы. Фамилия в 1811 году в подворных
    # записях не пишется: она выписана один раз, в заверительной части дела
    # (л. 222), у выборного «Герасимъ Ѳедосѣевъ Мальчиковъ». Привязка к РС 8
    # 1834 — по именам и возрастам, расхождение везде не больше года.
    *page("216",
    # Двор 439 — братья Дмитрей и Павелъ, в подлиннике объединены скобкой
    # «Дмитрей ⎫ Давыдовы дети / Павелъ ⎬». Их отец Давыдъ Ѳедосѣевъ умер
    # в 1791 (МК Кириллово, смерть № 4), то есть до ревизии 1795, и потому
    # в сказку не попал вовсе.
    # В РС 8 1834 Дмитрей — глава семьи 523, Павелъ — семьи 524.
    household("439",
              member(1, person("Дмитрей", "Давыдовъ"), CensusRole.HEAD, age=39, previous_age=23),
              member(2, person("Павелъ", "Давыдовъ"), CensusRole.BROTHER, age=37, previous_age=21),
              member(3, person("Нестеръ"), CensusRole.SON, ref_member=1, age=13),
              member(4, person("Василей"), CensusRole.SON, ref_member=1, age=10),
              member(5, person("Михаила"), CensusRole.SON, ref_member=2, age=12),
              member(6, person("Архипъ"), CensusRole.SON, ref_member=2, age=4)),
    # Двор 440 — Иванъ Ѳедосѣевъ, родной брат Давыда из двора 439.
    # В РС 8 1834 он глава семьи 525; его сын Григорей — семьи 532,
    # а внуки Андреянъ и Акимъ — семей 533 и 534.
    household("440",
              member(1, person("Иванъ", "Федосеевъ"), CensusRole.HEAD, age=55, previous_age=40),
              member(2, person("Григорей"), CensusRole.SON, age=33, previous_age=17),
              member(3, person("Андрей"), CensusRole.SON, age=30, previous_age=14),
              member(4, person("Максимъ"), CensusRole.SON, age=26, previous_age=10),
              member(5, person("Иванъ"), CensusRole.SON, age=16, previous_age="полгоду"),
              member(6, person("Емельянъ"), CensusRole.SON, ref_member=2, age=16),
              member(7, person("Андреянъ"), CensusRole.SON, ref_member=2, age=10),
              member(8, person("Акимъ"), CensusRole.SON, ref_member=2, age=5),
              member(9, person("Петръ"), CensusRole.SON, ref_member=2, age="году"),
              member(10, person("Дмитрей"), CensusRole.SON, ref_member=3, age=2)),
            ),
    # Двор 468 (лл. 219–219об.) — третья ветвь Мальчиковых: Ѳедоръ, брат Ивана
    # (двор 440) и Давыда. Здесь же назван их общий отец — Ѳедосѣй Петровъ,
    # корень рода, 70 лет по ревизии 1795, то есть около 1725 года рождения.
    # Его внук Герасимъ Ѳедоровъ — глава семьи 553 в РС 8 1834, где записан
    # «Герасимъ Сидоровъ Мальчиковъ» (отчество в МК тоже Федоров).
    # Ветвь Евсея прослеживается до РС 9 1850, двор 431.
    # Колонка возрастов 1811 года на этом листе уходит в тень корешка и не
    # читается — записаны только возрасты по ревизии 1795.
    *page("219",
    household("468",
              member(1, person("Федосей", "Петровъ"), CensusRole.HEAD, previous_age=70, departure_year=1803, departure_reason="умер"),
              member(2, person("Федоръ"), CensusRole.SON, previous_age=36, departure_year=1808, departure_reason="умер"),
              member(3, person("Герасимъ"), CensusRole.SON, ref_member=2, age=26, previous_age=10),
              member(4, person("Евсей"), CensusRole.SON, ref_member=2, age=21, previous_age=5),
              member(5, person("Лаврентей"), CensusRole.SON, ref_member=2, age=17, previous_age="по году"),
              member(6, person("Василей"), CensusRole.SON, ref_member=3, age=9),
              member(7, person("Семенъ"), CensusRole.SON, ref_member=3, age=3),
              member(8, person("Евсегней"), CensusRole.SON, ref_member=4, age=2)),
            ),
    defaults=RecordDefaults(
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE,
    ),
    prev_revision_year=1795,
    record_month=Month.SEPTEMBER,
)
