package model;

public interface PointTrackerMBean {
    int getTotalPoints();
    int getPointsOutsideArea();
    void resetCounters();
}
