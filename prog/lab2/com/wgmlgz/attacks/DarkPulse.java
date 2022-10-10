package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class DarkPulse extends SpecialMove {
  public DarkPulse() {
    super(Type.DARK, 80, 100);
  }

  @Override
  protected void applyOppEffects(Pokemon p) {
    new Effect().chance(0.2).flinch(p);
  }

  @Override
  protected String describe() {
    return "uses DarkPulse";
  }
}