package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class Rest extends StatusMove {
  public Rest() {
    super(Type.PSYCHIC, 0, 0);
  }

  @Override
  protected void applySelfEffects(Pokemon p) {
    new Effect().turns(2).sleep(p);
  }

  @Override
  protected String describe() {
    return "uses Rest";
  }
}