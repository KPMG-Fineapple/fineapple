import { Module } from '@nestjs/common';
import { PowerGenerationController } from './power-generation.controller';
import { PowerGenerationService } from './power-generation.service';

@Module({
  controllers: [PowerGenerationController],
  providers: [PowerGenerationService]
})
export class PowerGenerationModule {}
