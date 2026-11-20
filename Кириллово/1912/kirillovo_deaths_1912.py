from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, person, relative)
from verso.ru.dsl.causes_of_death import PARALYSIS, PNEUMONIA
from verso.ru.dsl.statuses import (PEASANT_DAUGHTER, PEASANT_FEMALE, PEASANT_MALE, PEASANT_SON,
                                   WIDOW)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины (и их родня по прозваниям). ГАПО 182-5-302, альбом
# Photos «1912 (ГАПО 182-5-302)» (pk 1281), ч. 3 — л. 287 шмуцтитул, лл. 287об–316об (70 муж. / 73 жен.), прочитана
# целиком 26.10.2026; импорта не было. Погребали свящ. Александр Васильев Писарев и Николай Расказовский.
kirillovo_deaths_1912 = death_records(
    "ГАПО",
    "182",
    "5",
    "302",
    "Кириллово",
    "Казанская церковь",
    1912,
    *death_month(Month.FEBRUARY,
                 # Матвей Яковлевич Мальчиков (унтер-офицер, жених 1868)
                 death(9, Gender.MALE, 15, 16,
                       deceased=person("Матѳей", "Яковлевъ", "Мальчиковъ"),
                       age=85, cause_of_death=PARALYSIS,
                       page="290об",
                       reviewed=False),
                 # Максим Емельянович Мальчиков — брат Степана Емельяновича (†1906)? отец Максимовичей «Дунаевых»?
                 death(11, Gender.MALE, 16, 17,
                       deceased=person("Максимъ", "Емельяновъ", "Мальчиковъ", comment="отец Максимовичей «Дунаевых» (Иван, Василий, Семен, Никифор, Николай)? не установлено"),
                       age=70, cause_of_death=PNEUMONIA,
                       page="290об",
                       reviewed=False),
                 ),
    *death_month(Month.OCTOBER,
                 # Петр, сын Стефана Степановича «Юлина», р. 24.06.1912 (рожд. м. №47)
                 death(57, Gender.MALE, 29, 30,
                       deceased=person("Петръ", status=PEASANT_SON),
                       relatives=[relative(person("Стефанъ", "Стефановъ", "Юлинъ"), Relationship.FATHER)],
                       age="5 мес",
                       page="309об",
                       reviewed=False),
                 ),
    *death_month(Month.NOVEMBER,
                 # Марфа, дочь Матвея Матвеевича Янина («Сырцовъ»)
                 death(56, Gender.FEMALE, 8, 9,
                       deceased=person("Марѳа", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Матѳей", "Матѳеевъ", "Сырцовъ", comment="он же: Матвей Матвеевич Янин"), Relationship.FATHER)],
                       comment="возраст у сгиба («6…»)",
                       page="310об",
                       reviewed=False),
                 # вдова Александра Семеновна «Юлина» — чья вдова, не установлено
                 death(61, Gender.FEMALE, 20, 21,
                       deceased=person("Александра", "Семенова", "Юлина", status=WIDOW, comment="чья вдова — не установлено"),
                       cause_of_death=PNEUMONIA,
                       comment="возраст у сгиба («8…»)",
                       page="311об",
                       reviewed=False),
                 ),
    *death_month(Month.DECEMBER,
                 # Екатерина, дочь Михаила Матвеевича Мальчикова, р. 19.11.1912 (рожд. ж. №88)
                 death(70, Gender.FEMALE, 23, 24,
                       deceased=person("Екатерина", status=PEASANT_DAUGHTER),
                       relatives=[relative(person("Михаилъ", "Матѳеевъ", "Мальчиковъ"), Relationship.FATHER)],
                       comment="возраст у сгиба",
                       page="314об",
                       reviewed=False),
                 ),
    defaults=RecordDefaults(residence="Кириллово", status_male=PEASANT_MALE, status_female=PEASANT_FEMALE),
)
