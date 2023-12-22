package com.wgmlgz;

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