/*
  Warnings:

  - You are about to drop the column `createdAt` on the `CheckResult` table. All the data in the column will be lost.
  - You are about to drop the column `userId` on the `CheckResult` table. All the data in the column will be lost.

*/
-- DropForeignKey
ALTER TABLE "CheckResult" DROP CONSTRAINT "CheckResult_userId_fkey";

-- AlterTable
ALTER TABLE "CheckResult" DROP COLUMN "createdAt",
DROP COLUMN "userId";
