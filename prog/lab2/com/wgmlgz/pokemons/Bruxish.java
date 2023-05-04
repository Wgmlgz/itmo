package com.wgmlgz.pokemons;

import ru.ifmo.se.pokemon.*;
import com.wgmlgz.attacks.*;

public class Bruxish extends Pokemon {
  public Bruxish(String name, int level) {
    super(name, level);
    setStats(68, 105, 70, 70, 70, 92);
    setType(Type.WATER, Type.PSYCHIC);
    setMove(new Slash(), new DarkPulse(), new HoneClaws(), new WillOWisp());
  }
}