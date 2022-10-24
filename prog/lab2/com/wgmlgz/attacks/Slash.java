package com.wgmlgz.attacks;

import ru.ifmo.se.pokemon.*;

public class Slash extends PhysicalMove {
  public Slash() {
    super(Type.PSYCHIC, 70, 100);
  }

  @Override
  protected double calcCriticalHit(Pokemon pokemon, Pokemon pokemon1) {
    if (pokemon1.getStat(Stat.SPEED) / (512.0 / 3.0) > Math.random()) {
      System.out.println("crits!");
      return 2.0;
    } else {
      return 1.0;
    }
  }

  @Override
  protected String describe() {
    return "uses  Slash ";
  }
}