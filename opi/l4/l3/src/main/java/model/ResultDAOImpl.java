package model;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class ResultDAOImpl implements ResultDAO {
    private final Map<Long, Result> results = new HashMap<>();
    private long currentId = 1;

    @Override
    public void save(Result result) {
        result.setId(currentId++);
        results.put(result.getId(), result);
    }

    @Override
    public void update(Long point_id, Result result) {
        if (results.containsKey(point_id)) {
            results.put(point_id, result);
        }
    }

    @Override
    public void delete(Result result) {
        results.remove(result.getId());
    }

    @Override
    public void clear() {
        results.clear();
    }

    @Override
    public Result getResultByID(Long result_id) {
        return results.get(result_id);
    }

    @Override
    public Collection<Result> getAllResults() {
        return results.values();
    }
}
