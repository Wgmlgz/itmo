package model;

import java.util.ArrayList;
import java.util.List;

public class ClickIntervalTracker implements ClickIntervalTrackerMBean {
  private static ClickIntervalTracker instance;
  private List<Long> clickTimes = new ArrayList<>();

  private ClickIntervalTracker() {
  }

  public static synchronized ClickIntervalTracker getInstance() {
    if (instance == null) {
      instance = new ClickIntervalTracker();
    }
    return instance;
  }

  @Override
  public double getAverageInterval() {
    if (clickTimes.size() < 2) {
      return 0;
    }
    long sumIntervals = 0;
    for (int i = 1; i < clickTimes.size(); i++) {
      sumIntervals += (clickTimes.get(i) - clickTimes.get(i - 1));
    }
    return sumIntervals / (double) (clickTimes.size() - 1);
  }

  @Override
  public void resetTracking() {
    clickTimes.clear();
  }

  public void recordClick() {
    clickTimes.add(System.currentTimeMillis());
  }
}
