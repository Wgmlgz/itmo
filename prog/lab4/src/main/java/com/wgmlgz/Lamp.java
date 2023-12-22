package com.wgmlgz;

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