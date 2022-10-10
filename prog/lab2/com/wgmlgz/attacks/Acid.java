package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class Acid extends SpecialMove {
  public Acid() {
    super(Type.POISON, 40, 100);
  }

  @Override
  protected void applyOppEffects(Pokemon p) {
    p.addEffect(new Effect().chance(0.1).stat(Stat.SPECIAL_DEFENSE, -1));
  }

  @Override
  protected String describe() {
    return "uses Acid";
  }
}