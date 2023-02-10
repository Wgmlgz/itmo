package com.wgmlgz;

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