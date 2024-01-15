// src/auth/auth.service.ts

import { HttpException, HttpStatus, Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma.service';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';

@Injectable()
export class AuthService {
  constructor(
    private readonly prisma: PrismaService,
    private readonly jwtService: JwtService,
  ) {}

  async login({ username, password }: { username: string; password: string }) {
    const user = await this.prisma.users.findFirstOrThrow({
      where: {
        username: username,
      },
    });

    if (!user || !bcrypt.compareSync(password, user.passwordHash)) {
      throw new HttpException('Invalid credentials', HttpStatus.UNAUTHORIZED);
    }

    const accessToken = this.jwtService.sign({
      username: user.username,
      id: user.id,
    });
    return accessToken;
  }

  async register({
    username,
    password,
  }: {
    username: string;
    password: string;
  }) {
    // Hash the password before storing it
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create a new user in the database
    const newUser = await this.prisma.users.create({
      data: {
        username,
        passwordHash: hashedPassword,
      },
    });

    return newUser;
  }
}
