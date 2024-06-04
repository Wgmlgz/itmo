package model;

import javax.management.*;
import java.beans.ConstructorProperties;
import java.util.logging.Logger;

public class PointTracker implements PointTrackerMBean, NotificationBroadcaster {
    private static PointTracker instance;
    private static final Logger LOGGER = Logger.getLogger(PointTracker.class.getName());

    private int totalPoints = 0;
    private int pointsOutsideArea = 0;
    private long sequenceNumber = 1;
    private NotificationBroadcasterSupport notificationBroadcaster;

    @ConstructorProperties({ "totalPoints", "pointsOutsideArea" })
    private PointTracker() {
        notificationBroadcaster = new NotificationBroadcasterSupport();
    }

    public static synchronized PointTracker getInstance() {
        if (instance == null) {
            instance = new PointTracker();
        }
        return instance;
    }

    @Override
    public int getTotalPoints() {
        return totalPoints;
    }

    @Override
    public int getPointsOutsideArea() {
        return pointsOutsideArea;
    }

    @Override
    public void resetCounters() {
        totalPoints = 0;
        pointsOutsideArea = 0;
    }

    public void addPoint(boolean isInside, double x, double y) {
        LOGGER.info("Adding point: isInside=" + isInside + ", x=" + x + ", y=" + y);
        totalPoints++;
        if (!isInside) {
            pointsOutsideArea++;

        }
        if (x > 2 || y > 2 || y < -2 || x < -2) {
            notificationBroadcaster.sendNotification(new Notification("model.PointTracker.outOfBounds",
                    this,
                    sequenceNumber++,
                    System.currentTimeMillis(),
                    "Point out of bounds: (" + x + ", " + y + ")"));
        }

    }

    @Override
    public void addNotificationListener(NotificationListener listener, NotificationFilter filter, Object handback)
            throws IllegalArgumentException {
        notificationBroadcaster.addNotificationListener(listener, filter, handback);
    }

    @Override
    public void removeNotificationListener(NotificationListener listener) throws ListenerNotFoundException {
        notificationBroadcaster.removeNotificationListener(listener);
    }

    @Override
    public MBeanNotificationInfo[] getNotificationInfo() {
        String[] types = new String[] { AttributeChangeNotification.ATTRIBUTE_CHANGE };
        String name = AttributeChangeNotification.class.getName();
        String description = "Notification that sends when a point is out of bounds";
        return new MBeanNotificationInfo[] { new MBeanNotificationInfo(types, name, description) };
    }
}
