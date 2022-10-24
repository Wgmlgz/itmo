package com.wgmlgz;

import java.util.Random;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.pokemons.*;

class Lab2 {
  public static void main(String[] args) {
    var battle = new Battle();

    var bellsprout = new Bellsprout("Geralt of Rivia", 1);
    var bruxish = new Bruxish("Ciri", 1);
    var cottonee = new Cottonee("Yennefer of Vengerberg", 1);
    var victreebel = new Victreebel("Triss Merigold", 1);
    var weepinbell = new Weepinbell("Dandelion", 1);
    var whimsicott = new Whimsicott("Vesemir", 1);

    battle.addAlly(bellsprout);
    battle.addAlly(bruxish);
    battle.addAlly(cottonee);
    battle.addFoe(victreebel);
    battle.addFoe(weepinbell);
    battle.addFoe(whimsicott);

    battle.go();
  }
}
