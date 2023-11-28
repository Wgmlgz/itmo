package model;

import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

public class Factory {
    private static EntityManagerFactory entityManagerFactory;

    private Factory() {}

    public static EntityManagerFactory getEntityManagerFactory() {
        if (entityManagerFactory == null) {
            try {
                entityManagerFactory = Persistence.createEntityManagerFactory("default"); // Replace with your persistence unit name
            } catch (Exception e) {
                System.out.println("error:: " + e);
            }
        }

        return entityManagerFactory;
    }
}
