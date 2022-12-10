package com.wgmlgz;

import java.util.*;

public class Lab4 {
  public static void main(String[] args) {
    var moominpappa = new Troll("Moominpappa", "rewriting the play", 0.1);

    List<Entity> beavers = new ArrayList<>();
    beavers.add(new Beaver("Beaver 1", "uncertain", 0.1));
    beavers.add(new Beaver("Beaver 2", "uncertain", 0.1));
    beavers.add(new Beaver("Beaver 666", "uncertain", 0.1));

    var repetition = new Show("Moominpappa's play repetition");
    var theater = new Theater(moominpappa, beavers);

    theater.swithLights(true);
    theater.move(MoteTarget.DeepWater);
    theater.perform(repetition);
    theater.rotate(10);

    theater.curtain.describe();
    var sun = new Theater.Sun();
    sun.printState();

    try {
      moominpappa.isReady();
    } catch (ReadyError e) {
      System.out.println(e.toString());
    }

    for (var i : beavers) {
      try {
        i.confidenceCheck();
      } catch (ConfidenceError e) {
        System.out.println(e.toString());
      }
    }
  }
}