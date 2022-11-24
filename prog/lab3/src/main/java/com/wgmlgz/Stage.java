package com.wgmlgz;

import java.util.List;
import java.util.stream.Collectors;

abstract class Stage implements Rotatable {
  List<Entity> actors;
  Entity director;
  double angle = 0;

  Stage(Entity director, List<Entity> actors) {
    this.director = director;
    this.actors = actors;
  }

  public String play(Show show) {
    return String.format("%s with:\n  %s\nby %s", show.play(),
        actors.stream().map(Object::toString).collect(Collectors.joining(",\n  ")), director.toString());
  }

  public void rotate(double angle) {
    this.angle = angle;
    System.out.format("Stage is rotating by %.1f °...", angle);
    if (angle < 30) {
      System.out.println("  but it's comfortable!");
    }
  }
}