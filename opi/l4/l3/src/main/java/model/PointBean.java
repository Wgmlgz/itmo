package model;

import jakarta.annotation.PostConstruct;
import jakarta.enterprise.context.SessionScoped;
import jakarta.inject.Named;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.io.Serializable;

@Named("bean")
@SessionScoped
public class PointBean implements Serializable {

    @PostConstruct
    public void init() {
        x = 0d;
        y = 0d;
        r = 2.0;
    }

    private Double x;
    private Double y;
    private Double r;

    private List<Result> results = new ArrayList<>();
    private Result lastCheckedPoint;
    private PointTracker pointTracker = PointTracker.getInstance();
    private ClickIntervalTracker clickTracker = ClickIntervalTracker.getInstance();

    public PointBean() {
        super();
        results = new ArrayList<>();
        try {
            results = new ArrayList<>(DAOFactory.getInstance().getResultDAO().getAllResults());
        } catch (Exception ignored) {
        }
    }

    public List<Result> getResults() {
        return results;
    }

    public Result getLastCheckedPoint() {
        if (lastCheckedPoint == null) {
            lastCheckedPoint = new Result();
        }
        return lastCheckedPoint;
    }

    public Double getX() {
        return x;
    }

    public void setX(Double x) {
        this.x = x;
    }

    public Double getY() {
        return y;
    }

    public void setY(Double y) {
        this.y = y;
    }

    public Double getR() {
        return r;
    }

    public void setR(Double r) {
        this.r = r;
    }

    // Add to the PointBean class

    public void checkPoint() {
        clickTracker.recordClick();
        boolean isInside = (((x > 0 && y > 0) && (x * x + y * y <= (r / 2) * (r / 2))) ||
                ((x <= 0 && y > 0) && (x >= -r && y <= r)) ||
                ((x <= 0 && y <= 0) && (-y + (-x) <= r)) ||
                ((x >= 0 && y <= 0) && false));
        pointTracker.addPoint(isInside, x, y); // Update MBean state

        Result result = new Result();
        result.setX(x);
        result.setY(y);
        result.setR(r);
        result.setInside(isInside);
        try {
            DAOFactory.getInstance().getResultDAO().save(result);
        } catch (Exception e) {
        }
        results.add(result);
        lastCheckedPoint = result;
    }

    // public void checkPoint() {
    // boolean isInside = //
    // (((x > 0 && y > 0) && (x * x + y * y <= (r / 2) * (r / 2))) ||
    // ((x <= 0 && y > 0) && (x >= -r && y <= r)) ||
    // ((x <= 0 && y <= 0) && (-y + (-x) <= r)) ||
    // ((x >= 0 && y <= 0) && false));

    // Result result = new Result();
    // result.setX(x);
    // result.setY(y);
    // result.setR(r);
    // result.setInside(isInside);
    // try {
    // DAOFactory.getInstance().getResultDAO().save(result);
    // } catch (Exception e) {
    // }
    // results.add(result);
    // lastCheckedPoint = new Result();
    // lastCheckedPoint.setX(x);
    // lastCheckedPoint.setY(y);
    // lastCheckedPoint.setR(r);
    // lastCheckedPoint.setInside(isInside);
    // }

    @Override
    public String toString() {
        return "x=" + x +
                ", y=" + y +
                ", a=" + lastCheckedPoint.isInside();
    }
}
