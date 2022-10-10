package com.wgmlgz;

import java.util.Random;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.pokemons.*;

class Lab2 {
  public static void main(String[] args) {
    Battle battle = new Battle();

    Bellsprout bellsprout = new Bellsprout("Geralt of Rivia", 1);
    Bruxish bruxish = new Bruxish("Ciri", 1);
    Cottonee cottonee = new Cottonee("Yennefer of Vengerberg", 1);
    Victreebel victreebel = new Victreebel("Triss Merigold", 1);
    Weepinbell weepinbell = new Weepinbell("Dandelion", 1);
    Whimsicott whimsicott = new Whimsicott("Vesemir", 1);

    battle.addAlly(bellsprout);
    battle.addAlly(bruxish);
    battle.addAlly(cottonee);
    battle.addFoe(victreebel);
    battle.addFoe(weepinbell);
    battle.addFoe(whimsicott);

    battle.go();
  }
}
