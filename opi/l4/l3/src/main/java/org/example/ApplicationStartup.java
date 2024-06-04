package org.example;

import jakarta.servlet.ServletContextEvent;
import jakarta.servlet.ServletContextListener;
import jakarta.servlet.annotation.WebListener;

import javax.management.*;
import java.lang.management.ManagementFactory;

import model.PointTracker;
import model.ClickIntervalTracker;

@WebListener
public class ApplicationStartup implements ServletContextListener {

    @Override
    public void contextInitialized(ServletContextEvent sce) {
        try {
            MBeanServer mBeanServer = ManagementFactory.getPlatformMBeanServer();
            ObjectName pointTrackerName = new ObjectName("com.example:type=PointTracker");
            PointTracker pointTracker = PointTracker.getInstance();
            mBeanServer.registerMBean(pointTracker, pointTrackerName);

            ObjectName clickTrackerName = new ObjectName("com.example:type=ClickIntervalTracker");
            ClickIntervalTracker clickTracker = ClickIntervalTracker.getInstance();
            mBeanServer.registerMBean(clickTracker, clickTrackerName);
        } catch (MalformedObjectNameException | InstanceAlreadyExistsException |
                 MBeanRegistrationException | NotCompliantMBeanException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void contextDestroyed(ServletContextEvent sce) {
        // Optionally implement logic to clean up resources or unregister MBeans
    }
}
