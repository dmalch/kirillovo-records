from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import NATURAL, PLEURISY
from verso.ru.dsl.statuses import ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_SON

# SELECTIVE EXTRACT: Only Янин-family related entries from 1840 metric book.

kirillovo_deaths_1840 = death_records(
    "ЦГАРМ",
    "57",
    "6",
    "200",
    "Кириллово",
    "Казанская церковь",
    1840,
    *page(
        "?",
        *death_month(
            Month.MARCH,
            death(
                12,
                Gender.MALE,
                29,
                0,
                deceased=person("Иосиф"),
                age=1,
                relatives=[relative(person("Андрей", "Алексеев", last_name_orig="Янин", residence="д. Гоголев Бор"), Relationship.FATHER)],
                cause_of_death=PLEURISY,
            ),
        ),
    ),
    # Дописано при сплошном проходе по скану (альбом «1840 (ЦГАРМ 57-6-200)», pk 1321; листы — по штампам
    # кадров) — записи первой волны (Мальчиковы/Янины), которых не было в импорте из таблицы. С 1840 книга
    # пишет «казенный крестьянин»; статусы файла оставлены как в импорте. «Юнинъ» в Гоголевом Бору (Ефремовичи,
    # Ерасим Дмитриевич и сын его Трофим) — вероятно, Юлины (в 1845 «Юлинъ»), не Янины
    *page("617об",
          *death_month(Month.APRIL,
                       # отец — сын Ерасима Дмитриевича «Юнина» (ум. 1839, смерть м. №1); ср. 1839 смерть м. №56
                       death(24, Gender.MALE, 25, 26,
                             deceased=person("Иванъ", status=PEASANT_SON, residence="Гоголев Бор"), age=5,
                             relatives=[relative(person("Трофимъ", "Ерасимовъ", "Юнинъ", comment="так в подлиннике; вероятно, Юлин (1845: ГБ «Юлинъ»), не Янин"), Relationship.FATHER)],
                             cause_of_death="утонул",
                             comment="«отъ утопа»",
                             reviewed=False),
                       ),
          ),
    *page("621об",
          *death_month(Month.MAY,
                       # жена Вонифатия Ефремовича «Юнина» (брак 1839 №32), мать Евдокии (рожд. 1840 ж. №15)
                       death(15, Gender.FEMALE, 27, 29,
                             deceased=person("Ѳевронія", "Ѳетисова", "Юнина", residence="Гоголев Бор", comment="так в подлиннике; вероятно, Юлина (1845: ГБ «Юлинъ»), не Янина"), age=26,
                             cause_of_death=NATURAL,
                             reviewed=False),
                       ),
          ),
    *page("635об",
          *death_month(Month.NOVEMBER,
                       # Павел Давидович Мальчиков (РС 1834 № 524; РС 1850 — «умер 1840»)
                       death(55, Gender.MALE, 25, 27,
                             deceased=person("Павелъ", "Давыдовъ", "Мальчиковъ"), age=70,
                             cause_of_death=NATURAL,
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
