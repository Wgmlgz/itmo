package com.wgmlgz.pokemons;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.attacks.*;

public class Victreebel extends Weepinbell {
  public Victreebel(String name, int level) {
    super(name, level);
    setStats(80, 105, 65, 100, 70, 70);
    addMove(new EnergyBall());
  }
}