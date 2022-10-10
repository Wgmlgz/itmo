package com.wgmlgz.pokemons;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.attacks.*;

public class Bellsprout extends Pokemon {
  public Bellsprout(String name, int level) {
    super(name, level);
    setStats(49, 55, 42, 42, 37, 85);
    setType(Type.GRASS, Type.POISON);
    setMove(new SludgeBomb(), new SleepPowder());
  }
}