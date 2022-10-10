package com.wgmlgz.pokemons;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.attacks.*;

public class Cottonee extends Pokemon {
  public Cottonee(String name, int level) {
    super(name, level);
    setStats(49, 55, 42, 42, 37, 85);
    setType(Type.NORMAL);
    setMove(new EnergyBall(), new Rest(), new DreamEater());
  }
}