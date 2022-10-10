package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class DreamEater extends SpecialMove {
  public DreamEater() {
    super(Type.PSYCHIC, 100, 100);
  }

  @Override
  protected void applyOppEffects(Pokemon p) {
    p.addEffect(new Effect().condition(Status.SLEEP));
  }

  protected void applySelfEffects(Pokemon p) {
    p.addEffect(new Effect().stat(Stat.HP, 50));
  }

  @Override
  protected String describe() {
    return "uses DreamEater";
  }
}