package com.wgmlgz;

import java.util.Random;

import ru.ifmo.se.pokemon.*;

class Lab2 {
  public static void main(String[] args) {
    System.out.println("sus");
    Battle b = new Battle();
    Pokemon p1 = new Pokemon("aaa", 1);
    Pokemon p2 = new Pokemon("bbb", 1);
    b.addAlly(p1);
    b.addFoe(p2);
    b.go();
    System.out.println("sus");
  }
}
