% Факты с одним аргументом

% Персонажи
character(v).
character(johnny_silverhand).
character(jackie_welles).
character(judy_alvarez).
character(panam_palmer).
character(evelyn_parker).
character(rogue_amendiares).
character(takamura).
character(alt_cunningham).
character(dexter_deshawn).
character(placide).
character(meredith_stout).
character(viktor_vector).
character(saburo_arasaka).
character(yorinobu_arasaka).
character(hanako_arasaka).
character(tyger_claws_member).
character(mox_member).
character(valentino_member).
character(sixth_street_member).
character(campo_orta).

% Локации
location(night_city).
location(pacifica).
location(watson).
location(westbrook).
location(santo_domingo).
location(heywood).
location(city_center).
location(badlands).
location(afterlife).

% Банды
gang(tyger_claws).
gang(moxes).
gang(valentinos).
gang(sixth_street).
gang(aldecaldos).

% Корпорации
corporation(arasaka).
corporation(militech).
corporation(kang_tao).

% Оружие
weapon(smart_pistol).
weapon(power_revolver).
weapon(tech_sniper_rifle).
weapon(smart_rifle).

% Технологические виды оружия
tech_weapon(tech_sniper_rifle).

% Смарт-оружие
smart_weapon(smart_pistol).
smart_weapon(smart_rifle).

% Факты с двумя аргументами

% Персонажи и их местоположение
is_in(v, night_city).
is_in(johnny_silverhand, night_city).
is_in(jackie_welles, night_city).
is_in(panam_palmer, badlands).
is_in(saburo_arasaka, night_city).
is_in(yorinobu_arasaka, night_city).
is_in(hanako_arasaka, night_city).

% Отношения между персонажами
friend_of(v, johnny_silverhand).
friend_of(v, jackie_welles).
friend_of(v, judy_alvarez).
friend_of(v, panam_palmer).
enemy_of(v, arasaka).

% Члены банд и корпораций
member_of(judy_alvarez, moxes).
member_of(panam_palmer, aldecaldos).
member_of(campo_orta, sixth_street).
works_for(saburo_arasaka, arasaka).
works_for(yorinobu_arasaka, arasaka).
works_for(hanako_arasaka, arasaka).
works_for(meredith_stout, militech).

% Использование оружия
uses_weapon(v, smart_pistol).
uses_weapon(jackie_welles, power_revolver).
uses_weapon(panam_palmer, tech_sniper_rifle).

% Семейные связи
father_of(saburo_arasaka, yorinobu_arasaka).
father_of(saburo_arasaka, hanako_arasaka).
sibling(yorinobu_arasaka, hanako_arasaka).

% Доктор и пациент
doctor_of(viktor_vector, v).

% Правила

% Персонаж X является союзником персонажа Y, если они друзья или работают вместе
ally(X, Y) :- friend_of(X, Y); works_with(X, Y).

% Персонаж X является врагом персонажа Y, если они враги или работают против друг друга
enemy(X, Y) :- enemy_of(X, Y); works_against(X, Y).

% Персонаж X находится в Найт-Сити, если он там находится или работает на организацию, базирующуюся в Найт-Сити
located_in(X, night_city) :-
    is_in(X, night_city);
    works_for(X, _),
    is_in(X, night_city).

% Персонаж X опасен, если он член опасной банды
dangerous(X) :-
    member_of(X, tyger_claws);
    member_of(X, valentinos);
    member_of(X, sixth_street).

% Персонаж X использует технологическое оружие
uses_tech_weapon(X) :-
    uses_weapon(X, W),
    tech_weapon(W).

% Персонаж X использует смарт-оружие
uses_smart_weapon(X) :-
    uses_weapon(X, W),
    smart_weapon(W).
