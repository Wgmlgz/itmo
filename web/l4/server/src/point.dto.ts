import { IsNumber, Min, Max } from 'class-validator';

export class Point {
  @IsNumber()
  @Min(-4)
  @Max(4)
  x: number;

  @IsNumber()
  @Min(-3)
  @Max(5)
  y: number;

  @IsNumber()
  @Min(0)
  @Max(4)
  r: number;
}
