package com.wgmlgz.pokemons;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.attacks.*;

public class Bruxish extends Pokemon {
  public Bruxish(String name, int level) {
    super(name, level);
    setStats(49, 55, 42, 42, 37, 85);
    setType(Type.NORMAL);
    setMove(new Slash(), new DarkPulse(), new HoneClaws(), new WillOWisp());
  }
}