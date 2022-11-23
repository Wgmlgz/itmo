package com.wgmlgz;

import java.util.*;
import java.util.stream.Collectors;

class Lamp {
  boolean on = false;

  @Override
  public boolean equals(Object obj) {
    if (!(obj instanceof Lamp)) {
      return false;
    }

    return this.on == ((Lamp) obj).on;
  }

  @Override
  public String toString() {
    return String.format("Lamp is %s", this.on ? "on" : "off");
  }

  @Override
  public int hashCode() {
    return (this.on) ? 1 : 0;
  }
}

abstract class Entity {
  String name;

  Entity(String name) {
    this.name = name;
  }

  @Override
  public String toString() {
    return name;
  }

  @Override
  public boolean equals(Object obj) {
    if (!(obj instanceof Lamp)) {
      return false;
    }
    return this.name.equals(((Entity) obj).name);
  }

  @Override
  public int hashCode() {
    return this.name.hashCode();
  }
}

class Beaver extends Entity {
  Beaver(String name) {
    super(name);
  }
}

class Troll extends Entity {
  Troll(String name) {
    super(name);
  }
}

enum MoteTarget {
  ShallowWater,
  DeepWater,
}

interface Movable {
  void move(MoteTarget target);
}

interface Rotatable {
  void rotate(double angle);
}

interface Playable {
  String play();
}

class Show implements Playable {
  String title;

  Show(String title) {
    this.title = title;
  }

  public String play() {
    return String.format("Performing %s", this.title);
  }

  @Override
  public String toString() {
    return title;
  }

  @Override
  public boolean equals(Object obj) {
    if (!(obj instanceof Show)) {
      return false;
    }
    return this.title.equals(((Show) obj).title);
  }

  @Override
  public int hashCode() {
    return this.title.hashCode();
  }
}

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

class Theater extends Stage implements Movable {
  MoteTarget location = MoteTarget.ShallowWater;

  List<Lamp> lamps = new ArrayList<>();

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

public class Lab3 {
  public static void main(String[] args) {
    var moominpappa = new Troll("Moominpappa");

    List<Entity> beavers = new ArrayList<>();
    beavers.add(new Beaver("Sus"));
    beavers.add(new Beaver("Impostror"));
    beavers.add(new Beaver("Amogus"));

    var repetition = new Show("Moominpappa's play repetition");
    var theater = new Theater(moominpappa, beavers);

    theater.swithLights(true);
    theater.move(MoteTarget.DeepWater);
    theater.perform(repetition);
    theater.rotate(10);

  }
}