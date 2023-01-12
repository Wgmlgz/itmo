package com.wgmlgz;

import java.util.*;

public class Lab4 {
  public static void main(String[] args) {
    var sus = new Integer(2);
    sus += 2;
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
    Theater.Sun.printState();

    try {
      moominpappa.isReady();
    } catch (ReadyError e) {
      System.out.println(e.toString());
    } finally {
      System.out.println("test");
    }
    System.out.println("test");

    for (var i : beavers) {
      try {
        i.confidenceCheck();
      } catch (ConfidenceError | ArithmeticException e) {
      
        System.out.println(e.toString());
      }
    }
  }
}