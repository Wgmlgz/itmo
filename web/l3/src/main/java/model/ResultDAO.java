package model;

import java.sql.SQLException;
import java.util.Collection;

public interface ResultDAO {
    void save(Result result) throws SQLException;
    void update(Long point_id, Result result) throws SQLException;
    void delete(Result result) throws SQLException;
    void clear() throws SQLException;
    Result getResultByID(Long result_id) throws SQLException;
    Collection<Result> getAllResults() throws SQLException;
}
