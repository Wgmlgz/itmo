import { PrismaModule } from './prisma.module';
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { AuthModule } from './auth/auth.module';
import { PrismaService } from './prisma.service';
import { JwtModule, JwtService } from '@nestjs/jwt';

@Module({
  imports: [AuthModule, PrismaModule, JwtModule],
  controllers: [AppController],
  providers: [AppService, PrismaService, JwtService],
})
export class AppModule {}
