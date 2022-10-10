package com.wgmlgz.pokemons;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.attacks.*;

public class Weepinbell extends Pokemon {
  public Weepinbell(String name, int level) {
    super(name, level);
    setStats(49, 55, 42, 42, 37, 85);
    setType(Type.NORMAL);
    setMove(new SludgeBomb(), new SleepPowder(), new Acid());
  }
}