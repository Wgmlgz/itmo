package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class HoneClaws extends StatusMove {
  public HoneClaws() {
    super(Type.PSYCHIC, 0, 0);
  }

  @Override
  protected void applySelfEffects(Pokemon p) {
    p.addEffect(new Effect().stat(Stat.ATTACK, 1).stat(Stat.ACCURACY, 1));
  }

  @Override
  protected String describe() {
    return "uses HoneClaws";
  }
}