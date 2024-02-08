/*
  Warnings:

  - Added the required column `userId` to the `CheckResult` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "CheckResult" ADD COLUMN     "userId" INTEGER NOT NULL;

-- AddForeignKey
ALTER TABLE "CheckResult" ADD CONSTRAINT "CheckResult_userId_fkey" FOREIGN KEY ("userId") REFERENCES "Users"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
