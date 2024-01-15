import { Injectable } from '@nestjs/common';
import { Point } from './point.dto';

@Injectable()
export class AppService {
  checkHit({ x, y, r }: Point): boolean {
    if (x >= 0 && y >= 0 && x <= r && y <= r) {
      return true;
    }

    if (x <= 0 && y >= 0 && -x * 2 + y <= r) {
      return true;
    }

    if (x <= 0 && y <= 0 && x * x + y * y <= (r / 2) * (r / 2)) {
      return true;
    }

    return false;
  }
}
