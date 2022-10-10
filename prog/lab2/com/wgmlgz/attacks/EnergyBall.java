package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class EnergyBall extends StatusMove {
  public EnergyBall() {
    super(Type.PSYCHIC, 0, 0);
  }

  @Override
  protected void applySelfEffects(Pokemon p) {
    Effect eff = new Effect();
    eff = eff.condition(Status.SLEEP);
    eff = eff.turns(2);
    p.restore();
    p.addEffect(eff);
  }

  @Override
  protected String describe() {
    return "использует EnergyBall ";
  }
}