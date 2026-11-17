from verso.ru.dsl import (Gender, Month, RecordDefaults, Relationship, death, death_month,
                          death_records, page, person, relative)
from verso.ru.dsl.causes_of_death import COLIC, NATURAL
from verso.ru.dsl.statuses import (KAZENNYJ_PEASANT_FEMALE, KAZENNYJ_PEASANT_MALE, PEASANT_DAUGHTER,
                                   PEASANT_SON)

# Выборка первой волны: только записи, где есть Мальчиковы или Янины. Альбом «1848 (ЦГАРМ 57-1-422)», pk 3619;
# ч. 3 — сканы 563–602, разворот л. (N−9)об–(N−8) по штампу. Летом 1848 — холера («эпидемическою холерою»).
kirillovo_deaths_1848 = death_records(
    "ЦГА республики Мордовия", "57", "1", "422", "Кириллово", "Казанская",
    1848,
    *page("576об",
          *death_month(Month.AUGUST,
                       # сын Андрея Васильевича Мальчикова. Возраст «2» без единицы: если это близнец Ефим (рожд.
                       # 24.04.1848, м. №37), ему не было и четырёх месяцев — младенцам писец обычно ставит
                       # «недель»/«мес», так что это может быть и старший Ефим; не сведено
                       death(57, Gender.MALE, 13, 15,
                             deceased=person("Ефимъ", status=PEASANT_SON), age=2,
                             relatives=[relative(person("Андрей", "Васильевъ", "Мальчиковъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="скан 585",
                             reviewed=False),
                       # Николай Павлович Мальчиков (сын Павла Давыдовича); Евдокия Денисовна — дочь Дениса Егоровича
                       # Янина? (его жена Анна Ивановна умерла от холеры через два дня, смерть ж. №73)
                       death(66, Gender.FEMALE, 13, 15,
                             deceased=person("Евдокія", "Денисова"), age=25,
                             relatives=[relative(person("Николай", "Павловъ", "Мальчиковъ"), Relationship.HUSBAND)],
                             cause_of_death="эпидемическая холера",
                             comment="«эпидимическою холерою»; скан 585",
                             reviewed=False),
                       ),
          ),
    *page("578об",
          *death_month(Month.AUGUST,
                       # Денис Егорович Янин; книга зовёт Денисовичей и «Хрипуновы», и «Сырцовы»
                       death(73, Gender.FEMALE, 15, 17,
                             deceased=person("Анна", "Иванова"), age=60,
                             relatives=[relative(person("Денисъ", "Егоровъ", "Хрипуновъ", comment="так в подлиннике; Денис Егорович Янин"), Relationship.HUSBAND)],
                             cause_of_death="эпидемическая холера",
                             comment="скан 587",
                             reviewed=False),
                       ),
          ),
    *page("579об",
          *death_month(Month.AUGUST,
                       # Настасья Андреевна Мальчикова; вдовец женился вторично 6.10.1848 (брак №25)
                       death(76, Gender.FEMALE, 17, 19,
                             deceased=person("Настасія", "Андреева"), age=34,
                             relatives=[relative(person("Константинъ", "Козьминъ", "Мальчиковъ", comment="в подлиннике «Казьминъ»"), Relationship.HUSBAND)],
                             cause_of_death="эпидемическая холера",
                             comment="причина вписана поперёк графы, читается «эпид…» — холера; скан 588 (в прежнем альбоме Photos его не было)",
                             reviewed=False),
                       ),
          ),
    *page("583об",
          *death_month(Month.SEPTEMBER,
                       # София — дочь Козьмы Андреяновича Мальчикова, род. 20.08.1848 (рожд. ж. №58)
                       death(93, Gender.FEMALE, 5, 7,
                             deceased=person("Софія", status=PEASANT_DAUGHTER), age="2 нед",
                             relatives=[relative(person("Козьма", "Андреяновъ", "Мальчиковъ", comment="в подлиннике «Казьма»"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="скан 592",
                             reviewed=False),
                       ),
          ),
    # Вторая волна (07.11.2026): дети дочерей Мальчиковых и Яниных, найдены поиском фамилий мужей по OCR Яндекс.Архива и
    # прочитаны по оригиналам
    *page("?",
          *death_month(Month.MARCH,
                       # мать — Феврония Герасимовна Мальчикова, вдова Ефима Ивановича Лапшина (брак 1843 №19), вторым браком
                       # за Алексеем Емельяновичем (брак 1844 №18)
                       death(5, Gender.MALE, 20, 22,
                             deceased=person("Казьма", status=PEASANT_SON), age=0.5,
                             relatives=[relative(person("Алексѣй", "Емельяновъ", "Пишкинъ"), Relationship.FATHER)],
                             cause_of_death=COLIC,
                             comment="скан 566; возрастъ «полугоду»; погребалъ іерей Іоаннъ Реморовъ",
                             reviewed=False),
                       ),
          ),
    defaults=RecordDefaults(
        residence="Кириллово",
        status_male=KAZENNYJ_PEASANT_MALE,
        status_female=KAZENNYJ_PEASANT_FEMALE,
        cause_of_death=NATURAL
    ),
)
