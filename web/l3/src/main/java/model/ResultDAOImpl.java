package model;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.Persistence;
import java.sql.SQLException;
import java.util.Collection;
import jakarta.persistence.Query;
import org.eclipse.persistence.sessions.Session;
import java.sql.SQLException;
import java.util.Collection;
import java.util.List;


public class ResultDAOImpl implements ResultDAO {

    private static final String PERSISTENCE_UNIT_NAME = "your_persistence_unit_name"; // Replace with your persistence
                                                                                      // unit name

    @Override
    public void save(Result result) throws SQLException {
        EntityManagerFactory entityManagerFactory = null;
        EntityManager entityManager = null;
        try {
            entityManagerFactory = Persistence.createEntityManagerFactory(PERSISTENCE_UNIT_NAME);
            entityManager = entityManagerFactory.createEntityManager();
            EntityTransaction transaction = entityManager.getTransaction();

            transaction.begin();
            entityManager.persist(result);
            transaction.commit();
        } catch (Exception e) {
            System.err.println("Something went wrong in DAO: " + e);
            throw new SQLException(e);
        } finally {
            if (entityManager != null && entityManager.isOpen()) {
                entityManager.close();
            }
            if (entityManagerFactory != null && entityManagerFactory.isOpen()) {
                entityManagerFactory.close();
            }
        }
    }

    @Override
    public void update(Long point_id, Result result) throws SQLException {
        EntityManagerFactory entityManagerFactory = null;
        EntityManager entityManager = null;
        try {
            entityManagerFactory = Persistence.createEntityManagerFactory(PERSISTENCE_UNIT_NAME);
            entityManager = entityManagerFactory.createEntityManager();
            EntityTransaction transaction = entityManager.getTransaction();

            transaction.begin();
            result.setId(point_id); // Assuming the id needs to be set for update
            entityManager.merge(result);
            transaction.commit();
        } catch (Exception e) {
            System.err.println("Something went wrong in DAO: " + e);
            throw new SQLException(e);
        } finally {
            if (entityManager != null && entityManager.isOpen()) {
                entityManager.close();
            }
            if (entityManagerFactory != null && entityManagerFactory.isOpen()) {
                entityManagerFactory.close();
            }
        }
    }

    @Override
    public void delete(Result result) throws SQLException {
        EntityManagerFactory entityManagerFactory = null;
        EntityManager entityManager = null;
        try {
            entityManagerFactory = Persistence.createEntityManagerFactory(PERSISTENCE_UNIT_NAME);
            entityManager = entityManagerFactory.createEntityManager();
            EntityTransaction transaction = entityManager.getTransaction();

            transaction.begin();
            entityManager.remove(entityManager.contains(result) ? result : entityManager.merge(result));
            transaction.commit();
        } catch (Throwable e) {
            System.err.println("Something went wrong in DAO: " + e);
            throw new SQLException(e);
        } finally {
            if (entityManager != null && entityManager.isOpen()) {
                entityManager.close();
            }
            if (entityManagerFactory != null && entityManagerFactory.isOpen()) {
                entityManagerFactory.close();
            }
        }
    }

    public final String TABLE_NAME = "results";

    @Override
    public void clear() throws SQLException {
        EntityManager entityManager = null;
        try {
            entityManager = getEntityManager();
            EntityTransaction transaction = entityManager.getTransaction();

            transaction.begin();
            Query query = entityManager.createNativeQuery("DELETE FROM results");
            query.executeUpdate();
            transaction.commit();
        } catch (Throwable e) {
            System.err.println("Something went wrong in DAO: " + e);
            throw new SQLException(e);
        } finally {
            if (entityManager != null && entityManager.isOpen()) {
                entityManager.close();
            }
        }
    }

    @Override
    public Result getResultByID(Long result_id) throws SQLException {
        EntityManager entityManager = null;
        Result result;
        try {
            entityManager = getEntityManager();
            result = entityManager.find(Result.class, result_id);
        } catch (Throwable e) {
            System.err.println("Something went wrong in DAO: " + e);
            throw new SQLException(e);
        } finally {
            if (entityManager != null && entityManager.isOpen()) {
                entityManager.close();
            }
        }
        return result;
    }

    @Override
    public Collection<Result> getAllResults() throws SQLException {
        EntityManager entityManager = null;
        List<Result> results;
        try {
            entityManager = getEntityManager();
            results = entityManager.createQuery("SELECT r FROM Result r", Result.class).getResultList();
        } catch (Throwable e) {
            System.err.println("Something went wrong in DAO: " + e);
            throw new SQLException(e);
        } finally {
            if (entityManager != null && entityManager.isOpen()) {
                entityManager.close();
            }
        }
        return results;
    }

    private EntityManager getEntityManager() {
        return Persistence.createEntityManagerFactory(PERSISTENCE_UNIT_NAME).createEntityManager();
    }
}
