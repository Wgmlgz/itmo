package com.wgmlgz;

import java.util.*;

public class Lab3 {
  public static void main(String[] args) {
    var moominpappa = new Troll("Moominpappa");

    List<Entity> beavers = new ArrayList<>();
    beavers.add(new Beaver("Beaver 1"));
    beavers.add(new Beaver("Beaver 2"));
    beavers.add(new Beaver("Beaver 666"));

    var repetition = new Show("Moominpappa's play repetition");
    var theater = new Theater(moominpappa, beavers);

    theater.swithLights(true);
    theater.move(MoteTarget.DeepWater);
    theater.perform(repetition);
    theater.rotate(10);
  }
}