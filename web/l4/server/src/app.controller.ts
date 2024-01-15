import {
  BadRequestException,
  Controller,
  Delete,
  Get,
  Query,
  Request,
  UseGuards,
} from '@nestjs/common';
import { AppService } from './app.service';
import { Point } from './point.dto';
import { PrismaService } from './prisma.service';
import { validate } from 'class-validator';
import { AuthGuard } from './auth/auth.guard';

@Controller()
export class AppController {
  constructor(
    private readonly appService: AppService,
    private readonly prisma: PrismaService,
  ) {}

  @UseGuards(AuthGuard)
  @Get('check-point')
  async checkPoint(
    @Query() { x, y, r }: any,
    @Request() req,
  ): Promise<{
    x: number;
    y: number;
    r: number;
    hit: boolean;
  }> {
    const point = new Point();
    point.x = Number(x);
    point.y = Number(y);
    point.r = Number(r);

    const res = await validate(point);
    if (res.length) {
      throw new BadRequestException(
        res
          .map((e) => {
            const s = e.toString();
            return s;
          })
          .join('\n'),
      );
    }

    ({ x, y, r } = point);
    const hit = this.appService.checkHit(point);
    await this.prisma.checkResult.create({
      data: {
        x,
        y,
        r,
        userId: req.user.id,
        hit,
      },
    });
    return {
      ...point,
      hit,
    };
  }

  @UseGuards(AuthGuard)
  @Get('results')
  async getResults(@Request() req) {
    const results = await this.prisma.checkResult.findMany({
      where: {
        userId: req.user.id,
      },
    });
    return results;
  }

  @UseGuards(AuthGuard)
  @Delete('results')
  async deleteResults(@Request() req) {
    const results = await this.prisma.checkResult.deleteMany({
      where: {
        userId: req.user.id,
      },
    });
    return results;
  }
}
