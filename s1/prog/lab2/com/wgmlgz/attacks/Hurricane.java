package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class Hurricane extends SpecialMove {
  public Hurricane() {
    super(Type.FLYING, 110, 70);
  }

  @Override
  protected void applySelfEffects(Pokemon p) {
    Effect e = new Effect().chance(0.3);
    e.confuse(p);
    p.addEffect(e);
  }

  @Override
  protected String describe() {
    return "uses Hurricane";
  }
}