package model;

public interface ClickIntervalTrackerMBean {
    double getAverageInterval();
    void resetTracking();
}
