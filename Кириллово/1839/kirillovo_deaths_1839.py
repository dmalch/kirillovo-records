from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON, ZHONKA)

kirillovo_deaths_1839 = death_records(
    "ЦГАРМ",
    "57",
    "6",
    "192",
    "Кириллово",
    "Казанская церковь",
    1839,
    *page(
        "?",
        *death_month(
            Month.AUGUST, death(31, Gender.FEMALE, 9, None, deceased=person("Евдокия", "Герасимова", last_name_orig="Мальчикова", status="женка вдова"), age=70, cause_of_death=NATURAL)
        ),
        *death_month(
            Month.SEPTEMBER,
            death(
                47,
                Gender.FEMALE,
                14,
                15,
                deceased=person("Евдокия"),
                age=1,
                relatives=[relative(person("Карп", "Антонов", last_name_orig="Янин"), Relationship.FATHER)],
                cause_of_death=COLIC,
            ),
        ),
    ),
    # Дописано при сплошном проходе по скану (альбом «1839 (ЦГАРМ 57-6-192)», pk 1301; листы — по
    # кадру от проверенных л. 413 и 444) — записи первой волны (Мальчиковы/Янины), которых не было
    # в импорте из таблицы. В Гоголевом Бору писец (иерей Александр Халев) пишет «Юнинъ»: Янины ли
    # это — не установлено; в 1845 тот же писец пишет «Юлинъ» (Ефимъ Ерасимовъ, Анна Трофимова) — вероятно, Юлины, не Янины (Ефремовичи, Дмитриевичи, Трофим в families/Янины.md не известны)
    *page("444об",
          *death_month(Month.FEBRUARY,
                       death(1, Gender.MALE, 5, 13,
                             deceased=person("Ерасимъ", "Дмитріевъ", "Юнинъ", residence="Гоголев Бор", comment="так в подлиннике; вероятно, Юлин (1845: ГБ «Юлинъ»), не Янин"), age=60,
                             reviewed=False),
                       ),
          ),
    *page("461об",
          *death_month(Month.SEPTEMBER,
                       # ср. восприемницу 1838 м. №92 «Параскева Иванова Юнина» из Гоголева Бора
                       death(50, Gender.FEMALE, 17, 19,
                             deceased=person("Прасковья", "Иванова", "Юнина", status=ZHONKA, residence="Гоголев Бор", comment="так в подлиннике; вероятно, Юлина (1845: ГБ «Юлинъ»), не Янина"), age=45,
                             reviewed=False),
                       ),
          ),
    # Вторая волна (07.11.2026): дети замужних дочерей Мальчиковых и Яниных, найденные по имени мужа
    *page("464об",
          *death_month(Month.OCTOBER,
                       # мать — Анна Михайловна Янина (брак 1832 №21 с Александром Трофимовичем Калягиным)
                       death(55, Gender.FEMALE, 22, 23,
                             deceased=person("Дарья", status=PEASANT_DAUGHTER), age=3,
                             relatives=[relative(person("Александръ", "Трофимовъ", "Калягинъ"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             comment="погребалъ іерей Александръ Халевъ; кадр 78 альбома",
                             reviewed=False),
                       ),
          ),
    *page("467об",
          *death_month(Month.DECEMBER,
                       death(56, Gender.MALE, 4, 5,
                             deceased=person("Гавріилъ", status=PEASANT_SON, residence="Гоголев Бор"), age=11,
                             relatives=[relative(person("Трофимъ", last_name_orig="Юнинъ", comment="отчество не записано; так в подлиннике; вероятно, Юлин (1845: ГБ «Юлинъ»), не Янин"), Relationship.FATHER)],
                             cause_of_death=DIARRHEA,
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
