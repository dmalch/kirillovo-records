from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, DIARRHEA, MEASLES, NATURAL
from verso.ru.dsl.statuses import (ECON_PEASANT_FEMALE, ECON_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON, SOLDIER_WIFE)

kirillovo_deaths_1841 = death_records(
    "ЦГАРМ",
    "57",
    "6",
    "217",
    "Кириллово",
    "Казанская церковь",
    1841,
    *page(
        "?",
        *death_month(Month.MAY, death(14, Gender.MALE, 10, None, deceased=person("Григорий", "Иванов", last_name_orig="Мальчиков"), age=70, cause_of_death=NATURAL)),
        *death_month(
            Month.JUNE,
            death(
                32,
                Gender.MALE,
                28,
                None,
                deceased=person("Иван", "Егоров", last_name_orig="Янин"),
                age="2 мес",
                relatives=[relative(person("Егор", "Денисов", last_name_orig="Янин"), Relationship.FATHER)],
                cause_of_death=MEASLES,
            ),
        ),
        *death_month(
            Month.JULY,
            death(
                38,
                Gender.MALE,
                17,
                None,
                deceased=person("Егор", "Ионов", last_name_orig="Мальчиков"),
                age=2 / 12,
                relatives=[relative(person("Ион", "Герасимов", last_name_orig="Мальчиков"), Relationship.FATHER)],
                cause_of_death=COLIC,
            ),

            death(
                37,
                Gender.MALE,
                11,
                None,
                deceased=person("Федор"),
                age=1,
                relatives=[relative(person("Марк", "Алексеев", last_name_orig="Янин", residence="д. Гоголев Бор"), None)],
                cause_of_death=COLIC,
            ),
        ),
        *death_month(Month.DECEMBER, death(86, Gender.MALE, 14, 16, deceased=person("Михаил", "Павлов", last_name_orig="Мальчиков"), age=40, cause_of_death=NATURAL)),
    ),
    # Дописано при сплошном проходе по скану (альбом «1841 (ЦГАРМ 57-6-217)», pk 1323; листы по архивной
    # нумерации на кадрах не видны — «?», как в импорте; в comment — кадр альбома) — записи первой волны
    # (Мальчиковы/Янины), которых не было в импорте из таблицы
    *page("?",
          *death_month(Month.MAY,
                       # Климент — сын Ефима (здесь «Ефрема») Алексеевича Киселева и Федоры (Варвары) Емельяновны
                       # Мальчиковой, род. 28.02.1840 (рожд. м. №15)
                       death(16, Gender.MALE, 23, 25,
                             deceased=person("Климентъ", status=PEASANT_SON), age=1,
                             relatives=[relative(person("Ефремъ", "Алексѣевъ", "Киселевъ"), Relationship.FATHER)],
                             cause_of_death=MEASLES,
                             comment="возраст «году»; кадр 58 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.JUNE,
                       # мать — Акилина Павловна Мальчикова (брак 1835 №3); их сын Иван умер в 1837
                       death(26, Gender.MALE, 23, 25,
                             deceased=person("Ѳеодоръ", status=PEASANT_SON), age=2,
                             relatives=[relative(person("Семенъ", "Агаповъ", "Крапивниковъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="кадр 61 альбома",
                             reviewed=False),
                       # солдатка Екатерина Григорьевна — вероятно, жена Акима Григорьевича Мальчикова, отданного
                       # в солдаты (1838 рожд. м. №88 — их сын Трофим, отец «отданный в солдаты»)
                       death(27, Gender.MALE, 24, 26,
                             deceased=person("Трофимъ", status=PEASANT_SON), age=3,
                             relatives=[relative(person("Екатерина", "Григорьева", status=SOLDIER_WIFE), Relationship.MOTHER)],
                             cause_of_death=MEASLES,
                             comment="кадр 61 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.JULY,
                       # Ефим — сын Федора Антоновича Янина, род. 28.01.1841 (рожд. м. №8); фамилия здесь «Зенинъ»
                       death(33, Gender.MALE, 2, 4,
                             deceased=person("Ефимъ", status=PEASANT_SON), age=0.5,
                             relatives=[relative(person("Ѳеодоръ", "Антоновъ", "Зенинъ", comment="так в подлиннике; Янин"), Relationship.FATHER)],
                             cause_of_death=MEASLES,
                             comment="кадр 64 альбома",
                             reviewed=False),
                       # Агафья — дочь Якова Максимовича «Познякова» (Мальчикова по роду), род. 11.02.1837
                       # (рожд. ж. №17, восприемник Аким Григорьевич Мальчиков)
                       death(32, Gender.FEMALE, 10, 12,
                             deceased=person("Агафья", status=PEASANT_DAUGHTER), age=4,
                             relatives=[relative(person("Яковъ", "Максимовъ", "Позняковъ"), Relationship.FATHER)],
                             cause_of_death=MEASLES,
                             comment="кадр 65 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.SEPTEMBER,
                       # отец Алексеевичей Яниных из Гоголева Бора (Марк, Родион, Иван, Андрей, София)
                       death(79, Gender.MALE, 27, 29,
                             deceased=person("Алексѣй", "Ѳедоровъ", "Янинъ", residence="Гоголев Бор"), age=66,
                             cause_of_death=NATURAL,
                             comment="кадр 78 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.OCTOBER,
                       # мать — та же солдатка Екатерина Григорьевна, что и у Трофима (смерть м. №27)
                       death(63, Gender.FEMALE, 10, 12,
                             deceased=person("Матрона", status=PEASANT_DAUGHTER), age=15,
                             relatives=[relative(person("Екатерина", "Григорьева", status=SOLDIER_WIFE), Relationship.MOTHER)],
                             cause_of_death=DIARRHEA,
                             comment="«отъ поносной»; кадр 79 альбома",
                             reviewed=False),
                       ),
          *death_month(Month.NOVEMBER,
                       # Михаил — сын Лукьяна Михайловича Янина, род. 1.11.1838 (рожд. м. №109)
                       death(85, Gender.MALE, 18, 20,
                             deceased=person("Михаилъ", status=PEASANT_SON),
                             relatives=[relative(person("Лукьянъ", "Михайловъ", "Янинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="возраст «…году», цифра закрыта подписью; кадр 81 альбома",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(residence="Кириллово", status_male=ECON_PEASANT_MALE, status_female=ECON_PEASANT_FEMALE),
)
