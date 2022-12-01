package com.wgmlgz;

import java.util.*;

public class Lab4 {
  public static void main(String[] args) {
    var moominpappa = new Troll("Moominpappa", "rewriting the play", 0.1);

    List<Entity> beavers = new ArrayList<>();
    beavers.add(new Beaver("Beaver 1", "unconfiden", 0.1));
    beavers.add(new Beaver("Beaver 2", "unconfiden", 0.1));
    beavers.add(new Beaver("Beaver 666", "unconfiden", 0.1));

    var repetition = new Show("Moominpappa's play repetition");
    var theater = new Theater(moominpappa, beavers);

    theater.swithLights(true);
    theater.move(MoteTarget.DeepWater);
    theater.perform(repetition);
    theater.rotate(10);

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