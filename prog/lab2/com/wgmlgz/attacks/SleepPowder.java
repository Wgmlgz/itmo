package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class SleepPowder extends StatusMove {
  public SleepPowder() {
    super(Type.PSYCHIC, 0, 0);
  }

  @Override
  protected void applyOppEffects(Pokemon p) {
    p.addEffect((new Effect()).condition(Status.SLEEP).turns((int)(Math.random() * 3.0 + 1.0)));
  }

  @Override
  protected String describe() {
    return "uses SleepPowder ";
  }
}