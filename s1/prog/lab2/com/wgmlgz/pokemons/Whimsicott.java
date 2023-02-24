package com.wgmlgz.pokemons;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.attacks.*;

public class Whimsicott extends Cottonee {
  public Whimsicott(String name, int level) {
    super(name, level);
    setStats(60, 67, 85, 77, 75, 116);
    addMove(new Hurricane());
  }
}