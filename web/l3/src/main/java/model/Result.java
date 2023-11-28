package model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "sus")
public class Result {
    @Id
    @Column(name = "id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(name = "x")
    private Double x;
    @Column(name = "y")
    private Double y;
    @Column(name = "r")
    private Double r;
    @Column(name = "result")
    private Boolean inside = false;
    
    public Result() {
        super();
    }


    public void setX(Double x) {
        this.x = x;
    }

    public Double getX() {
        return x;
    }


    public void setY(Double y) {
        this.y = y;
    }

    public Double getY() {
        return y;
    }


    public void setR(Double r) {
        this.r = r;
    }

    public Double getR() {
        return r;
    }

    public boolean isInside() {
        return inside;
    }

    public void setInside(boolean inside) {
        this.inside = inside;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }
}

