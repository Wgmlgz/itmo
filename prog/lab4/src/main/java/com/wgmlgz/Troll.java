package com.wgmlgz;

class Troll extends Entity {
  Troll(String name, String unconfidentMsg, double confidence) {
    super(name, unconfidentMsg, confidence);
  }

  public void isReady() {
    if (confidence < 0.5) {
      throw new ReadyError(name + " is " + unconfidentMsg);
    }
  }
}