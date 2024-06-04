package model;

import java.util.Collection;

public interface ResultDAO {
    void save(Result result);
    void update(Long point_id, Result result);
    void delete(Result result);
    void clear();
    Result getResultByID(Long result_id);
    Collection<Result> getAllResults();
}
