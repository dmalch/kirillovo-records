from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL, SMALLPOX
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER

# Выборка первой волны: записи, где есть (или считались) Мальчиковы или Янины. Ч. 3 — лл. 19–24об по
# нумерации книги и два подшитых листа без номера (архивные 531–532), осенняя оспа 1827 г.
kirillovo_deaths_1827 = death_records(
    "ЦГА республики Мордовия", "57", "6", "124", "Кириллово", "Казанская",
    1827,
    *page("26",
          *death_month(Month.DECEMBER,
                       # Елена Григорьевна, рожд. 20.05.1827 (рождение №59); отец — Григорий Иванович Широков, не Мальчиков
                       # (см. 1832 ж. №79)
                       death(76, Gender.FEMALE, 14, None,
                             deceased=person("Елена", status=PEASANT_DAUGHTER), age="6 мес",
                             relatives=[relative(person("Григорій", "Ивановъ"), Relationship.FATHER)],
                             cause_of_death=SMALLPOX,
                             comment="лист без номера книги (архивный 531); возраст в подлиннике «полугоду»",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=ECON_PEASANT_MALE,
        status_female=ECON_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
