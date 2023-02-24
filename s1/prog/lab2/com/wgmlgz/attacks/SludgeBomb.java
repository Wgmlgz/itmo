package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class SludgeBomb extends StatusMove {
  public SludgeBomb() {
    super(Type.PSYCHIC, 0, 0);
  }

  @Override
  protected void applyOppEffects(Pokemon p) {
    if (!p.hasType(Type.POISON) && !p.hasType(Type.STEEL)) {
      Effect var1 = (new Effect()).condition(Status.POISON).turns(-1);
      p.setCondition(var1);
    }
  }

  @Override
  protected String describe() {
    return "uses SludgeBomb ";
  }
}