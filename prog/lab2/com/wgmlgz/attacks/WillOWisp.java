package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class WillOWisp extends StatusMove {
  public WillOWisp() {
    super(Type.PSYCHIC, 0, 0);
  }

  @Override
  protected void applyOppEffects(Pokemon p) {
    Effect.burn(p);
  }

  @Override
  protected String describe() {
    return "uses WillOWisp ";
  }
}
