package com.wgmlgz;

abstract class Entity {
  String name;
  String unconfidentMsg;
  double confidence;

  Entity(String name, String unconfidentMsg, double confidence) {
    this.name = name;
    this.unconfidentMsg = unconfidentMsg;
    this.confidence = confidence;
  }

  public void confidenceCheck() throws ConfidenceError {
    if (confidence < 0.5) {
      throw new ConfidenceError(name + " is " + unconfidentMsg);
    }
  }

  public void Eat() {
    class Food {
      double calories;

      Food(double calories) {
        this.calories = calories;
      }
    }

    var dinner = new Food(20) {
      String name = "dinner";
    };

    System.out.println("Eating" + dinner.name + dinner.calories);
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