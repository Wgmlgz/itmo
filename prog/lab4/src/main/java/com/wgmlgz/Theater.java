package com.wgmlgz;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

class Theater extends Stage implements Movable {
  MoteTarget location = MoteTarget.ShallowWater;

  List<Lamp> lamps = new ArrayList<>();

  public static class Sun {
    double angle = 0;

    public void setAngle(double angle) {
      this.angle = angle;
    }
    public void printState() {
      if (angle < 12) {
        System.out.println("The sun is rising");
      } else {
        System.out.println("The sun is setting");
      }
    }
  }

  public class Curtain {
    String color;
    String description;

    Curtain(String color, String description) {
      this.color = color;
      this.description = description;
    }

    public void describe() {
      System.out.format("Curtain is %s and %s\n", color, description);
    }
  }

  public Curtain curtain = new Curtain("red", "mysterious");

  Theater(Entity director, List<Entity> actors) {
    super(director, actors);

    this.lamps.add(new Lamp());
    this.lamps.add(new Lamp());
    this.lamps.add(new Lamp());
    this.lamps.add(new Lamp());
  }

  public void perform(Show show) {
    System.out.format("%s at %s!\n", super.play(show), this.location.name());
  }

  @Override
  public void move(MoteTarget target) {
    this.location = target;
    System.out.format("Moving theater to -> %s\n", this.location.name());
  }

  public void swithLights(boolean state) {
    for (var lamp : lamps) {
      lamp.on = state;
    }
    System.out.format("Lamps are %s!\n", state ? "on" : "off");
  }

  @Override
  public String toString() {
    return String.format("%s with %s by %s", this.location.name(),
        actors.stream().map(Object::toString).collect(Collectors.joining(", ")),
        director.toString());
  }

  @Override
  public boolean equals(Object obj) {
    if (!(obj instanceof Theater)) {
      return false;
    }
    return this.actors.equals(((Theater) obj).actors) &&
        this.director.equals(((Theater) obj).director) &&
        this.location.equals(((Theater) obj).location) &&
        this.lamps.equals(((Theater) obj).lamps);
  }

  @Override
  public int hashCode() {
    return this.actors.hashCode() ^ this.director.hashCode() ^ this.location.hashCode() ^ this.lamps.hashCode();
  }
}