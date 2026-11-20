from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import DROPSY
from verso.ru.dsl.statuses import PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_WIFE

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-574, альбом
# Photos «1916 (ГАПО 182-5-574)» (pk 1251), ч. 3 — л. 289 шмуцтитул, лл. 289об–317об (м. №1–67, ж. №1–48), прочитана
# целиком 26.10.2026; импорта не было. Л. 310об — вшитый лист другого причта (свящ. Алексей Антонов, диакон Евгений Орлов):
# там 23.04 погребён «Аѳанасія Козмина Мальчикова сынъ Николай» — не Казанская, не взят. Погребали свящ. Николай
# Расказовский и Григорий Феодоровский.
kirillovo_deaths_1916 = death_records(
    "ГАПО",
    "182",
    "5",
    "574",
    "Кириллово",
    "Казанская церковь",
    1916,
    *death_month(Month.JANUARY,
                 # Елена Арсеньевна?, жена Павла Егоровича «Кистенева»
                 death(2, Gender.FEMALE, None, 1,
                       deceased=person("Елена", "Арсеньева", status=PEASANT_WIFE, comment="отчество читается неуверенно"),
                       relatives=[relative(person("Павелъ", "Егоровъ", "Кистеневъ"), Relationship.HUSBAND)],
                       comment="умерла 30.12.1915, погребена 1.01.1916; возраст у края",
                       page="289об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Пелагия, дочь Федора Герасимовича Мальчикова, р. 11.10.1916 (рожд. ж. №58)
                 death(45, Gender.FEMALE, 17, 18,
                       deceased=person("Пелагія", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Ѳеодоръ", "Герасимовъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="возраст у края",
                       page="314об",
                       reviewed=False),
                 ),
    *death_month(Month.DECEMBER,
                 # Степан Васильевич «Юлинъ» (рядовой, жена Матрона Феодосиевна, 1888)
                 death(65, Gender.MALE, 16, 17,
                       deceased=person("Стефанъ", "Васильевъ", "Юлинъ"),
                       age=54,
                       comment="возраст «54» читается неуверенно",
                       page="316об",
                       reviewed=False),
                 # Николай «Кондратьевич»? «Кистенев» — Николай Константинович Малахаев/Кистенев?
                 death(66, Gender.MALE, 17, 18,
                       deceased=person("Николай", "Кондратьевъ", "Кистеневъ", comment="отчество читается неуверенно («Конд…тиевъ»); он же: Николай Константинович Малахаев/Кистенев, отец Андрея, Ивана, Параскевы Николаевичей? не установлено"),
                       age=75, cause_of_death=DROPSY,
                       page="317об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
