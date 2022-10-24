package com.wgmlgz.pokemons;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.attacks.*;

public class Cottonee extends Pokemon {
  public Cottonee(String name, int level) {
    super(name, level);
    setStats(40, 27, 60, 37, 50, 66);
    setType(Type.GRASS, Type.FAIRY);
    setMove(new EnergyBall(), new DreamEater());
  }
}